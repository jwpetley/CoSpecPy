import pytest
from CoSpecPy.download import DownloadSpectra

print("TESTING WGET!")
test_wget_download = DownloadSpectra("wget", 1, 10, "test_tmp")
test_wget_download.clear_up()
test_wget_download.download_example()
test_wget_download.clear_up()
print("CLEARED UP WGET")

print("TESTING ARIA2!")
test_aria2_download = DownloadSpectra("aria2", 5, 10, "test_tmp")
test_aria2_download.clear_up()
test_aria2_download.download_example()
test_aria2_download.clear_up()
print("CLEARED UP ARIA2")
