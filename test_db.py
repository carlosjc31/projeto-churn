
import pandas as pd
from sqlalchemy import create_engine

# Configuração da conexão corporativa
# IMPORTANTE: O host é o nome do serviço no docker-compose (ex: 'db'), não 'localhost'
db_user = 'root'
db_password = 'sua_senha_aqui' # <--- Coloque a senha do seu MySQL
db_host = 'db'
db_name = 'db_empresa' # <--- O banco que você já tem

print(f"Tentando conectar ao banco '{db_name}' no host '{db_host}'...")

try:
    # Cria o motor de conexão
    engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}:3306/{db_name}')

    # Faz uma query simples para pegar apenas 5 linhas da tabela customers
    query = "SELECT * FROM customers LIMIT 5"
    df = pd.read_sql(query, engine)

    print("\n✅ CONEXÃO BEM SUCEDIDA! Veja os primeiros dados:")
    print("-" * 50)
    print(df.head())
    print("-" * 50)

except Exception as e:
    print("\n❌ ERRO DE CONEXÃO:")
    print(e)
