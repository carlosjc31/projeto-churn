import mysql.connector
from faker import Faker
import random
from datetime import datetime, timedelta

# Configurações
fake = Faker('pt_BR')
NUM_CLIENTES = 1000

print("⏳ Conectando ao Banco Docker...")

# Conexão com o Banco Docker
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="user_analista",
        password="senha_analista",
        database="telecom_churn_db"
    )
    cursor = conn.cursor()
    print("✅ Conectado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao conectar. Verifique se o Docker está rodando. Erro: {e}")
    exit()

# 1. Criar Tabelas (DDL) - Simulando o ERP
# Note que normalizamos: Clientes separados de Assinaturas e Uso
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    genero VARCHAR(10),
    data_nascimento DATE,
    cidade VARCHAR(50),
    estado VARCHAR(2)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS assinaturas (
    id_assinatura INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    plano VARCHAR(20), -- Basico, Premium, Familia
    valor_mensal DECIMAL(10,2),
    data_inicio DATE,
    status VARCHAR(10), -- Ativo, Cancelado (Isso é o Churn!)
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS uso_servico (
    id_uso INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    mes_referencia DATE,
    dados_consumidos_gb FLOAT, -- Consumo de internet
    chamadas_suporte INT, -- Quantas vezes ligou reclamando
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
)
""")

print("✅ Tabelas criadas/verificadas.")

# 2. Popular com Dados Fictícios Inteligentes
print("⏳ Gerando dados (isso pode levar alguns segundos)...")

for _ in range(NUM_CLIENTES):
    # --- Dados Demográficos ---
    genero = random.choice(['M', 'F'])
    nome = fake.name_male() if genero == 'M' else fake.name_female()
    nasc = fake.date_of_birth(minimum_age=18, maximum_age=70)
    cidade = fake.city()
    estado = fake.state_abbr()

    cursor.execute("INSERT INTO clientes (nome, genero, data_nascimento, cidade, estado) VALUES (%s, %s, %s, %s, %s)",
                   (nome, genero, nasc, cidade, estado))
    id_cliente = cursor.lastrowid

    # --- Dados de Contrato ---
    # Vamos definir se esse cliente VAI dar Churn ou não (Ground Truth)
    vai_dar_churn = random.random() < 0.25  # 25% de chance de ser Churn

    plano = random.choice(['Basico', 'Premium', 'Familia'])
    valor = {'Basico': 59.90, 'Premium': 99.90, 'Familia': 149.90}[plano]
    inicio = fake.date_between(start_date='-2y', end_date='-6m')

    status = 'Cancelado' if vai_dar_churn else 'Ativo'

    cursor.execute("INSERT INTO assinaturas (id_cliente, plano, valor_mensal, data_inicio, status) VALUES (%s, %s, %s, %s, %s)",
                   (id_cliente, plano, valor, inicio, status))

    # --- Dados de Uso (Onde a IA vai trabalhar) ---
    # Vamos gerar dados dos últimos 6 meses
    for i in range(6):
        mes = datetime.now().replace(day=1) - timedelta(days=30 * i)
        mes_str = mes.strftime("%Y-%m-%d")

        # Lógica de Negócio: Quem vai cancelar, usa menos e reclama mais!
        if vai_dar_churn and i < 2: # Nos últimos 2 meses antes de hoje
            consumo = random.uniform(0, 5) # Consumo cai drasticamente
            suporte = random.randint(2, 8) # Reclama muito
        else:
            consumo = random.uniform(10, 50) # Consumo normal
            suporte = random.randint(0, 1) # Pouca reclamação

        cursor.execute("INSERT INTO uso_servico (id_cliente, mes_referencia, dados_consumidos_gb, chamadas_suporte) VALUES (%s, %s, %s, %s)",
                       (id_cliente, mes_str, consumo, suporte))

conn.commit()
cursor.close()
conn.close()

print(f"🎉 Sucesso! {NUM_CLIENTES} clientes gerados no Banco de Dados.")

