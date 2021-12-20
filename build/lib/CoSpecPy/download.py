import numpy as np
import scipy
from subprocess import call
import pkg_resources


class DownloadSpectra:
    ''' Class for handling the downloading of spectra given
    a method and various forms of object lists'''

    def __init__(self, download_method, no_of_connections,
                    batch_size, download_folder):

        if download_method != "aria2" and download_method != "wget":
            raise Exception("Valid Download Method is either 'wget' or 'aria2'")
        self.download_method = download_method
        self.no_of_connections = no_of_connections
        self.batch_size = batch_size
        self.download_folder = download_folder

    def download_spectra(download_file):
        '''Given spectra list containing correctly formatted URLs, download
        using preferred method given in class initiation'''
        if self.download_method == "aria2":
            call(['aria2c', '-c', '--check-certificate=false',
            '-j', self.no_of_connections, '-i', download_file],
            cwd = self.download_folder)

        if self.download_method == "wget":
            call(['wget', '-c', '-i', download_file],
            cwd = self.download_folder)

    def download_example():
        ''' Download the example short spectra list in the data directory '''
        DATA_PATH = pkg_resources.resource_filename(__name__, 'data/speclist.txt')
        download_spectra(DATA_PATH)
        print("Downloaded Succesfully")
