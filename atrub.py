import os
import ctypes
import stat

FILE_ATTRIBUTE_SYSTEM = 0x00000020
FILE_ATTRIBUTE_HIDDEN = 0x00000002

def add_attributes_ctypes(file_path):
    ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_SYSTEM | FILE_ATTRIBUTE_HIDDEN)

def remove_attributes_ctypes(file_path):
    ctypes.windll.kernel32.SetFileAttributesW(file_path, 0)

def add_attributes_os(file_path):
    st = os.stat(file_path)
    new_permissions = st.st_mode | stat.S_ISYSTEM | stat.S_IHIDDEN
    os.chmod(file_path, new_permissions)

def remove_attributes_os(file_path):
    st = os.stat(file_path)
    new_permissions = st.st_mode & ~(stat.S_ISYSTEM | stat.S_IHIDDEN)
    os.chmod(file_path, new_permissions)

def choose_method():
    print("Выберите способ:")
    print("1. ctypes")
    print("2. os")
    print("способ 2 не рабочий")
    choice = input("Введите номер способа (1 или 2): ")
    return choice

def add_or_remove_attributes():
    while True:
        method_choice = choose_method()
        if method_choice == '1':
            add_or_remove = input("Хотите добавить или удалить атрибуты? (добавить/удалить): ").lower()
            if add_or_remove == 'добавить' or '+' or '1':
                file_path = input("Введите путь к файлу: ")
                add_attributes_ctypes(file_path)
                print(f"Атрибуты 'скрытый' и 'системный' успешно добавлены к файлу {file_path}.")
            elif add_or_remove == 'удалить' or '-' or '2':
                file_path = input("Введите путь к файлу: ")
                remove_attributes_ctypes(file_path)
                print(f"Атрибуты 'скрытый' и 'системный' успешно удалены из файла {file_path}.")
            else:
                print("Неверный ввод. (Возможно вы написали с ковычками)")
            break
        elif method_choice == '2':
            add_or_remove = input("Хотите добавить или удалить атрибуты? (добавить/удалить): ").lower()
            if add_or_remove == 'добавить' or '+' or '1':
                file_path = input("Введите путь к файлу: ")
                add_attributes_os(file_path)
                print(f"Атрибуты 'скрытый' и 'системный' успешно добавлены к файлу {file_path}.")
            elif add_or_remove == 'удалить' or '-' or '2':
                file_path = input("Введите путь к файлу: ")
                remove_attributes_os(file_path)
                print(f"Атрибуты 'скрытый' и 'системный' успешно удалены из файла {file_path}.")
            else:
                print("Неверный ввод. (Возможно вы написали с ковычками)")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите '1' или '2'.")


add_or_remove_attributes()