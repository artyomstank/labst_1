class Book:
    # Конструктор
    def __init__(self, title, price):
        self.title = title
        self.price = price

    # Запись
    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price
        }


class Tragedy(Book):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages

    def to_dict(self):
        tragedy_dict = super().to_dict()
        tragedy_dict.update({
            "pages": self.pages
        })
        return tragedy_dict


class ScienceFiction(Book):
    def __init__(self, title, price, paper):
        super().__init__(title, price)
        self.paper = paper

    def to_dict(self):
        Science_Fiction_dict = super().to_dict()
        Science_Fiction_dict.update({
            "paper": self.paper,
        })
        return Science_Fiction_dict


class Fairytale(Book):
    def __init__(self, title, price, author):
        super().__init__(title, price)
        self.author = author

    def to_dict(self):
        Fairytale_dict = super().to_dict()
        Fairytale_dict.update({
            "author": self.author
        })
        return Fairytale_dict


class Fantasy(Book):
    def __init__(self, title, price, paper_color):
        super().__init__(title, price)
        self.paper_color = paper_color

    def to_dict(self):
        Fantasy_dict = super().to_dict()
        Fantasy_dict.update({
            "paper_color": self.paper_color,
        })
        return Fantasy_dict


class Adventure(Book):
    def __init__(self, title, price, chapters):
        super().__init__(title, price)
        self.chapters = chapters

    def to_dict(self):
        adventure_dict = super().to_dict()
        adventure_dict.update({
            "chapters": self.chapters
        })
        return adventure_dict


class CrimeAndMystery(Book):
    def __init__(self, title, price, main_character):
        super().__init__(title, price)
        self.main_character = main_character

    def to_dict(self):
        CAM_dict = super().to_dict()
        CAM_dict.update({
            "main_character": self.main_character,
        })
        return CAM_dict
