#!/usr/bin/env python3
"""
Sistema de Automação de Relatórios de Vendas
Autor: Adryan Silva
Data: 2025
"""

import os
import argparse
import logging
from report_utils import gerar_resumo, gerar_resumo_detalhado
from email_utils import enviar_relatorio

# Configura logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def main() -> None:
    """Função principal do sistema"""
    parser = argparse.ArgumentParser(description='Sistema de Relatórios de Vendas')
    parser.add_argument('--email', help='E-mail do destinatário')
    parser.add_argument('--tipo', choices=['simples', 'detalhado'], default='simples',
                        help='Tipo de relatório (padrão: simples)')
    parser.add_argument('--csv', default='data/vendas.csv', help='Caminho do arquivo CSV de vendas')
    
    args = parser.parse_args()
    caminho_csv = args.csv
    
    logging.info("Iniciando sistema de relatórios...")
    logging.info(f"Arquivo de dados: {caminho_csv}")
    
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_csv):
        print("\033[91m[ERRO] Arquivo de vendas não encontrado!\033[0m")
        return
    
    # Gera relatório
    if args.tipo == 'detalhado':
        relatorio = gerar_resumo_detalhado(caminho_csv)
    else:
        relatorio = gerar_resumo(caminho_csv)
    
    print("\n" + "="*60)
    print(relatorio)
    print("="*60)
    
    # Envio por e-mail
    if args.email:
        logging.info(f"Enviando relatório para: {args.email}")
        sucesso = enviar_relatorio(args.email, caminho_csv, args.tipo)
        if sucesso:
            print("\033[92m[SUCESSO] Relatório enviado com sucesso!\033[0m")
        else:
            print("\033[91m[FALHA] Não foi possível enviar o e-mail.\033[0m")
    else:
        logging.info("Dica: Use --email para enviar automaticamente por e-mail")
        logging.info("Exemplo: python main.py --email seu@email.com --tipo detalhado")

if __name__ == "__main__":
    main()
