.PHONY: workspace

PYTHON_VERSION=3.6

workspace:
	@pipenv install --python $(PYTHON_VERSION) --dev -e .
	@pipenv shell
