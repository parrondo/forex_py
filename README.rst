Status
=========

.. image:: https://travis-ci.org/0h-n0/forex_py.svg?branch=master
   :target: https://travis-ci.org/0h-n0/forex_py

.. image:: https://readthedocs.org/projects/forex-py/badge/?version=latest
   :target: http://forex-py.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/0h-n0/forex_py/badge.svg
   :target: https://coveralls.io/github/0h-n0/forex_py


.. image:: https://codeclimate.com/github/0h-n0/forex_py/badges/gpa.svg
   :target: https://codeclimate.com/github/0h-n0/forex_py
   :alt: Code Climate
         

CONCEPT
----------

Frxpy is just a `test` tool to know whether DeepLearning predict a forex market. So, Frxpy doesn't provide the best prediction for a market. Of course, Frxpy may lead the completely wrong predictions. If you use this for your real trading and lose a lot of money, you have to take `all the responsibility on yourself`.


TODO
----------


* add tensorboard for visulaization.
* add Deeplearning.
            

forex_py
----------

predicting forex.

.. more discription.

Download
-----------

.. code-block::

   git clone https://github.com/0h-n0/forex_py.git
   # or
   wget https://github.com/0h-n0/forex_py/archive/master.zip
   unzip master.zip

Install(build&install)
-----------

build Envrionment
*****************

.. code-block::

   $ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
   
Install frxpy
*****************


.. code-block::

   cd forex_py
   python3 setup.py install

   
Docs
-----------

.. code-block::

   cd forex_py
   cd docs
   make html
   firefox build/html/index.html
   
   
Where do I get data?
--------------------

Histdata provides histrical forex data. The data is available for free.

* http://www.histdata.com/

Examples
---------------------  

Command-line interface
***********************

.. code-block::

   frxpy --input --buy
   
API of python3
***********************

I assume that forex_py is used in python-scripts. So, Python3-APIs of forex_py is more poweful and
frexible than command-line interface.

.. code-block::

   import frxpy
   
Supported Data Base & Serializer
--------------------

In progress...

* sqlite3
* leveldb
* mysql  
* hdf5
* postgresql
* tinydb
* protobuf
  
