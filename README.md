[![Build Status](https://travis-ci.org/naveenkumarmarri/DownloadImagesFromFile.svg?branch=master)](https://travis-ci.org/naveenkumarmarri/DownloadImagesFromFile)

# DownloadImageFromFile

The project is to download all the images from the given URLs mentioned in a text file.

  - url.txt file contains the list of the URLs from where images are to be downloaded
  - download.py is the script to download the images 
  - download.py contains function downloadImages which expects the path and name of the file as input parameters
  - file path format is in unix style

Running instructions

```sh
$ python <sourceDirectory> <fileName>
```

> source_directory is the folder which contains the file in which urls are present

Example

```sh
$ python ~/py url.txt
```

