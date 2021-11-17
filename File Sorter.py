import os,shutil

s=os.chdir("Downloads")
current = os.getcwd()

files=os.listdir(current)

images=[".jpeg",".png",".jpg",".gif"]
text=[".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf"]
videos=[".mp4",".mkv"]
sounds=[".mp3",".wav",".m4a"]
applications=[".exe",".lnk"]
codes = [".c",".py",".java",".cpp",".js",".html",".css",".php"]

print("Sorting the files...")

for file in files:
    dest = ""
    for ex in images:
        if file.endswith(ex):
            dest='../Images'
            shutil.move(file,dest)
            break

    for ex in text:
        if file.endswith(ex):
            dest='../Text'
            shutil.move(file,dest)
            break

    for ex in sounds:
        if file.endswith(ex):
            dest='../Sounds'
            shutil.move(file,dest)
            break

    for ex in videos:
        if file.endswith(ex):
            dest='../Videos'
            shutil.move(file,dest)
            break

    for ex in applications:
        if file.endswith(ex):
            dest= '../Applications'
            shutil.move(file,dest)
            break

    for ex in codes:
        if file.endswith(ex):
            dest= '../Codes'
            shutil.move(file,dest)
            break

    if dest == "":
        shutil.move(file,'../Others')

print("Sorting Completed...")