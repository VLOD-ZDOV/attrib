import os
#def attrib():
    #os.system(f'attrib  +s +h {way}')
#def deattib():
    #os.system(f'attrib  -s -h {way}')

l = input("enter language:")

if l == "e" or l == "E" or l == "English" or l == "english" or l == "eng" or l == "Eng":
    attORdeatrib = input("Add system attribute or remove? (A/D)\n")

elif l == "r" or l == "R" or l == "Russian "or l == "russian "or l == "ru" or l == "Ru" or l == "р":
    attORdeatrib =input("Убрать аттрибут системный или снять? (С/Д)\n")


#attrib
while attORdeatrib == "a" or attORdeatrib == "A" or attORdeatrib == "Add" or attORdeatrib == "add" or attORdeatrib == "Д" or attORdeatrib == "д" or attORdeatrib == "Добавить" or attORdeatrib == "ДОБАВИТЬ":
    if l == "e" or l == "E" or l == "English" or l == "english" or l == "eng" or l == "Eng":
        print ("Attention! if there are spaces in the path, enclose it in quotes like this:","c:/file")
        way = input("enter way to file:")
        #attrib
        os.system(f'attrib  +s +h {way}')
        
    elif l == "r" or l == "R" or l == "Russian "or l == "russian "or l == "ru" or l == "Ru":
        print ("Внимание! если в пути есть пробелы оберни в ковычки типо:","c:/файл")
        way = input("введите путь к файлу:")
        #attrib
        os.system(f'attrib  +s +h {way}')
        



#deattib
while attORdeatrib == "r" or attORdeatrib == "R" or attORdeatrib == "rm" or attORdeatrib == "Rm" or attORdeatrib == "RM" or attORdeatrib == "С" or  attORdeatrib == "с" or attORdeatrib == "убрать" or attORdeatrib == "Убр" or attORdeatrib == "снять":
    if l == "e" or l == "E" or l == "English" or l == "english" or l == "eng" or l == "Eng":
        print ("Attention! if there are spaces in the path, enclose it in quotes like this:","c:/file")
        way = input("enter way to file:")
        #deattib
        os.system(f'attrib  -s -h {way}')
    elif l == "r" or l == "R" or l == "Russian "or l == "russian "or l == "ru" or l == "Ru":
        print ("Внимание! если в пути есть пробелы оберни в ковычки типо:","c:/файл")
        way = input("введите путь к файлу:")
        #deattib
        os.system(f'attrib  -s -h {way}')
        

