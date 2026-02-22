# Makefile para Projeto Churn - Automação MLOps

# Variáveis
DOCKER_COMPOSE = docker-compose

# Cores para o terminal (Deixa a saída profissional)
GREEN = \033[0;32m
NC = \033[0m # No Color

help: ## Mostra os comandos disponíveis
	@echo "$(GREEN)Comandos Disponíveis para o Projeto Churn:$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

up: ## Sobe os containers (MySQL + App) em modo detach
	@echo "$(GREEN)Subindo o ambiente...$(NC)"
	$(DOCKER_COMPOSE) up -d --build

down: ## Para e remove os containers
	@echo "$(GREEN)Derrubando o ambiente...$(NC)"
	$(DOCKER_COMPOSE) down

logs: ## Mostra os logs dos containers em tempo real
	$(DOCKER_COMPOSE) logs -f

db-shell: ## Entra no terminal do MySQL dentro do container
	@echo "$(GREEN)Acessando MySQL... (Use a senha configurada)$(NC)"
	$(DOCKER_COMPOSE) exec db_empresa mysql -u root -p

clean: ## Limpa containers parados e imagens não utilizadas (Manutenção)
	docker system prune -f

test-db: ## Testa a conexão do Python com o MySQL (db_empresa)
	@echo "$(GREEN)Testando conexão com o banco de dados...$(NC)"
	$(DOCKER_COMPOSE) exec app python test_db.py
