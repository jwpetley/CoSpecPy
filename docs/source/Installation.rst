Install Instructions
=====================

Requires a Python version later than 3.6.

Install using ``pip`` available through:

``pip install CoSpecPy``

Or alternatively you can clone this GitHub repository, navigate to the directory you have just cloned and run:

``python setup.py install``

======================
Download Dependencies
======================

The ``DownloadHandler`` requires use of either ``wget`` or ``aria2`` to download from the SDSS servers.

``wget`` is GNU Wget, a free software package for retrieving files using HTTP, HTTPS, FTP and FTPS. Information and documentation can be found here https://www.gnu.org/software/wget/. For a quick Debian/Ubuntu install try:

``sudo apt-get install wget``

``aria2`` is a lightweight multi-protocol & multi-source command-line download utility and can be far faster than ``wget`` when used with this package. Information and documentation can be found here https://aria2.github.io/. For a quick Debian/Ubuntu install try:

``sudo apt-get install -y aria2``
