from setuptools import setup, Extension

MIN_PYTHON_VERSION = "3.11"
PY_LIMITED_API = "0x030b00f0"

extensions = [
    Extension(
        "adder.add",
        sources=["adder/add.pyx"],
        py_limited_api=True,
        define_macros=[
            ("Py_LIMITED_API", PY_LIMITED_API),
            ("CYTHON_LIMITED_API", "1"),
        ],
    )
]


setup(
    ext_modules=extensions,
    python_requires=f">={MIN_PYTHON_VERSION}",
)
