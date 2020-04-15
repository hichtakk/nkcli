.DEFAULT_GOAL := help
POETRY := $(shell which poetry)

install: ## install nkcli and dependencies
	@${POETRY} install -vvv

help: ## Makefile
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort