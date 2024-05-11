import numpy as np
import astropy as ap
from astropy.io import fits
import matplotlib.pyplot as plt
import tarfile
import tkinter as tk
from tkinter import filedialog


# Initialize an empty list to store the extracted data
data_list = []

''' FUNCTIONS '''
# Extract data from .fits file and append to data list
def extract_data_from_fits():
    file_path = filedialog.askopenfilename(filetypes=[("FITS Files", "*.fits")])
    print('file selected succesfully: ', file_path)
    
    with fits.open(file_path) as hdul:
        # Extract the table
        table_hdu = hdul[1]
        data = table_hdu.data
    
    # Append the extracted data to the data list
    data_list.append(data)
    

# Merges the data collected and creates a histogram of logN for CIV systems
def create_histogram(data_list):
    # Merge the extracted data using vstack
    data = np.vstack(data_list)
    
    # Extract CIV systems
    data_CIV = data[data['series'] == 'CIV']    

    # Plot histogram of logN
    plt.hist(data_CIV['logN'], bins=10)
    plt.xlabel('logN')
    plt.ylabel('Number of systems')
    plt.title('Histogram of logN')
    plt.show()

# Create a GUI window
def GUI():
    # Create the GUI window
    root = tk.Tk()

    # Button to select a file and call the extract_data_from_fits function
    button = tk.Button(root, text="Select file", command= lambda : extract_data_from_fits())
    button.pack()

    # Button to create histogram
    button = tk.Button(root, text="Create histogram", command=lambda: create_histogram(data_list))
    button.pack()

    # Run the GUI window
    root.mainloop()



''' MAIN CODE '''
GUI()

