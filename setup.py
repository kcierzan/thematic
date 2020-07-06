import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="thematic",
    version="0.0.1",
    description="A total environment themer",
    long_description=long_description,
    url="https://gitlab.com/kcierzan/thematic",
    author="Kyle Cierzan",
    license="MIT",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    zip_safe=False,
    install_requires=["Jinja2", "pyyaml", "iterm2", "typer", "neovim-remote"],
    entry_points={
        "console_scripts": ["theme=thematic.theme:main"]
    },
)
