
readme.html: readme.rst
	rst2html.py readme.rst > readme.html
	refresh.sh Renamer


check_readme:
	# requires readme_renderer
	python3 setup.py check --restructuredtext --strict


publish: check_readme
	rm -rf build  # possible wheel bug
	python3 setup.py sdist bdist_wheel --universal upload

	pip3 install --user -e .  # fix bug on next invocation

clean:
	rm -rf build dist
