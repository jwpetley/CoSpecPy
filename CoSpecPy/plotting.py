import matplotlib.pyplot as plt
from .composites import Composite
from .composite_helpers import *


class ComparisonPlot:
    '''Class for Multiple Composites

        This class handles the plotting of one or more composites on a single
        plot

        Attributes:
            composite_list (list[Composite]): Contains all the currently added composites
            w_low (float): Lowest plotting wavelength in Angstrom. Default = 0
            w_high (float): Highest plotting wavelength in Angstrom. Default = 3000
    '''

    def __init__(self, w_low = 0, w_high = 3000):
        self.composite_list = []
        self.w_low = w_low
        self.w_high = w_high

    def set_plotting_wavelength(self, w_low, w_high):
        ''' Set plotting wavelength range

            Args:
                w_low (float): Lowest plotting wavelength in Angstrom
                w_high (float): Highest plotting wavelength in Angstrom
        '''
        self.w_low = w_low
        self.w_high = w_high

    def add_composite(self, composite):
        '''Add a composite to the current composite list

            Args:
                composite (Composite): A valid composite class.
        '''
        self.composite_list.append(composite)

    def plot_all(self):

        plt.figure()

        for composite in self.composite_list:
            median_flux, bootstrap_std = boostrap_fluxes(composite.flux, samples = 500)

            plot_flux = median_flux*3e8/self.wavelength_grid
            difference = bootstrap_std*3e8/self.wavelength_grid

            plt.plot(composite.wavelength_grid, plot_flux, linewidth = 0.5, label = composite.name)
            plt.fill_between(composite.wavelength_grid, plot_flux-difference, plot_flux+difference,
                                    alpha = 0.5)

        plt.xlim(self.w_low, self.w_high)

        plt.xlabel(r"$\lambda$ [Å]", fontsize = 'xx-large')
        plt.ylabel(r"$F \nu$", fontsize = 'xx-large')
        plt.yscale('log')
        plt.show()
