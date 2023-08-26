**Step1**: create your project with notebook files and .md files and put them in some folder say "source". Now run this command 
```
sphinx-quickstart
```
This will ask you some of the arguments provided them concisely, this will create a **Makefile** in your working directory, and a **conf.py** will be created in your source folder(Please mind you are in one directory above source)

**Step 2:** You’ll have to make a few changes to the file named conf.py. You should make sure that the extensions setting at least contains 'nbsphinx' eg
```
extensions = [
    'nbsphinx',
]
```

**Step 2a** Change the build folder to ***docs*** in Makefile as well as make.bat, please mind the default folder is _build. 

**Step 2b** Make these changes to conf.py to use the particular theme and increase width of the frame

```shell
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
nbsphinx_allow_errors = True
html_theme_options = {
  'content_fixed': True,
  'content_width': '1200px',
}
```
**Step 2c** **Add a file with the name ".nojekyll"** without any content in the docs folder to stop using Jekyll.



**Step 3**: Once your conf.py is in place, edit the file named source/index.rst and add the file names of your notebooks (without the .ipynb extension) to the toctree directive. For example, 
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
(run this step after every change)
```
make html
```
this will create a folder wiht your website. You can run this website on your local machine.

**Step3a** the docs folder containt doctree and html, not index.html, hence create a index.html wiht 
```
<meta http-equiv="refresh" content="0; url=./html/index.html" />
```
This links index.html to ./html/index.html


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


**To server locally** 
give path from where to sever site
```
#first install dependencies in requrirement.txt
pip install -r requirement.txt
#
#**Now install http-server using**
npm install --global http-server
#
http-server -o ./build/html/
```


**Apperantly only a particlar version of jupyter notebook support simple copy pasting in different tab with ctrl+c/v: pip install notebook==5.1.0rc2**
