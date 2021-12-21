from .download import DownloadHandler
from .composite_helpers import *

import scipy.interpolate as interp
import numpy as np
from astropy.io import fits


from glob import glob

import pkg_resources

class Composite:
    '''Composite Class to handle creation of composites'''

    def __init__(self, name):
        self.name = name
        self.fluxes = []

    def reset_composite(self):
        '''Reset the flux list to an empty list'''
        self.fluxes = []

    def get_fluxes(self):
        ''' Return the current flux list'''
        return self.fluxes

    def set_download_handler(self, handler):
        ''' Set the download handler for in-built fetching of spectra'''
        if isinstance(handler, DownloadHandler):
            self.download_handler = handler
        else:
            raise Exception("Handler must be valid DownloadHandler")

    def set_wavelength_grid(self, w_min, w_max, steps):
        ''' Add the common wavelength grid which we will place
            spectra in '''
        self.w_min = w_min
        self.w_max = w_max
        self.wavelength_grid = np.linspace(w_min, w_max, steps)

    def set_normalisation(self, norm_low, norm_high):
        '''Add upper and lower normalisation values'''
        self.norm_low = norm_low
        self.norm_high = norm_high


    def composite_from_downloads(self, download_folder):
        '''Create composite from a directory of downloaded spectra'''

        file_list = glob(download_folder+"/*.fits")
        output_fluxes = [] #Initalise empty list for fluxes

        composite_run(file_list, self.wavelength_grid,
                        output_fluxes, self.norm_low, self.norm_high)
        self.fluxes.append(output_fluxes) #Add to the current flux list


    def save_composite(self, filename):
        '''Save current set of fluxes to .npy file'''
        write_output(filename, self.fluxes)



    def composite_from_speclist(self, speclist, chunks = 1):
        '''From a valid speclist.txt file, download all spectra and create a composite'''
        if chunks == 1:
            self.download_handler.download_spectra(speclist)
            self.composite_from_downloads(self.download_handler.download_folder)


        elif chunks > 1:
            splitfile(speclist, chunks)
            glob_speclist = glob(os.path.dirname(speclist) +"/*[0-9]**.txt")
            print(glob_speclist)
            for file in glob_speclist:
                self.download_handler.download_spectra(file)
                self.composite_from_downloads(self.download_handler.download_folder)
                self.download_handler.clear_up()

        else:
            raise Exception("Chunks must be an integer defining the number of" +
                                " files to split the speclist into.")


    def composite_from_table(self, table, chunks = 1):
        '''Create a composite from an Astropy table, produces speclist files as an intermediary'''
        create_speclist(table, self.download_handler.download_folder) #Use helper function to create speclist
        print(self.download_handler.download_folder+"/speclist.txt")
        self.composite_from_speclist(self.download_handler.download_folder+"/speclist.txt", chunks)



    def plot_composite(self, output_figure):
        '''Simple plot of the current composite'''

        import matplotlib.pyplot as plt

        flat_fluxes = np.array([item for sublist in self.fluxes for item in sublist]) #Flatten it all
        print(flat_fluxes)

        median_flux, std_flux = boostrap_fluxes(flat_fluxes, 500)
        plot_flux = median_flux*3e8/self.wavelength_grid
        difference = std_flux*3e8/self.wavelength_grid


        plt.figure(figsize = (12, 7))
        plt.plot(self.wavelength_grid, plot_flux, linewidth = 0.5)
        plt.fill_between(self.wavelength_grid, plot_flux-difference,
                            plot_flux+difference, alpha = 0.5)
        plt.xlabel(r"$\lambda$ [Å]", fontsize = 'xx-large')
        plt.ylabel(r"$F \nu$", fontsize = 'xx-large')
        plt.yscale('log')
        plt.xlim(self.w_min, self.w_max)
        plt.title("Composite: %s"%self.name)

        if output_figure == None:
            plt.show()
        elif len(output_figure)>0:
            plt.savefig(output_figure)
        else:
            plt.show()

    def example_from_downloads(self, download_folder):
        '''Full example run using the already downloaded list'''
        self.set_wavelength_grid(1000, 3000, 2500)
        self.set_normalisation(2575, 2625)
        self.composite_from_downloads(download_folder)
        self.plot_composite()
