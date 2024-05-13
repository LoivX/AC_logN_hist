# Histogram of logN for CIV Systems

This simple Python script for Astrocook generates a histogram of the logN values (for CIV systems only) from FITS files analized via Astrocook.

## Functions

### `create_histogram(data_list)`

This function takes a list of FITS data arrays, merges them into a single table, extracts the CIV systems, and plots a histogram of the logN values.

### `GUI()`

This function creates a simple GUI with a button that allows the user to select a FITS file. When the button is clicked, the `extract_data_from_fits()` function is called.

## Usage

To use this script, run it with Python and use the GUI to select a FITS file. The script will extract the data from the FITS file, merge it with any previously selected data, and update the histogram.

## Dependencies

This script requires the following Python packages:

- numpy
- astropy
- matplotlib
- tkinter

These can be installed with pip:

```bash
pip install numpy astropy matplotlib tkinter
