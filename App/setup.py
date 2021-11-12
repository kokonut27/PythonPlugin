from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = "PythonPlugin",
  version = "0.0.1",
  description = "Python web framework",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "",
  author = "JBYT27",
  author_email = "",
  license = "MIT License",
  packages=['pythonplugin'],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
)