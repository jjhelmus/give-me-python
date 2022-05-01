give-me-python
==============

CPython that can be installed via pip.

This packages the CPython interpreters from the manylinux2014 image into Python wheels.
These wheels can be installed using pip.  A gm-python3.X console script will be installed which can
be used to run the installed interpreter.


To build wheels
---------------

Start a manylinux2014 docker container:
```
docker run -it --rm -v `pwd`:/io quay.io/pypa/manylinux2014_x86_64
```

Inside the container run the following commands each subdirectory:
```
/opt/python/cp310-cp310/bin/python setup.py bdist_wheel
auditwheel repair dist/<whl.whl>
```
