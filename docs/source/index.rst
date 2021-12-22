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
   * A directory of downloaded spectra
   * A list of valid SDSS URLs
   * An astropy table containing valid PLATE, MJD and FIBERIDs
   * A list of ra and dec positions in degrees
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

   DownloadHandler
   Composites
   Plotting



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
