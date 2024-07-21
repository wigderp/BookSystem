# Импортируем класс Book из модуля book
from book import Book
import time

# Функция для отображения меню действий
def display_menu():
    print("Выберите действие:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу")
    print("4. Отобразить все книги")
    print("5. Изменить статус книги")
    print("6. Выйти")

# Функция для интерфейса добавления книги
def add_book_interface():
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год издания книги: ")
    new_book = Book.add_book(title, author, year)  # Создаем новый объект книги
    print(f"Книга добавлена: {new_book.get_details()}")  # Выводим информацию о добавленной книге

# Функция для интерфейса удаления книги
def remove_book_interface():
    book_id = input("Введите ID книги, которую нужно удалить: ")
    try:
        Book.remove_book(int(book_id))  # Пытаемся удалить книгу с указанным ID
        print("Книга успешно удалена")
    except ValueError:
        print("Неверный формат ID книги")

# Функция для интерфейса поиска книги
def find_book_interface():
    search_criteria = input("Выберите критерий поиска (название, автор или год): ").lower()
    search_value = input(f"Введите значение для критерия '{search_criteria}': ")
    Book.find_book(search_criteria, search_value)  # Выполняем поиск книги по указанным критериям

# Функция для интерфейса изменения статуса книги
def change_status_interface():
    book_id = input("Введите ID книги, статус которой нужно изменить: ")
    print("Выберите статус книги:")
    print("1. Выдана")
    print("2. В наличии")
    new_status_choice = input("Выберите действие: ")
    if new_status_choice == "1":
        Book.change_book_status(int(book_id), "выдана")  # Изменяем статус книги на "выдана"
        print("Статус книги успешно изменен")
    elif new_status_choice == "2":
        Book.change_book_status(int(book_id), "в наличии")  # Изменяем статус книги на "в наличии"
        print("Статус книги успешно изменен")
    else:
        print("Неверное значение")

# Основная функция программы
def main():
    while True:
        display_menu()  # Отображаем меню действий
        choice = input("Выберите действие: ")  # Получаем выбор пользователя

        if choice == "1":  # Если выбрано "Добавить книгу"
            add_book_interface()  # Вызываем соответствующий интерфейс
        elif choice == "2":  # Если выбрано "Удалить книгу"
            remove_book_interface()  # Вызываем соответствующий интерфейс
        elif choice == "3":  # Если выбрано "Найти книгу"
            find_book_interface()  # Вызываем соответствующий интерфейс
        elif choice == "4":  # Если выбрано "Отобразить все книги"
            print("\n", "Список ваших книг:")
            Book.display_all_books()  # Отображаем все книги
            print("\n")
            time.sleep(10)  # Задержка на 10 секунд
        elif choice == "5":  # Если выбрано "Изменить статус книги"
            change_status_interface()  # Вызываем соответствующий интерфейс
        elif choice == "6": # Если выбрано "Выйти"
            print("До свидания!")
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__": 
    main()