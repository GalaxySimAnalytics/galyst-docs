.. Galyst documentation master file, created by
   sphinx-quickstart on Thu Jun 26 13:42:06 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root ``toctree`` directive.

Welcome to the Galyst documentation!
====================================

.. raw:: html

   <div style="border:1px solid #ccc; background:#f9f9f9; padding:8px; border-radius:6px; width:max-content; float:right;">
     <a href="../en/index.html">English</a> |
     <a href="../zh_CN/index.html">简体中文</a>
   </div>

``Galyst``: a Python package for multi-dimensional analysis of galaxy simulations. Built on top of `pynbody <http://pynbody.readthedocs.io>`_ and `tangos <https://tangos.readthedocs.io/>`_.
It uses ``pynbody`` for data processing and analysis, and ``tangos`` for data management. ``Galyst`` provides a complete toolchain for analyzing galaxies in simulations from multiple dimensions.



Installation
============

.. code-block:: bash

   git clone https://github.com/GalaxySimAnalytics/Galyst.git
   cd Galyst
   pip install -e .

.. toctree::
   :maxdepth: 2


   Tutorials <tutorials/tutorials>
   Installation <installation>
   Reference <reference/index>
