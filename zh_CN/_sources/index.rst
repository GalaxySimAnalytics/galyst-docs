.. Galyst documentation master file, created by
   sphinx-quickstart on Thu Jun 26 13:42:06 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root ``toctree`` directive.

Welcome to the Galyst documentation!
====================================

.. raw:: html

   <div style="border:1px solid #ccc; background:#f9f9f9; padding:8px; border-radius:6px; width:max-content; margin-bottom:18px;">
     <a href="../en/index.html">English</a> |
     <a href="../zh_CN/index.html">简体中文</a>
   </div>

``Galyst`` is an omni-dimensional analysis toolkit for galaxy simulations.
It is a Python package designed for multi-dimensional (0D, 1D, 2D, 3D) analysis of galaxy numerical simulations.
Built on top of `Pynbody <http://pynbody.readthedocs.io>`_ and `Tangos <https://tangos.readthedocs.io/>`_, ``Galyst`` leverages ``pynbody`` for data processing and analysis, and ``tangos`` for data management. It provides a comprehensive toolchain for analyzing galaxies in simulations across multiple dimensions.

Key features:

- **Efficient data management:** `Tangos <https://tangos.readthedocs.io/>`_ organizes and manages diverse simulation projects, supporting storage and retrieval of analysis results.
- **Broad data compatibility:** `Pynbody <https://pynbody.readthedocs.io/>`_ reads mainstream simulation data formats, enabling in-depth computation and analysis.
- **Collaborative workflows:** Galyst includes a robust user permission management system with built-in row-level security (RLS), allowing flexible user access control and efficient collaboration.
- **Extensible analysis tools:** Galyst integrates easily with external analysis tools, such as radiative transfer (`SKIRT <https://skirt.ugent.be/root/_home.html>`_), dynamical analysis (`AGAMA <https://agama.software/>`_, `galpy <http://galpy.readthedocs.io>`_), 2D image processing (`galfit <https://users.obs.carnegiescience.edu/peng/work/galfit/galfit.html>`_, `imfit <https://imfit.readthedocs.io/en/latest/>`_), and 3D morphology modeling (`gal3d <https://github.com/GalaxySimAnalytics/gal3d>`_), greatly enhancing analytical efficiency and extensibility.



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
