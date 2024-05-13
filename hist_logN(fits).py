import numpy as np
import astropy as ap
from astropy.io import fits
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from astropy.table import Table


# Initialize an empty list to store the extracted data
data_list = []

''' FUNCTIONS '''
# Extract data from .fits file
def extract_data_from_fits():
    file_paths = filedialog.askopenfilenames(filetypes=[("FITS Files", "*.fits")])
    
    for file_path in file_paths:
        print('file selected successfully: ', file_path)
        with fits.open(file_path) as hdul:
            # Extract the table
            table = hdul[1]
            
            # Append the table to the list
            data_list.append(table.data)

# Merge the data collected and creates a histogram of logN for CIV systems
def create_histogram(data_list):
    # Merge the data and create the final table
    data = np.concatenate(data_list)
    table = Table(data)
    
    # Extract CIV systems
    data_CIV = table[table['series'] == 'CIV']    

    # Plot histogram of logN
    plt.hist(data_CIV['logN'], bins=25)
    plt.xlabel('logN')
    plt.ylabel('Number of systems')
    plt.title('Histogram of logN')
    plt.show()

# Create the GUI window
def GUI():
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
