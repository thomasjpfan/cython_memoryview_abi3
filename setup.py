from setuptools import setup, Extension
import sys

if sys.version_info >= (3, 11):
    py_limited_api = True
    define_macros = [
        ("Py_LIMITED_API", "0x030b00f0"),
        ("CYTHON_LIMITED_API", "1"),
    ]
else:
    py_limited_api = False
    define_macros = []


extensions = [
    Extension(
        "adder.add",
        sources=["adder/add.pyx"],
        py_limited_api=py_limited_api,
        define_macros=define_macros,
    )
]


setup(ext_modules=extensions)
