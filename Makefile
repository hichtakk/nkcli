.DEFAULT_GOAL := help

install: ## install nkcli and dependencies
	@poetry install -vvv

help: ## Makefile
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort