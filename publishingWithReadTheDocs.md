**Step1**: create your project with notebook files and .md files and put them in some folder say "source". Now run this command 
```
sphinx-quickstart
```
This will ask you some of arguments provied them concisely, this will create a **Makefile** in your working directory, and a **conf.py** will be created in your source folder(Please mind you are in one directory above source)

**Step2:** You’ll have to make a few changes to the file named conf.py. You should make sure that the extensions setting at least contains 'nbsphinx' eg
```
extensions = [
    'nbsphinx',
]
```


**Step3**: Once your conf.py is in place, edit the file named source/index.rst and add the file names of your notebooks (without the .ipynb extension) to the toctree directive. For an example, 
```shell

Welcome to Cosmology MSc course's documentation!
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Preface
   Introduction
   Cosmological_principle
   FRW_models
   Early_Universe
   Inhomogeneous_Universe

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```
Here source directory contains files wiht names "Cosmological_principle.ipynb,  Early_Universe.ipynb,  FRW_models.ipynb , Inhomogeneous_Universe.ipynb,  Introduction.ipynb,  Preface.ipynb"

**Step3:** make with html
```
make html
```
this will create a folder wiht your website. You can run this website on your local machine.

**Step4:** To publish on ReadTheDocs *make a file requirement.txt* with the following content and **specify** its location (ie ./requirement.txt) in advanced
tab under 'Admin' menu after importing your project in ReadTheDocs
```
sphinx>=1.4
ipykernel
nbsphinx
```
**Step5** Change the default theme
(make appropriate change in conf.py in theme section)
```
 pip install sphinx_rtd_theme

```

