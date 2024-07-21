import json

class Book: # Структура нашей библиотеки
    def __init__(self, title, author, year, status="в наличии"):
        self.id = None  # будем генерировать id автоматически
        self.title = title # Название книги
        self.author = author # Автор книги
        self.year = year # Год издания
        self.status = status # Статус (В наличии/Выдана)

    def set_id(self, book_id): # Генерация id книги
        self.id = book_id

    def get_details(self): # Вывод новой книги после её добавления
        return f"ID: {self.id}, Название: {self.title}, Автор: {self.author}, Год издания: {self.year}, Статус: {self.status}"
    
    @staticmethod # Делаем метод статическим для того, чтобы не делать экземпляр класса и работать прям внутри него
    def add_book(title, author, year, status="в наличии"):
        new_book = Book(title, author, year, status)
        try:
            with open('data/library.json', 'r', encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        new_book.set_id(len(data) + 1)
        book_info = {
            "id": new_book.id,
            "title": new_book.title,
            "author": new_book.author,
            "year": new_book.year,
            "status": new_book.status
        }
        data.append(book_info) 

        with open('data/library.json', 'w', encoding="utf-8") as file: # записываем новую книгу в json файл с кодировкой utf-8 для русских букв и различных символов
            json.dump(data, file, indent=4, ensure_ascii=False) # кодировку unicode выключаем для лучшего отображения данных в json файле (если такое не нужно - ставим True)
        
        return new_book
    
    @staticmethod
    def remove_book(book_id): # Функция удаления книги
        try:
            with open('data/library.json', 'r', encoding='utf-8') as file:
                data = json.load(file)  # Загружаем данные из файла
        except FileNotFoundError:
            print("Библиотека пуста.")
            return

        updated_data = [book for book in data if book["id"] != book_id]  # Создаем обновленный список без книги с заданным id

        if len(updated_data) == len(data):  # Если длина нового списка равна старой, значит книга не найдена
            print("Книга с таким ID не найдена.")
        else:
            # Обновление ID после удаления книги
            for i, book in enumerate(updated_data, start=1):
                book["id"] = i

            with open('data/library.json', 'w', encoding='utf-8') as file:
                json.dump(updated_data, file, indent=4, ensure_ascii=False)  # Записываем обновленные данные в файл
            print(f"Книга с ID {book_id} удалена.")

    @staticmethod
    def find_book(criteria, value): # Функция поиска книги по заданным критериям
        try:
            with open('data/library.json', 'r', encoding='utf-8') as file:
                data = json.load(file)  # Загружаем данные из файла
        except FileNotFoundError:
            print("Библиотека пуста.")
            return

        found_books = [book for book in data if str(book.get(criteria, "")).lower() == str(value).lower()]  # Ищем книги с заданными критериями

        if not found_books:  # Если список найденных книг пустой
            print("Книги с такими критериями не найдены.")
        else:
            for book in found_books:  # Выводим информацию о найденных книгах
                print(f"Найдена книга: {book['title']} - {book['author']} ({book['year']})")
    
    @staticmethod
    def display_all_books(): # Функция отображения всех книг в библиотеке
        try:
            with open('data/library.json', 'r', encoding='utf-8') as file:
                data = json.load(file)  # Загружаем данные из файла
        except FileNotFoundError:
            print("Библиотека пуста.")
            return

        for book in data:  # Выводим информацию о каждой книге в библиотеке
            print(f"{book['id']}. {book['title']} - {book['author']} ({book['year']}) - {book['status']}")

    @staticmethod
    def change_book_status(book_id, new_status):  # Функция изменения статуса книги
        try:
            with open('data/library.json', 'r', encoding='utf-8') as file:
                data = json.load(file)  # Загружаем данные из файла
        except FileNotFoundError:
            print("Библиотека пуста.")
            return

        for book in data:  # Изменяем статус книги с заданным id
            if book["id"] == book_id:
                book["status"] = new_status
                break
        else:  # Если книга с заданным id не найдена
            print("Книга с таким ID не найдена.")
            return

        with open('data/library.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)  # Записываем обновленные данные в файл
        print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")