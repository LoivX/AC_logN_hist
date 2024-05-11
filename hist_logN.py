import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt


# Create the GUI window
root = tk.Tk()
root.withdraw()

# Prompt the user to select a .dat file
file_path = filedialog.askopenfilename(filetypes=[("DAT Files", "*.dat")])

# Read the .dat file into a dataframe
df = pd.read_csv(file_path, delimiter=' ', skiprows=1, names=['func', 'series', 'z0', 'z', 'dz', 'logN', 'dlogN', 'b', 'db', 'btur', 'dbtur', 'resol', 'chi2r', 'snr', 'id'])

# Create a table of the dataframe
table = pd.DataFrame(df)
print(table)


# Extract only CIV systems
dfCIV = df.loc[df['series'] == 'CIV']


# Plot histogram of logN
plt.hist(dfCIV['logN'], bins=10)
plt.xlabel('logN')
plt.ylabel('Number of systems')
plt.title('Histogram of logN')
plt.show()
