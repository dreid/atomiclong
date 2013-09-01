import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

try:
    from atomiclong import ffi
except ImportError:
    ext_modules=[]
else:
    ext_modules=[ffi.verifier.get_extension()]

with open('README.rst') as r:
    README = r.read()

setup(
    name='atomiclong',
    version='0.1.1',
    author='David Reid',
    author_email='dreid@dreid.org',
    url='https://github.com/dreid/atomiclong',
    description="An AtomicLong type using CFFI.",
    long_description=README,
    license='MIT',
    py_modules=['atomiclong'],
    setup_requires=['cffi'],
    install_requires=['cffi'],
    tests_require=['pytest'],
    ext_modules=ext_modules,
    zip_safe=False,
    cmdclass={"test": PyTest},
)
