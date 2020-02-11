#-include .env

PROJECT_NAME := $(shell basename "$(PWD)")

PROJ_BASE := $(shell pwd -LP)

## init: Simple initialization.
init:
	@echo "  > Simple initialization"
	@-$(MAKE) create-venv install-dependency

## create-venv: Creating virtual environment
create-venv:
	@echo "  > Creating virtual environment"
	@python3 -m venv venv

## update-requirements: Freezing pip dependency
update-requirements:
	@echo " > Updating requirements"
	@pip freeze > requirements.txt

## install-dependency: Install pip dependency
install-dependency:
	@echo "  > Install dependency"
	@pip install -r requirements.txt

## run: start magic
run:
	python -m wilcoxon_signed_rank_test --data_path="./data/Python Exam (1).xlsx" --out_path="./data/out.csv" --key_product_idx=1

.PHONY: help
all: help
help: Makefile
	@echo
	@echo " Choose a command run in "$(PROJECT_NAME)":"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo