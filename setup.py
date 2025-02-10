from setuptools import setup, find_packages


setup(
    name="dbt_shared_macros_pkg",  # The name of your package
    version="1.0.0",           # Package version
    packages=find_packages(),  # This will find all sub-packages in dbt_shared_macros/
    install_requires=[],       # If you have any dependencies, list them here
    include_package_data=True, # This will include the macros (SQL files) in the package
    package_data={             # Ensure SQL files are included in the package
        "dbt_shared_macros_pkg": ["macros/*.sql"],
    },
    description="Shared dbt macros for multiple projects",  # Brief description of the package
)
