# Monitor de Preços de Produtos de Beleza

Este projeto é um robô automatizado que monitora preços de produtos de beleza em diferentes sites, compara os valores e gera alertas quando encontra ofertas.

## Funcionalidades

- Monitoramento de preços em múltiplos sites (Sephora, Boticário, Amazon)
- Comparação de preços entre diferentes lojas
- Geração de planilha com resultados
- Alertas por e-mail quando preços estão abaixo do valor definido
- Análise de tendências de preços usando IA

## Configuração

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente:
- Crie um arquivo `.env` baseado no `.env.example`
- Adicione suas credenciais de e-mail e API keys necessárias

3. Configure os produtos para monitorar no arquivo `config.py`

## Uso

Execute o script principal:
```bash
python main.py
```

## Estrutura do Projeto

- `main.py`: Script principal
- `scrapers/`: Módulos para cada site monitorado
- `utils/`: Funções utilitárias
- `config.py`: Configurações do projeto
- `data/`: Diretório para armazenar planilhas geradas 