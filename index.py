# Author: Mafee7
# Github: https://github.com/mafee6

#  Copyright Mafee 2022
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#      http://www.apache.org/licenses/LICENSE-2.0

#  Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# Dependencies: pandas, requests, zipfile, sklearn
import requests, zipfile as zip , pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KnnClass
from io import BytesIO
import os, sys
os.system("") # for colored output

pre = "\u001b[38;2;67;113;214m[Asteroidis]\033[0m "
preER = "\u001b[38;2;255;88;116m[Asteroidis]\033[0m "

print(pre + "Welcome Asteroidis!")
print(pre + "- Mafee7\n")

def astrStop (exitCode = None) :
    if(exitCode == 3): print(pre + "Check \"debug.txt\" for error info.")
    print(pre + "Stopping Asteroidis..")
    quit()

def downloadDataset () :
    datasetURL = "https://gitlab.com/mirsakhawathossain/pha-ml/-/raw/master/Dataset/dataset.csv"
    print(pre + "Downloading dataset. You can also download it manually from Kaggle.com")   

    allowDownload = input(pre + "Do you want to Download the Asteroid Dataset from Kaggle.com (400mb +) (y / n): ")

    if(allowDownload.lower() != "y"):
        astrStop()

    try:

        print(pre + "Downloading dataset! (Might take some time..)")
        dataSetZip = requests.get(datasetURL)
        print(pre + "Done downloading dataset!")

        print(pre + "Extracting zip archive..")
        zfile = zip.ZipFile(BytesIO(dataSetZip.content))
        zfile.extractall("./data")
        print(pre + "Extracted zip archive!\n", end = "\n")

    except :
        print(preER + "An Error occured while downloading or extracting the dataset.")
        dbg = open("debug.txt", "w")
        dbg.write(str(sys.exc_info()))
        astrStop(3)

def main () :
    print(pre + "Loading dataset, might be slow..")
    frame = pd.read_csv("./data/dataset.csv", low_memory = False)
    print(pre + "Loaded dataset!")

    showInfo = input(pre + "Do you want some information about the data? (y / n): ")

    if showInfo == "y": 
        print(pre + "Showing information about the data.")
        print(frame.info())

    x = frame[0:100][["diameter"]]
    x = x.dropna()

    y = frame["name"][0:100]
    y = y.dropna()

    knn = KnnClass()
    mod = knn.fit(x, y)

    predictionFrame = pd.DataFrame()
    predictionFrame["diameter"] = [400, 600]

    print(pre + "Starting Prediction!")
    prediction = mod.predict(predictionFrame)
    print(pre + "Prediction Complete!")
    print(pre + prediction[0] + " may cause huge destruction because of its diameter.")

detected = False

try:
    dataset = open("./data/dataset.csv", "r")
    print(pre + "Dataset detected!")
    detected = True
    dataset.close()
except:
    print(pre + "Dataset not detected.")
    downloadDataset()
    main()

if detected :
    main()