=======
goldbar
=======

Embedded language for defining and working with genetic design spaces.

.. image:: https://badge.fury.io/py/goldbar.svg
   :target: https://badge.fury.io/py/goldbar
   :alt: PyPI version and link.

Purpose
-------
GOLDBAR is a syntax and language for describing genetic design spaces. GOLDBAR is being developed at `CIDAR <http://cidarlab.org/>`_, and other tools for working with genetic design spaces using GOLDBAR are currently being developed. These tools include `Knox <https://github.com/CIDARLAB/knox/>`_ and `Constellation <https://github.com/hicsail/constellation-js>`_.

This embedded domain-specific language for Python has semantics that adhere to those of the GOLDBAR language definition and existing associated tools. It allows users to define genetic design spaces using GOLDBAR operators within Python.

Package Installation and Usage
------------------------------
The package is available on PyPI::

    python -m pip install goldbar

The library can be imported in the usual ways::

    import goldbar
    from goldbar import *
