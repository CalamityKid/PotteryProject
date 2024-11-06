from PIL import Image
import glob
import json


rootp = "UnderTheHood/Images/"

def show_images(Classvar):
    "introduce as filename.json"

    jsonexists = glob.glob ("data.json")
    
    if jsonexists == []:
        jsondict = {}
    else:
        with open("data.json", "r") as json_file:
            jsondict = json.load(json_file)
    
    for key, value in jsondict[Classvar.cat_name].items():
        for imagedir in value:
            Image.open(imagedir).show()
            print ("press any key for next one.")
            input()
    
    print ("That was the last one!")