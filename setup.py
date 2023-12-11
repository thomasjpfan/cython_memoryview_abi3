from setuptools import setup, Extension

MIN_PYTHON_VERSION = "3.11"
PY_LIMITED_API = "0x030b00f0"
CPYTHON_TAG = f"cp{MIN_PYTHON_VERSION.replace('.', '')}"

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
    name="adder",
    packages=["adder"],
    ext_modules=extensions,
    python_requires=f">={MIN_PYTHON_VERSION}",
)