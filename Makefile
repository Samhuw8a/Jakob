run: Jakobsstab.py
	python3 Jakobsstab.py
compile:
	python3 setup.py build
	cp -r config ./build/exe.win-amd64-3.9/
	cp -r Icons ./build/exe.win-amd64-3.9/
	ln build/exe.linux-x86_64-3.8/Jakobsstab

clean:
	rm -rf build/
