
clean:
	fd pycache -I -x rm -rv {}
	rm -rv build dist htmlpy.egg-info

install:
	python3 setup.py install