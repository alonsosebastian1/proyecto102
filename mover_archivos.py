import os
import shutil

from_dir ="C:/Users/alons/Downloads"
to_dir = "C:/Users/alons/Desktop/Archivos_Documentos"

list_of_files =os.listdir(from_dir)
#print(list_of_files)
for file_name in list_of_files:
    name,extencion = os.path.splitext(file_name)
    #print(name)
    #print(extencion)
    if extencion == "":
        continue
    if extencion in [".png",".jpg"]:
        ruta1 =  from_dir+'/'+file_name
        ruta2 =  to_dir + '/' + "Archivos_Documentos"
        ruta3 =  to_dir + '/' + "Archivos_Documentos" + '/' + file_name
        if os.path.exists(ruta2):
            print("moving" + file_name + ".....")
            shutil.move(ruta1,ruta3)
        else:
            os.makedirs(ruta2)
            print("moving" + file_name + "....")
            shutil.move(ruta1,ruta3)
