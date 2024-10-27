from JSONcontrol import DisplayJson
from XMLcontrol import DisplayXml
from books import Tragedy, ScienceFiction, Fairytale, Fantasy, Adventure, CrimeAndMystery


# Валидация ввода
def get_good_number(x):
    while True:
        try:
            price = int(input(x))
            if price <= 0:
                raise ValueError
            return price
            break
        except ValueError:
            print("Введите положительное число.")


# Функция вывода данных из файла
def print_data(data, file_format):
    if file_format == 'json':
        print("\nДанные из JSON:")
    elif file_format == 'xml':
        print("\nДанные из XML:")

    print("\nТрагедии:")
    for dish in data['tragedys']:
        print(f"Название: {dish['title']}, Цена: {dish['price']} руб., Страницы: {dish['pages']}")

    print("\nНаучнаые фантастики:")
    for drink in data['ScienceFictions']:
        print(f"Название: {drink['title']}, Цена: {drink['price']} руб., Качество бумаги: {drink['paper']}")

    print("\nСказки")
    for Fairytale in data['Fairytales']:
        print(
            f"Название: {Fairytale['title']}, Цена: {Fairytale['price']} руб., Автор: {Fairytale['author']}")

    print("\nФантастика:")
    for Fantasy in data['Fantasys']:
        print(f"Название: {Fantasy['title']}, Цена: {Fantasy['price']} руб., Цвет бумаги: {Fantasy['paper_color']}")

    print("\nПриключения:")
    for Adventure in data['Adventures']:
        print(
            f"Название: {Adventure['title']}, Цена: {Adventure['price']} руб., Количество глав: {Adventure['chapters']}")

    print("\nКриминал и Мистика:")
    for CrimeAndMystery in data['CrimeAndMysterys']:
        print(
            f"Название: {CrimeAndMystery['title']}, Цена: {CrimeAndMystery['price']} руб., Главный персонаж: {CrimeAndMystery['main_character']}")


# Основа программы, вызов всех описанных функций
def main():
    dataFromJson = DisplayJson.load_from_json("books.json")  # читаем и закидываем туда данные
    dataFromXml = DisplayXml.load_from_xml("books.xml")

    while True:
        # Что-то типа swich-case
        choice = input("\n-----------------------"
                       "\nВыберите действие:\n"
                       "1. Добавить Трагедию\n"
                       "2. Добавить Научные фантастику\n"
                       "3. Добавить Сказку\n"
                       "4. Добавить Фантастику\n"
                       "5. Добавить Приключение\n"
                       "6. Добавить Криминал и Мистику\n"
                       "7. Сохранить в JSON\n"
                       "8. Сохранить в XML\n"
                       "9. Читать из JSON\n"
                       "10. Читать из XML\n"
                       "11. Выход\n"
                       "-----------------------\n")

        if choice == '1':
            title = input("Введите название Трагедии: ")
            price = get_good_number("Введите цену: ")
            pages = input("Введите количество страниц: ")
            tragedy = Tragedy(title, price, pages)
            DisplayJson.add_tragedy(dataFromJson, tragedy)
            DisplayXml.add_tragedy(dataFromXml, tragedy)
        elif choice == '2':
            title = input("Введите название Сказки: ")
            price = get_good_number("Введите цену: ")
            paper = get_good_number("Введите качество бумаги: ")
            drink = ScienceFiction(title, price, paper)
            DisplayJson.add_Science_Fiction(dataFromJson, drink)
            DisplayXml.add_Science_Fiction(dataFromXml, drink)
        elif choice == '3':
            title = input("Введите название Научной фантастики: ")
            price = get_good_number("Введите цену: ")
            author = get_good_number("Введите автора: ")
            Frt = Fairytale(title, price, author)
            DisplayJson.add_Fairytale(dataFromJson, Frt)
            DisplayXml.add_Fairytale(dataFromXml, Frt)
        elif choice == '4':
            title = input("Введите название Сказки: ")
            price = get_good_number("Введите цену: ")
            description = input("Введите автора: ")
            Fnt = Fantasy(title, price, description)
            DisplayJson.add_Fantasy(dataFromJson, Fnt)
            DisplayXml.add_Fantasy(dataFromXml, Fnt)
        elif choice == '5':
            title = input("Введите название Фантастики: ")
            price = get_good_number("Введите цену: ")
            chapters = input("Введите цвет бумаги: ")
            Adv = Adventure(title, price, chapters)
            DisplayJson.add_Adventure(dataFromJson, Adv)
            DisplayXml.add_Adventure(dataFromXml, Adv)
        elif choice == '6':
            title = input("Введите название Приключения: ")
            price = get_good_number("Введите цену: ")
            type = input("Введите количество глав: ")
            CAM = CrimeAndMystery(title, price, type)
            DisplayJson.add_CrimeAndMystery(dataFromJson, CAM)
            DisplayXml.add_CrimeAndMystery(dataFromXml, CAM)
        elif choice == '7':
            DisplayJson.save_to_json(dataFromJson, "books.json")
            print(f"Данные сохранены в books.json ")
        elif choice == '8':
            DisplayXml.save_to_xml(dataFromXml, "books.xml")
            print(f"Данные сохранены в books.xml ")
        elif choice == '9':
            print_data(dataFromJson, 'json')
        elif choice == '10':
            print_data(dataFromXml, 'xml')
        elif choice == '11':
            break


# Цикличность программы, не завершает работу после 1-го обработанного кейса
if __name__ == "__main__":
    main()
