
A duckdb kernel for Jupyter. Using SQL for data analysis in  Jupyter with DuckDB.  
在Jupyter中使用SQL和duckdb进行数据分析。

===========================

Prerequisites
-------------
Install `JupyterLab <https://github.com/jupyterlab/jupyterlab-desktop>`_ and the
`duckdb packages for Python <https://github.com/duckdb/duckdb>`_.

Installation
------------

Install using::

    $ pip install duckdb_kernel

or ``pip install git+https://github.com/suyin1203/duckdb_kernel`` for the dev version.

To use the kernel, run one of::


To remove from kernel listings::

    $ jupyter kernelspec remove duckdb


Development
~~~~~~~~~~~

Install the package locally::

    $ pip install -e .
    $ python -m duckdb_kernel install

As you make changes, test them in a notebook (restart the kernel between changes).

