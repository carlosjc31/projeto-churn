# 🚀 Previsão de Churn (Telecom) | Arquitetura MLOps na Azure

Este projeto é uma aplicação de Machine Learning de ponta a ponta que prevê o cancelamento de clientes (Churn) de uma empresa de Telecomunicações. Além da construção do modelo preditivo, o foco principal é a **arquitetura de implantação (Deploy)** na nuvem usando as melhores práticas de MLOps, DevOps e FinOps.

## 🏗️ Arquitetura e Tecnologias

A aplicação foi conteinerizada e implantada em uma infraestrutura de nuvem pública (Microsoft Azure), com automação de custos integrada.

* **Front-end / App:** Streamlit (Python)
* **Modelagem de Dados:** Scikit-Learn, Pandas
* **Banco de Dados:** Azure Database for MySQL (Flexible Server)
* **Conteinerização:** Docker & Docker Compose
* **Registro de Imagens:** Azure Container Registry (ACR)
* **Hospedagem:** Azure App Service
* **CI/CD & FinOps:** GitHub Actions

## ⚙️ Destaques de Engenharia

1. **Separação de Ambientes:** O código fonte foi desacoplado das credenciais utilizando Variáveis de Ambiente (`os.getenv`), garantindo segurança na transição do ambiente local para a nuvem.
2. **Banco de Dados Gerenciado (PaaS):** Migração do banco de dados local em Docker para uma instância do Azure MySQL em uma região de baixo custo.
3. **Segurança de Rede:** Configuração de regras de Firewall na Azure para permitir a injeção remota de dados de forma controlada.
4. **FinOps Automatizado:** Implementação de rotinas (Cron Jobs) via **GitHub Actions** que pausam e iniciam automaticamente os recursos da Azure (Banco de Dados e App Service) fora do horário comercial, otimizando o consumo de créditos da nuvem.

## 💻 Como rodar localmente

Para testar o projeto na sua máquina usando o Docker:

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)

## 📷 Screenshots
<img width="744" height="882" alt="image" src="https://github.com/user-attachments/assets/6f52445d-37e3-41b5-9c41-ee3608e30f2a" />



