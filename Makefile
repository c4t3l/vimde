dist: 
	python -m build

clean:
	rm -rf dist

install:
	pip install --force-reinstall dist/vimde*.whl
