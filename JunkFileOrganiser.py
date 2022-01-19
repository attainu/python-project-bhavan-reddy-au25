# Junk File Organizer
# Python Project To Sort Files 


import os, shutil

print("Welcome To Junk File Organizer")
print("Program By - Bhavan")
print("--OPTIONS--")
print("Enter 1 For File Type Sorting")

typeofsort = input("Enter Sorting Method: ")
folderpath = input('Enter Your Folder Path To Sort The Files: ')


# To Sort According To Size

file_extensions={
       'Audio':('.mp3','.wav','.flac', '.m4a', '.aac'),
       'Video':('.mp4','.mkv','.MKV','.flv','.mpeg'),
       'Images':('.jpeg', '.jpg', '.tiff', '.gif', '.png'),
       'Docs':('.doc','.pdf','.txt','.docx','.xls', '.xlsx', '.ppt', '.pptx', '.xps'),
       'Archives':('.zip', '.7z', '.rar'),
       'Others':('.exe', '.apk', '.bat', '.bin'),
       'Programming':('.py', '.htm', '.html', '.html5', '.css', '.php', '.js')
}
new_path={
    "Organized":('Audio','Video','Images','Docs','Archives','Others','Programming')
}

if typeofsort=="1":
    def file_finder(folderpath,file_extensions):
        files=[]
        for file in os.listdir(folderpath):
            for extension in file_extensions:
                if file.endswith(extension):
                    files.append(file)
        return files 

    for extensions_type,extension_tuple in file_extensions.items():
        folder_name=extensions_type.split('_')[0]
        folder_path=os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for item in (file_finder(folderpath,extension_tuple)):
            item_path=os.path.join(folderpath,item)
            item_new_path=os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)

    for extensions_type,extension_tuple in new_path.items():
        folder_name=extensions_type.split('_')[0]
        folder_path=os.path.join(folderpath,folder_name)
        os.mkdir(folder_path)
        for item in (file_finder(folderpath,extension_tuple)):
            item_path=os.path.join(folderpath,item)
            item_new_path=os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)
    print("Done Sorting :)")