# Build

To build package the from source, use:

```sh
make clean && make build
```

To push to PyPi, install the package `twine` and use:

```sh
make install
```

You may wish to push to the test PyPi instance first:

```sh
python -m twine upload --repository testpypi dist/*
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps witaker-clipboard-server
```
