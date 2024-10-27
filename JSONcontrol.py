import json


# файл работы с JSON
class DisplayJson:
    # Функция записи в файл
    def save_to_json(data, filename):
        try:  # Обработка встроенной ошибки
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Все блюда успешно сохранены в JSON-файл {filename}")
        except IOError as e:
            print(f"Ошибка при записи в JSON-файл: {str(e)}")

    # Функция чтения из файла
    def load_from_json(filename):
        try:  # Обработка встроенной ошибки
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"tragedy": [], "ScienceFictions": [], "Fairytales": [], "Fantasys": [],
                    "Adventures": [], "CrimeAndMysterys": []}

    def add_tragedy(data, tragedys):
        data['tragedys'].append(tragedys.to_dict())

    def add_Science_Fiction(data, sf):
        data['drinks'].append(sf.to_dict())

    def add_Fairytale(data, frt):
        data['alcohols'].append(frt.to_dict())

    def add_Fantasy(data, fnt):
        data['desserts'].append(fnt.to_dict())

    def add_Adventure(data, adv):
        data['salads'].append(adv.to_dict())

    def add_CrimeAndMystery(data, cam):
        data['bakeries'].append(cam.to_dict())
