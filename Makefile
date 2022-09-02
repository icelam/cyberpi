.PHONY: create-venv clean-venv install lint

# Init new virtual environment
create-venv:
	pipenv --python 3.9.9

# Remove existing virtual environment
clean-venv:
	pipenv --rm

# Install dependencies
install:
	pipenv install --dev

# Run pylint checking
lint:
	pipenv run pylint $$(find . -type f -name "*.py")

# Prettify README.md
prettify-readme:
	npx prettier README.md **/*/README.md --write
