============
Quick Start
============

We have added an example speclist of 50 SDSS URLs to get you started with composite creation.

Below is also another example of how easy it is to get started with this package using only
RA and Dec coordinates of target objects.
Given a list of ra and dec positions in degrees, this will find the best matches to the SDSS DR14 quasar
catalogue and create a composite to plot.


You must have wget installed:

.. code-block:: python

  from CoSpecPy import DownloadHandler, Composite # Import the Handler

  output_dir = "/path/to/output"

  ra = [] # Input you ra values here
  dec = [] # Input you dec values here

  example_handler = DownloadHandler(download_method = "wget", #Download method (aria2 or wget)
  no_of_connections = 1, batch_size="10", #Connections only apply to aria2, batches not implemented
   download_folder=output_dir) # output folder

  #Example download with wget
  example_handler.download_example()

  #This will download the 50 example spectra in CoSpecPy/data/example_speclist.txt to your chosen output

  example_composite = Composite(name = "example_composite") #Creation of Composite Class
  example_composite.set_wavelength_grid(w_min = 1000, w_max = 3000, steps = 2500) #Add the desired wavelength grid in Angstrom
  example_composite.set_normalisation(norm_low = 2575, norm_high = 2625) #Add desired normalisation range in Angstrom
  example_composite.composite_from_downloads(output_dir) # Will create the composite
  example_composite.plot_composite() # Plots the composite stored in the composite class with bootstrapped uncertainties

  # Now rest and create using the ra and dec list
  example_composite.reset_composite()
  example_composite.composite_from_coords(ra, dec) # Will download SDSS DR14 catalogue if not already present (~750 MB)
  example_composite.plot_composite()

The example download section of the code will produce ths output. Feel free to change parameters

.. image:: _static/example.png

Other features can be explored by looking through the code.
