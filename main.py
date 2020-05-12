import os
def crateifnotexists(folder):
    if not os.path.exists(folder):
        print(f"creating {folder}")
        os.makedirs(folder)
    else :
        print(f"{folder} already created")

def move(foldername, files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")

files=os.listdir()
files.remove("main.py")
print(files)
crateifnotexists('images')
crateifnotexists('docs')
crateifnotexists('media')
crateifnotexists('others')

imgext=[".png",".jpg","jpeg",".gif"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imgext]

docext=[".txt",".pdf",".docx",".doc"]
docs=[file for file in files if os.path.splitext(file)[1].lower() in docext]

mediaext=[".mp3",".mp4",".mp5"]
medias=[file for file in files if os.path.splitext(file)[1].lower in mediaext]

#print(images)
#print(docs)
#print(medias)
other=[]
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if(ext not in mediaext) and(ext not in docext) and(ext not in imgext) and os.path.isfile(file):
        other.append(file)

print(other)
move("images",images)
move("docs",docs)
move("media",medias)
move("others",other)
