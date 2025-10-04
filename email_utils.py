import smtplib
import os
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional

# Configura logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def enviar_email(
    destinatario: str,
    assunto: str,
    corpo: str,
    remetente: Optional[str] = None,
    senha: Optional[str] = None
) -> bool:
    """
    Envia um e-mail com versão texto simples e HTML.
    
    Tenta pegar remetente e senha das variáveis de ambiente se não fornecidos.
    Retorna True se o e-mail foi enviado com sucesso, False caso contrário.
    """
    # Credenciais
    if remetente is None:
        remetente = os.getenv('EMAIL_USER')
    if senha is None:
        senha = os.getenv('EMAIL_PASSWORD')
    
    if not remetente or not senha:
        logging.error("Credenciais de e-mail não fornecidas.")
        return False
    
    # Criação da mensagem
    msg = MIMEMultipart('alternative')
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario
    
    # Texto simples
    part_texto = MIMEText(corpo, 'plain', 'utf-8')
    
    # HTML com bullets
    linhas = [linha.strip() for linha in corpo.split('\n') if linha.strip()]
    corpo_html = "<ul>" + "".join(f"<li>{linha}</li>" for linha in linhas) + "</ul>"
    part_html = MIMEText(f"""
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd;">
          <h2 style="color: #333; text-align: center;">{assunto}</h2>
          <div style="background: #f9f9f9; padding: 15px; border-radius: 5px;">
            {corpo_html}
          </div>
          <p style="text-align: center; color: #666; margin-top: 20px;">
            Relatório gerado automaticamente • Sistema de Automação
          </p>
        </div>
      </body>
    </html>
    """, 'html', 'utf-8')
    
    msg.attach(part_texto)
    msg.attach(part_html)
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(remetente, senha)
            smtp.send_message(msg)
        logging.info(f"E-mail enviado com sucesso para {destinatario}!")
        return True
    
    except smtplib.SMTPAuthenticationError:
        logging.error("Erro de autenticação: Verifique usuário e senha.")
    except smtplib.SMTPException as e:
        logging.error(f"Erro SMTP: {e}")
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
    
    return False

def enviar_relatorio(
    destinatario: str,
    caminho_csv: str,
    tipo_relatorio: str = 'simples',
    remetente: Optional[str] = None,
    senha: Optional[str] = None
) -> bool:
    """
    Envia um relatório completo baseado em CSV.
    
    Args:
        destinatario: e-mail do destinatário
        caminho_csv: caminho do arquivo CSV
        tipo_relatorio: 'simples' ou 'detalhado'
        remetente: e-mail remetente (opcional)
        senha: senha do e-mail (opcional)
    """
    from report_utils import gerar_resumo, gerar_resumo_detalhado
    
    if tipo_relatorio == 'detalhado':
        corpo = gerar_resumo_detalhado(caminho_csv)
        assunto = "Relatório Detalhado de Vendas"
    else:
        corpo = gerar_resumo(caminho_csv)
        assunto = "Relatório de Vendas Diário"
    
    return enviar_email(destinatario, assunto, corpo, remetente=remetente, senha=senha)
