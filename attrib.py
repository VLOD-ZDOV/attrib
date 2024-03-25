import os
def attrib():
    if l.casefold() in ["e", "english", "eng"]:
        way = input("enter way to file:")  
        os.system(f"attrib  +s +h {way}")

    elif l.casefold() in ["rus","ru","русский","ру","рус","русс"]:
        way = input("введите путь к файлу:")
        os.system(f"attrib  +s +h {way}")



def deattrib():
    if l.casefold() in ["e", "english", "eng"]:
        way = input("enter way to file:")  
        os.system(f"attrib  -s -h {way}")

    elif l.casefold() in ["rus","ru","русский","ру","рус","русс","Р","р"]:
        way = input("введите путь к файлу:")
        os.system(f"attrib  -s -h {way}")





def main():
    
    if l.casefold() in ["e", "english", "eng"]:
        attORdeattrib = input("Add system attribute or remove? (A/D)\n")
        return attORdeattrib

    elif l.casefold() in ["р","r","russian","rus","ru","русский","ру","рус","русс"]: 
        attORdeattrib =input("Добавить аттрибут системный или снять? (Д/С)\n")
        return attORdeattrib
    
print("Я ХЗ ПОЧЕМУ НО РУССКИЙ НЕ РАБОТАЕТ ПИШИ: eng")    
l = input("enter language:")        
attORdeattrib = main()




main

while True:
    if attORdeattrib in ["Д", "д", "add", "Add", "Доб", "Доб", "Добавить","a", "A"]:
        attrib()
    elif attORdeattrib in ["d", "delete", "D", "удалить", "У", "Удалить", "r","rm","remove", "R","RM","Remove","снять","Снять"]:
        deattrib()
    else:
        print("error")
        print("exit")
        break
        


# #attrib
# while l.casefold() in["a", "add", "A", "добавить", "Д", "Доб", "Добавить"] :
#     if l.casefold() in ["e", "english", "eng"]:
#         print ("Attention! if there are spaces in the path, enclose it in quotes like this:","c:/file")
#         way = input("enter way to file:")
#         attrib
        
        
#     elif l.casefold() in ["д","доб","добавить","rus","ru","русский","ру","рус","русс"]:
#         print ("Внимание! если в пути есть пробелы оберни в ковычки типо:","'c:/файл'")
#         way = input("введите путь к файлу:")
#         attrib
        
    

# #deattrib
# while l.casefold() in ["d", "delete", "D", "удалить", "У", "Удалить"]:
#     if l.casefold() in ["e", "english", "eng"]:                                                         #english vers
#         print ("Attention! if there are spaces in the path, enclose it in quotes like this:","c:/file")
#         way = input("enter way to file:")
#         deattrib


#     elif l.casefold() in ["р","r","russian","rus","ru","русский","ру","рус","русс"]:                     #russian vers
#         print ("Внимание! если в пути есть пробелы оберни в ковычки типо:","'c:/файл'")
#         way = input("введите путь к файлу:")
#         deattrib
        
        

