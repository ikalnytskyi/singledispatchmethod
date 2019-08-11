"""Backport of @functools.singledispatchmethod to Python 2.7-3.7."""

import os
import io
import setuptools


here = os.path.dirname(__file__)

with io.open(os.path.join(here, "README.rst"), "r", encoding="UTF-8") as f:
    long_description = f.read()


setuptools.setup(
    name="singledispatchmethod",
    description=__doc__,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/ikalnytskyi/singledispatchmethod",
    license="MIT",
    author="Ihor Kalnytskyi",
    author_email="ihor@kalnytskyi.com",
    py_modules=["singledispatchmethod"],
    package_dir={"": "src"},
    use_scm_version={"root": here},
    setup_requires=["setuptools_scm"],
    install_requires=['singledispatch; python_version < "3.4"'],
    project_urls={
        "Documentation": (
            "https://docs.python.org/3.8/library/functools.html"
            "#functools.singledispatchmethod"
        ),
        "Source": "https://github.com/ikalnytskyi/singledispatchmethod",
        "Bugs": "https://github.com/ikalnytskyi/singledispatchmethod/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
    ],
)
