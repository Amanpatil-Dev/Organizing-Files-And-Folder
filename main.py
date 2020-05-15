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

if __name__ =="__main__":
    files=os.listdir()
    files.remove("main.py")
    print(files)
    crateifnotexists('images')
    crateifnotexists('docs')
    crateifnotexists('media')
    crateifnotexists('others')
    crateifnotexists('zips')

    imgext=[".png",".jpg","jpeg",".gif"]
    images=[file for file in files if os.path.splitext(file)[1].lower() in imgext]

    docext=[".txt",".pdf",".docx",".doc",".xlsx",".csv"]
    docs=[file for file in files if os.path.splitext(file)[1].lower() in docext]

    mediaext=[".mp3",".mp4",".mp5"]
    medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaext]

    zipext=[".zip",".exe",".rar"]
    zipp=[file for file in files if os.path.splitext(file)[1].lower() in zipext]


    #print(images)
    #print(docs)
    #print(medias)
    print(zipp)

    other=[]
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if(ext not in mediaext) and(ext not in docext) and (ext not in imgext) and (ext not in zipext)  and os.path.isfile(file):
            other.append(file)

    print(other)
    move("images",images)
    move("docs",docs)
    move("media",medias)
    move("others",other)
    move("zips",zipp)
