from CoSpecPy.composites import Composite
from CoSpecPy.download import DownloadHandler
import pkg_resources
import os
from astropy.io import fits

print("Testing Composite")
test_aria2_download = DownloadHandler("aria2", 5, 10, "test_tmp")
test_aria2_download.clear_up()

example_speclist = os.path.abspath("test_tmp/example_speclist.txt")

example_composite = Composite("example_composite")
example_composite.set_download_handler(test_aria2_download)
example_composite.set_wavelength_grid(w_min = 1000, w_max = 3000, steps = 3000)
example_composite.set_normalisation(norm_low = 2575, norm_high = 2625)
print("Composite Setup Finished")

example_table = fits.open("test_table.fits")
example_table = example_table[1].data

example_composite.composite_from_table(example_table, chunks = 10)
example_composite.plot_composite(None)
