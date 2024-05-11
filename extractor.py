import tarfile
import tkinter as tk
from tkinter import filedialog

def extract_files_from_acs(acs_file_path, destination_folder):
    with tarfile.open(acs_file_path, 'r') as tar:
        tar.extractall(destination_folder)

def select_acs_file():
    acs_file_path = filedialog.askopenfilename(filetypes=[("ACS Files", "*.acs")])
    return acs_file_path

def select_destination_folder():
    destination_folder = filedialog.askdirectory()
    return destination_folder

acs_file_path = select_acs_file()
destination_folder = select_destination_folder()

extract_files_from_acs(acs_file_path, destination_folder)