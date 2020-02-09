from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import os
import json
import shutil

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i=0
            if filename!='Applications' or 'Files' or 'compressed_files' or 'images' or 'pictures' or 'others':
                new_name=filename
                extension='noname'
                try:
                    extension=str(os.path.splitext(folder_to_track + "\\" + new_name)[1])
                    opath=extension_types[extension]
                except Exception:
                    extension='noname'
                folder_destination_path=extension_types[extension]
                file_exists=os.path.isfile(folder_destination_path + "\\" + new_name)
                while file_exists:
                    i+=1
                    new_name=os.path.splitext(folder_to_track + '\\' + new_name)[0] + str(i) + os.path.splitext(folder_to_track+'\\'+new_name)[1]
                    new_name=new_name.split("\\")[4]
                    file_exists=os.path.isfile(folder_destination_path + "\\" + new_name)
                src=folder_to_track+"\\"+filename
                destination = folder_destination_path+"\\"+new_name
                os.rename(src, destination)



extension_types={
'.txt' :"C:\\Users\\Lakkireddy\\Downloads1\\Files",
'.doc':"C:\\Users\\Lakkireddy\\Downloads1\\Files",
'.docx':"C:\\Users\\Lakkireddy\\Downloads1\\Files",
'.wps':"C:\\Users\\Lakkireddy\\Downloads1\\Files",
'.wpd':"C:\\Users\\Lakkireddy\\Downloads1\\Files",

'.gif':"C:\\Users\\Lakkireddy\\Downloads1\\pictures",
'.ico':"C:\\Users\\Lakkireddy\\Downloads1\\pictures",
'.jpg':"C:\\Users\\Lakkireddy\\Downloads1\\pictures",
'.jpeg':"C:\\Users\\Lakkireddy\\Downloads1\\pictures",
'.png':"C:\\Users\\Lakkireddy\\Downloads1\\pictures",

'.exe':"C:\\Users\\Lakkireddy\\Downloads1\\Applications",
'.bat':"C:\\Users\\Lakkireddy\\Downloads1\\Applications",
'.com':"C:\\Users\\Lakkireddy\\Downloads1\\Applications",
'.jar':"C:\\Users\\Lakkireddy\\Downloads1\\Applications",
'.apk':"C:\\Users\\Lakkireddy\\Downloads1\\Applications",
'.wsf':"C:\\Users\\Lakkireddy\\Downloads1\\Applications",


'.7z':"C:\\Users\\Lakkireddy\\Downloads1\\compressed_files",
'.pkg':"C:\\Users\\Lakkireddy\\Downloads1\\compressed_files",
'.rar':"C:\\Users\\Lakkireddy\\Downloads1\\compressed_files",
'.zip':"C:\\Users\\Lakkireddy\\Downloads1\\compressed_files",
'.z':"C:\\Users\\Lakkireddy\\Downloads1\\compressed_files",

'.iso':"C:\\Users\\Lakkireddy\\Downloads1\\images",
'noname':"C:\\Users\\Lakkireddy\\Downloads1\\others"
}

folder_to_track='C:\\Users\\Lakkireddy\\Downloads'
event_handler=MyHandler()
observer=Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

