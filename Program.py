from UnderTheHood.TreeNode.CreateTree import pottery
from UnderTheHood.ReadWrite.Json import introduce_files
from UnderTheHood.ReadWrite.pillow import show_images

print ("\nWelcome to the pottery recomendation program. ")
print ("This will eventually help you make custom orders too.")
print ("I'll ask a few questions.\n")

classselected = pottery.traverse()
while True:
    print ("\n Write 0 to look at pics, 1 to add new pots. ")
    lookoradd = input ()
    if lookoradd == "0":
        show_images (classselected)
        break
    elif lookoradd == "1":
        introduce_files(classselected)
        break

print("Thanks for visiting!")



