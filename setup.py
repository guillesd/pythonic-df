from setuptools import setup, find_packages


requirements = [
    "tabulate==0.8.9"
]
setup_requirements = ["pytest-runner"]
tests_requirements = ["pytest==5.4.1"]
dev_requirements = [
    "pre-commit==2.19.0",
    "flake8==4.0.0",
    "black==22.3.0",
    "bump2version",
] + tests_requirements
extras_requirements = {"dev": dev_requirements}
setup(
    name="pythonic-df",
    version="0.1",
    description="This package exposes a structured data processing library based only on pythonic objects. This is a pet project and it is not intended to be used in a production setting.",
    license="MIT License",
    # Author details
    author="Guillermo Sanchez",
    author_email="guillermosanchez@godatadriven.com",
    packages=find_packages("pythonic_df"),
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=tests_requirements,
    extras_require=extras_requirements,
)