# Configurações dos produtos para monitorar
PRODUTOS = [
    {
        "nome": "Perfume La Vie Est Belle",
        "urls": {
            "sephora": "https://www.sephora.com.br/perfume-la-vie-est-belle-eau-de-parfum-100ml/p/1234567",
            "boticario": "https://www.boticario.com.br/perfume-la-vie-est-belle-eau-de-parfum-100ml/p/1234567",
            "amazon": "https://www.amazon.com.br/Perfume-La-Vie-Est-Belle/dp/B00X47GQOY"
        },
        "preco_alvo": 299.90
    }
]

# Configurações de e-mail
EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "email_from": "yrisferreira94@gmail.com",
    "email_to": "yrisferreira94@gmail.com"
}

# Configurações de IA
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Configurações de arquivos
PASTA_DADOS = "data"
NOME_ARQUIVO_EXCEL = "precos_produtos.xlsx"

# Configurações de scraping
TEMPO_ESPERA = 10  # segundos entre requisições
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" 