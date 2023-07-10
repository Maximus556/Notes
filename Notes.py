import csv
import datetime
import uuid

# Функция для чтения всех заметок из файла с возможностью фильтрации по дате или вывод  всех заметок
def read_notes():
    filter_date = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД), либо оставьте поле пустым для вывода всех заметок: ")
    
    with open('notes.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            note_date = row[3].split()[0] 
            
            if filter_date == "" or note_date == filter_date: 
                print(f"Идентификатор: {row[0]}")
                print(f"Заголовок: {row[1]}")
                print(f"Текст: {row[2]}")
                print(f"Дата/время: {row[3]}")
                print("----------------------")


# Функция для добавления новой заметки
def add_note():
    id = str(uuid.uuid4())
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.datetime.now().strftime("%d-%m-%Y %S:%M:%H")
    print("----------------------")
    
    with open('notes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, title, body, date])
    
    print("Заметка успешно добавлена!")
    print("----------------------")

# Функция для редактирования существующей заметки
def edit_note():
    id = input("Введите идентификатор заметки, которую хотите отредактировать: ")
    new_title = input("Введите новый заголовок заметки: ")
    new_body = input("Введите новый текст заметки: ")
    new_date = datetime.datetime.now().strftime("%d-%m-%Y %S:%M:%H")
    
    with open('notes.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    for row in rows:
        if row[0] == id:
            row[1] = new_title
            row[2] = new_body
            row[3] = new_date
    
    with open('notes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("Заметка успешно отредактирована!")
    print("----------------------")

# Функция для удаления существующей заметки
def delete_note():
    id = input("Введите идентификатор заметки, которую хотите удалить: ")
    
    with open('notes.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    for row in rows:
        if row[0] == id:
            rows.remove(row)
    
    with open('notes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print("Заметка успешно удалена!")
    print("----------------------")
    
# Главное меню
while True:
    print("1. Просмотреть список заметок")
    print("2. Добавить новую заметку")
    print("3. Редактировать существующую заметку")
    print("4. Удалить существующую заметку")
    print("5. Выход")
    
    print("----------------------")
    choice = input("Выберите действие: ")
    
    if choice == "1":
        read_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
    elif choice == "5":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
print("----------------------")
