
check_readme:
	# requires readme_renderer
	python3 setup.py check --restructuredtext --strict


readme.html: readme.rst
	rst2html.py readme.rst > readme.html
	refresh.sh Renamer


publish: test
	rm -rf build  # possible wheel bug
	python3 setup.py sdist bdist_wheel --universal upload

	pip3 install --user -e .  # fix bug on next invocation

clean:
	git gc
	rm -f readme.html
	rm -rf .pytest_cache build dist
	rm -rf test/results

	-find -type d -name __pycache__ -exec rm -rf '{}' \;

test: check_readme
	pyflakes **.py ./prn

	cd test; \
	rm -rf results; \
	cp -R original results; \
	\
	cd results; \
	prn -r foo1 @   -z 4   -r @ foo1   -e   *.tif; \
	prn -a _baz   --match foo_bar.txt   -e; \
	prn --append-ext txt   --match no_ext_file   -e; \
	prn -c -R --re-sub '\s+' ' ' -e; \
	prn --lower-ext   --execute   *.Sh; \
	\
	cd ..; \
	diff results expected


# all targets for now
.PHONY: $(MAKECMDGOALS)
