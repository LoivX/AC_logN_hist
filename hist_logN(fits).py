import numpy as np
import astropy as ap
from astropy.io import fits
import matplotlib.pyplot as plt
import tarfile
import tkinter as tk
from tkinter import filedialog
from astropy.table import Table, vstack


# Initialize an empty list to store the extracted data
table_list = []

''' FUNCTIONS '''
# Extract data from .fits file
def extract_data_from_fits():
    file_path = filedialog.askopenfilename(filetypes=[("FITS Files", "*.fits")])
    print('file selected succesfully: ', file_path)
    
    with fits.open(file_path) as hdul:
        # Extract the table
        table = hdul[1]
        # Convert the table to an astropy table
        table = Table(table.data)

        # Append the table to the list
        table_list.append(table)
        print(table_list)

# Merges the data collected and creates a histogram of logN for CIV systems
def create_histogram(table_list):
    # Merge the tables using vstack
    table = np.vstack(table_list)
    
    # Extract CIV systems
    data_CIV = table[table['series'] == 'CIV']    

    # Plot histogram of logN
    plt.hist(data_CIV['logN'], bins=10)
    plt.xlabel('logN')
    plt.ylabel('Number of systems')
    plt.title('Histogram of logN')
    plt.show()

# Create the GUI window
def GUI():
    # Create the GUI window
    root = tk.Tk()

    # Button to select a file and call the extract_data_from_fits function
    button = tk.Button(root, text="Select file", command= lambda : extract_data_from_fits())
    button.pack()

    # Button to create histogram
    button = tk.Button(root, text="Create histogram", command=lambda: create_histogram(table_list))
    button.pack()

    # Run the GUI window
    root.mainloop()



''' MAIN CODE '''
GUI()

''' trova un modo per mergiare i dati estratti da più file .fits'''