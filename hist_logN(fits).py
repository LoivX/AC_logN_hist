import numpy as np
import astropy as ap
from astropy.io import fits
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from astropy.table import Table


''' FUNCTIONS '''
# Extract data from .fits file
def extract_data_from_fits(data_list=[]):
    file_paths = filedialog.askopenfilenames(filetypes=[("FITS Files", "*.fits")])
    
    for file_path in file_paths:
        print('file selected successfully: ', file_path)
        with fits.open(file_path) as hdul:
            # Extract the table
            table = hdul[1]
            
            # Append the table to the list
            data_list.append(table.data)

def error_window(message):
    # Create the error window
    root = tk.Tk()
    root.title("Error")

    # Display the error message
    error_label = tk.Label(root, text=message)
    error_label.pack()

    # Run the error window
    root.mainloop()

def extract_systems(data_list=[], system_name=''):
    # Merge the data and create the final table
    data = np.concatenate(data_list)
    table = Table(data)

    # Extract systems data
    if system_name == '':
        print('No system name provided')
        error_window('No system name provided')
        return None
    elif system_name not in table['series']:
        print('System name not found')
        error_window('System name not found')
        return None
    else:
        systems_data = table[table['series'] == system_name]
        return systems_data

# Merge the data collected and creates a histogram of logN for systems
def create_plot(data_list, system_name, n_bins=0):
    # Check if data_list is empty
    if len(data_list) == 0:
        print('No data collected')
        error_window('No data collected')
        return None
    
    # Extract the systems
    system_data = extract_systems(data_list, system_name)

    # Extract values from the histogram
    try:
        n_bins = int(n_bins)
    except:
        print('Invalid number of bins: setting to default value')
        n_bins = int(np.sqrt(len(system_data)))
    
    values, bins = np.histogram(system_data['logN'], bins=n_bins)

    # Finding the knee
    k = np.argmax(np.diff(values)) + 1

    # Convert values in log scale
    values[values == 0] = 1
    values = np.log10(values)

    # Fit a linear function to the histogram
    m, q = np.polyfit(bins[:-1][values != 0][k:], values[values != 0][k:], 1)

    print(f'\n Slope: {m:.3g}', f'\n Intercept: {q:.4g}', f'\n Knee: {bins[k]:.4g} ± {np.diff(bins)[k]/2:.1g}')

    # Create the plot
    x = np.linspace(11, 15, 100)
    y = m*x + q

    plt.plot(x, y, color='green', linestyle='--')
    plt.bar(bins[:-1], values, width=np.diff(bins))
    plt.xlim(11, 15)
    plt.ylim(0, 1.5)
    plt.xlabel('logN')
    plt.ylabel('Number of systems in log scale')
    plt.title('Histogram of logN')
    plt.show()

    


''' MAIN CODE '''
def main():
    data_list = []

    # Create the GUI window
    root = tk.Tk()

    # Button to select a file and call the extract_data_from_fits function
    button = tk.Button(root, text="Select file", command = lambda : extract_data_from_fits(data_list))
    button.pack()

    # Entry for system name
    system_label = tk.Label(root, text="Name of the system:")
    system_label.pack()

    system_entry = tk.Entry(root)
    system_entry.pack()

    # Entry for number of bins
    bins_label = tk.Label(root, text="Number of bins:")
    bins_label.pack()

    bins_entry = tk.Entry(root)
    bins_entry.pack()

    # Button to create histogram
    button = tk.Button(root, text="Create histogram", command= lambda: create_plot(data_list, system_entry.get(), bins_entry.get()))
    button.pack()

    # Run the GUI window
    root.mainloop()
main()