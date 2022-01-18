run: Jakobsstab.py
	python3 Jakobsstab.py
compile:
	python3 setup.py build
	cp config ./build/exe.win-amd64-3.9/
	cp Icons ./build/exe.win-amd64-3.9/
