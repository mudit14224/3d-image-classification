import zipfile
import os

exist = os.path.exists("./MedData")
if not exist:
    os.makedirs("./MedData")

with zipfile.ZipFile("CT-0.zip", "r") as z:
  z.extractall("./MedData/")

with zipfile.ZipFile("CT-23.zip", "r") as z:
  z.extractall("./MedData/")

print("The zip files have been extracted in the MedData Folder!")