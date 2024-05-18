# Astrocook column density analyzer

## Description

The program is designed to analyze FITS files produced by the 'Astrocook' software. This tool allows you to extract data from FITS files, create histograms of logN values for selected systems, and identify the knee of the number of systems over the logN curve.

## Features

- **Data Extraction**: Loading and parsing of FITS files.
- **Error Handling**: Display error windows for warnings and issues.
- **System Analysis**: Extracting specific system data from the dataset, fitting data with a linear fit, and calculating the logN value corresponding to the knee.
- **Graph Creation**: Generating histograms of logN values selected systems and displaying the fitted line.

## System Requirements

- Python 3.7 or higher
- Python libraries:
  - numpy
  - astropy
  - matplotlib
  - tkinter

These can be installed with pip:

```bash
pip install numpy astropy matplotlib tkinter


