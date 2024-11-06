import json
import glob

rootp = "UnderTheHood/Images/"

def introduce_files(Classvar):
    "introduce filrd to the data.jason"

    jsonexists = glob.glob ("data.json")

    if jsonexists == []:
        jsondict = {}
    else:
        with open("data.json", "r") as json_file:
            jsondict = json.load(json_file)

    while True:
        print ("What's the name of the piece?")
        name = input()
        namesearch = name[:3] +"*.jpg"
        globsearch = rootp + Classvar.class_path + namesearch
        imagelist = []
        imagelist = glob.glob(globsearch)
        if Classvar.cat_name not in jsondict:
            jsondict[Classvar.cat_name] = {}
        
        if imagelist != []:
            jsondict[Classvar.cat_name][name] = imagelist

        inputvar = input("press enter for another piece: ")
        if inputvar == "":
            continue
        else:
            break

    if "" in jsondict[Classvar.cat_name]:
        del jsondict[Classvar.cat_name][""]
    with open('data.json', 'w') as json_file:
        json.dump(jsondict, json_file)
