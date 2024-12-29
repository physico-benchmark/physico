import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="physico",
    author="Shunchi Zhang",
    author_email="shunchizhang.cs@gmail.com",
    description="Tools for PhysiCo Dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/physico-benchmark/physico",
    project_urls={
        "Homepage": "https://physico-benchmark.github.io",
        "Repository": "https://github.com/physico-benchmark/physico",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "setuptools",
    ],
    include_package_data=True,
)
