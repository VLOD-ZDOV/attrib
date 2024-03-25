import os

l = input("enter language:")
while True:
    if l == "e" or l == "E" or l == "English" or l == "english" or l == "eng" or l == "Eng":
        way = input("enter way to file:")
        os.system(f'attrib  +s +h "{way}"')

    elif l == "r" or l == "R" or l == "Russian "or l == "russian "or l == "ru" or l == "Ru":
        way = input("введите путь к файлу:")
        os.system(f'attrib  +s +h "{way}"')
    else:
        print("There are no other languages yet")

