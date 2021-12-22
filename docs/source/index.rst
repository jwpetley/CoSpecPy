Welcome to CoSpecPy's documentation!
====================================

This is a Python package for creating composite spectra using the latest SDSS
spectra releases. The source code for this project is found at
https://github.com/jwpetley/CoSpecPy.
If you would like to get involved in improving this
project then please contact me at jwpetley@gmail.com.

===========
Feautures
===========

The features currently implemented included:
   * Downloading of spectra from SDSS DR12 and DR14
   * Creation of composites from:
      * A directory of downloaded spectra - :meth:`Composite.composite_from_downloads(dir_name) <CoSpecPy.composites.Composite.composite_from_downloads>`
      * A list of valid SDSS URLs - - :meth:`Composite.composite_from_speclist(speclist) <CoSpecPy.composites.Composite.composite_from_speclist>`
      * An astropy table containing valid PLATE, MJD and FIBERIDs - - :meth:`Composite.composite_from_table(astropy.Table) <CoSpecPy.composites.Composite.composite_from_table>`
      * A list of ra and dec positions in degrees - :meth:`Composite.composite_from_coords(ra, dec) <CoSpecPy.composites.Composite.composite_from_coords>`
      * Plotting of stored spectra

In the future I will add more features including:
   * More valid inputs for composite creation
   * Fitting of composites
   * Inclusion of other sources than SDSS

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Installation
   getting_started

===================
Full Documentation
===================

.. toctree::
   DownloadHandler
   Composites
   Plotting



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
