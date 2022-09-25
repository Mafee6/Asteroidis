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

# Depenancies: pandas, requests, zipfile, sklearn
import requests, zipfile as zip , pandas as pd
from sklearn.neighbors import KNeighborsClassifier as KnnClass
from io import BytesIO, StringIO
import os, json, sys
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
    datasetURL = "https://storage.googleapis.com/kaggle-data-sets/689444/4217054/compressed/dataset.csv.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20220923%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220923T144431Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=17c507972bb6eacb4279fe56f3cacfca7afdaebf98d6e64d31d9d6c3ff9765c24779a618e99f116cbd1256970b82df66379c2ff6dda465ec04b1b88fe95bc9d4482703390cc36ae473bc36760391455f8697a717402868e10fcc91d21b829b9790ec34048911d8ff735d8972227a116714126776eca5f83a55c86fa80296a5cb56ac630c176fbeebbd40ed6d710fecb18f01ef0ca5e9f848da6d29631d113b19f94b6d6afe71391416b1b00cd27ea79628c24bb9b7d8f75e67a5abcc206e133c34b758da4f7bd404c7c66d3327437dc8959bea8d8656fdad0840478ab7a1e61a8689e8e105fb364a83000f94d81530ead34d2f3827078c95fe409800d34dc047"
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