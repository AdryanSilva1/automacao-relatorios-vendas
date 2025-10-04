import pandas as pd
from datetime import datetime
from typing import Optional

def ler_dados(caminho_csv: str) -> Optional[pd.DataFrame]:
    """
    Lê o arquivo CSV com tratamento de erros.
    
    Args:
        caminho_csv: caminho do arquivo CSV
    
    Returns:
        DataFrame limpo ou None se houver erro
    """
    try:
        df = pd.read_csv(
            caminho_csv,
            na_values=['', 'N/A', 'Unknown', 'NULL'],  # Trata valores ausentes
            dtype={'valor': float},  # Garante que valor seja float
            parse_dates=['data']  # Converte coluna data para datetime
        )
        return df
    except FileNotFoundError:
        print("Erro: Arquivo CSV não encontrado!")
        return None
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        return None

def gerar_resumo(caminho_csv: str) -> str:
    """
    Gera um resumo financeiro das vendas.

    Args:
        caminho_csv: caminho do arquivo CSV
    
    Returns:
        Resumo formatado como string
    """
    df = ler_dados(caminho_csv)
    
    if df is None or df.empty:
        return "Não foi possível gerar o relatório. Verifique os dados."
    
    # Remove registros sem valor
    df_limpo = df.dropna(subset=['valor'])
    
    # Cálculos principais
    total_vendas = df_limpo['valor'].sum()
    quantidade_vendas = len(df_limpo)
    ticket_medio = total_vendas / quantidade_vendas if quantidade_vendas else 0
    media_vendas = df_limpo['valor'].mean() if quantidade_vendas else 0
    maior_venda = df_limpo['valor'].max() if quantidade_vendas else 0
    menor_venda = df_limpo['valor'].min() if quantidade_vendas else 0
    data_mais_recente = df_limpo['data'].max() if quantidade_vendas else None
    clientes_unicos = df_limpo['cliente'].nunique() if quantidade_vendas else 0
    
    # Formatação do relatório
    resumo = (
        f"RELATÓRIO DE VENDAS - {datetime.now().strftime('%d/%m/%Y')}\n\n"
        f"RESUMO FINANCEIRO:\n"
        f" - Total vendido: R$ {total_vendas:,.2f}\n"
        f" - Ticket médio: R$ {ticket_medio:,.2f}\n"
        f" - Maior venda: R$ {maior_venda:,.2f}\n"
        f" - Menor venda: R$ {menor_venda:,.2f}\n\n"
        f"ESTATÍSTICAS:\n"
        f" - Quantidade de vendas: {quantidade_vendas}\n"
        f" - Clientes únicos: {clientes_unicos}\n"
        f" - Data mais recente: {data_mais_recente.strftime('%d/%m/%Y') if data_mais_recente else 'N/A'}\n\n"
        f"OBSERVAÇÕES:\n"
        f" - {len(df) - len(df_limpo)} venda(s) com valor faltante foram ignoradas\n"
        f" - Período analisado: Todas as datas disponíveis\n"
    )
    
    return resumo

def gerar_resumo_detalhado(caminho_csv: str) -> str:
    """
    Gera um relatório detalhado para análise interna, incluindo vendas por dia
    e destaque do produto mais vendido.

    Args:
        caminho_csv: caminho do arquivo CSV
    
    Returns:
        Resumo detalhado como string
    """
    df = ler_dados(caminho_csv)
    
    if df is None or df.empty:
        return "Não foi possível gerar o relatório detalhado."
    
    df_limpo = df.dropna(subset=['valor'])
    
    # Vendas por dia
    vendas_por_dia = df_limpo.groupby(df_limpo['data'].dt.date)['valor'].sum()
    produto_mais_vendido = df_limpo['produto'].mode().iloc[0] if not df_limpo.empty else "N/A"
    
    # Monta relatório detalhado com bullets HTML-friendly
    resumo_detalhado = (
        f" RELATÓRIO DETALHADO - {datetime.now().strftime('%d/%m/%Y %H:%M')}\n\n"
        f"Vendas por dia:\n"
    )
    
    for data, total in vendas_por_dia.items():
        resumo_detalhado += f"   • {data.strftime('%d/%m')}: R$ {total:,.2f}\n"
    
    resumo_detalhado += (
        f"\n DESTAQUES:\n"
        f"   • Produto mais vendido: {produto_mais_vendido}\n"
        f"   • Total de registros analisados: {len(df)} (válidos: {len(df_limpo)})\n"
    )
    
    return resumo_detalhado
