import os
l = input("Enter you language: ")
while True:


    if l.casefold() in ["e", "english", "eng"]:
        choise = input("attrib file or deattrib file")
        if choise.casefold() in ["a", " ","add","adding","+","1"]:
            path = input("enter path to file")
            os.system(f"attrib  +s +h {path}")
        elif choise.casefold() in ["rm", "remove","-","0"]:
            path = input("enter path to file")
            os.system(f"attrib  -s -h {path}")



    elif l.casefold() in ["rus","ru","русский","ру","рус","русс"]:
        choise = input("Добавить или убрать аттрибут с файла? ")
        if choise.casefold() in ["Д", "Добавить","+","1"]:
            path = input("введите путь к файлу: ")
            os.system(f"attrib  +s +h {path}")
        elif choise.casefold() in ["У", "Удалить", "убрать"]:
            path = input("введите путь к файлу: ")
            os.system(f"attrib  -s -h {path}")


    else:
        print("somenting wrong")
