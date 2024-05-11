import numpy as np
import astropy as ap
from astropy.io import fits
import matplotlib.pyplot as plt
import tarfile
import tkinter as tk
from tkinter import filedialog


# Create the GUI window
root = tk.Tk()
root.withdraw()

# Select a .fits file
file_path = filedialog.askopenfilename(filetypes=[(".fits Files", "*.fits")])

with fits.open(file_path) as hdul:
    hdul.info()
    
    # Extract the table
    table_hdu = hdul[1]
    data = table_hdu.data

# Extract CIV systems
data_CIV = data[data['series'] == 'CIV']    

# Plot histogram of logN
plt.hist(data_CIV['logN'], bins=10)
plt.xlabel('logN')
plt.ylabel('Number of systems')
plt.title('Histogram of logN')
plt.show()