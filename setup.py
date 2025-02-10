from setuptools import setup, find_packages

setup(
    name="dbt_shared_macros",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],  # No dependencies required for dbt macros
    include_package_data=True,
    description="Shared dbt macros for multiple projects",
)
