#!make
################################################################################
# Makefile internals
################################################################################
.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | sort | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-6s\033[0m %s\n", $$1, $$2}'

################################################################################

clean:  ## Remove all pyc and caches
	@find . -name '*.py[co]' -exec rm -f {} +
	@find . -name '\.pytest_cache' -exec rm -fr {} +
	@find . -name '\.mypy_cache' -exec rm -fr {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name 'dist' -exec rm -fr {} +

format: ## Format the code
	@python3 -m isort  --atomic . && \
	python3 -m black  . && \
	python3 -m autoflake \
		--in-place \
		--remove-unused-variables \
		--remove-all-unused-imports \
		--remove-duplicate-keys \
		--ignore-init-module-imports \
		--recursive . \


lint:  ## Static analysis
	@python3 -m isort -c  --atomic . && \
	python3 -m black --check  . \


build:  ## Builds new version.
	@python3 -m build

publish:  ## Publish latest version.
	python3 -m twine upload $(shell find dist -type f -print | tail -1)  --verbose
