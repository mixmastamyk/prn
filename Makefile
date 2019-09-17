
check_readme:
	# requires readme_renderer
	python3 setup.py check --restructuredtext --strict


readme.html: readme.rst
	rst2html.py readme.rst > readme.html
	refresh.sh Renamer


publish: check_readme
	rm -rf build  # possible wheel bug
	python3 setup.py sdist bdist_wheel --universal upload

	pip3 install --user -e .  # fix bug on next invocation

clean:
	git gc
	rm -f readme.html
	rm -rf .pytest_cache build dist

	-find -type d -name __pycache__ -exec rm -rf '{}' \;

test:
	pyflakes **.py


# all targets for now
.PHONY: $(MAKECMDGOALS)
