import xml.etree.ElementTree as ET
class DisplayXml:

    def indent(elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                DisplayXml.indent(subelem, level + 1)
            if not subelem.tail or not subelem.tail.strip():
                subelem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def save_to_xml(data, filename):

        root = ET.Element('books')

        tragedys = ET.SubElement(root, 'tragedys')
        for tragedy in data['tragedys']:
            tragedy_element = ET.SubElement(tragedys, 'tragedy')
            for key, value in tragedy.items():
                child = ET.SubElement(tragedy_element, key)
                child.text = str(value)

        ScienceFictions = ET.SubElement(root, 'ScienceFictions')
        for drink in data['ScienceFictions']:
            drink_element = ET.SubElement(ScienceFictions, 'ScienceFiction`')
            for key, value in drink.items():
                child = ET.SubElement(drink_element, key)
                child.text = str(value)

        Fairytales = ET.SubElement(root, 'Fairytales')
        for Fairytale in data['Fairytales']:
            Fairytale_element = ET.SubElement(Fairytales, 'Fairytale')
            for key, value in Fairytale.items():
                child = ET.SubElement(Fairytale_element, key)
                child.text = str(value)

        Fantasys = ET.SubElement(root, 'Fantasys')
        for Fantasy in data['Fantasys']:
            Fantasy_element = ET.SubElement(Fantasys, 'Fantasy')
            for key, value in Fantasy.items():
                child = ET.SubElement(Fantasy_element, key)
                child.text = str(value)

        Adventures = ET.SubElement(root, 'Adventures')
        for Adventure in data['Adventures']:
            Adventure_element = ET.SubElement(Adventures, 'Adventure')
            for key, value in Adventure.items():
                child = ET.SubElement(Adventure_element, key)
                child.text = str(value)

        CrimeAndMysterys = ET.SubElement(root, 'CrimeAndMysterys')
        for CrimeAndMystery in data['CrimeAndMysterys']:
            CrimeAndMystery_element = ET.SubElement(CrimeAndMysterys, 'CrimeAndMystery')
            for key, value in CrimeAndMystery.items():
                child = ET.SubElement(CrimeAndMystery_element, key)
                child.text = str(value)

#oooomagad

        DisplayXml.indent(root)
                # Создаем дерево XML и записываем его в файл
        try: #Обработка встроенной ошибки
            tree = ET.ElementTree(root)
            tree.write(filename, encoding='utf-8', xml_declaration=True)
            print(f"Все книги успешно сохранены в файл '{filename}'")
        except IOError as e:
            print(f"Ошибка при записи в XML-файл: {str(e)}")

    def load_from_xml(filename):
        try: #Обработка встроенной ошибки
            tree = ET.parse(filename)
            root = tree.getroot()
        except FileNotFoundError:
            return {"tragedys": [], "ScienceFictions": [], "Fairytales": [], "Fantasys": [],"Adventures": [],"CrimeAndMysterys": [],"soups": [],"Classics": []}

        data = {"tragedys": [], "ScienceFictions": [], "Fairytales": [], "Fantasys": [],"Adventures": [],"CrimeAndMysterys": [],"soups": [],"Classics": []}


        tragedys = root.find('tragedys')
        if tragedys is not None:
            for dish in tragedys:
                dish_data = {}
                for child in dish:
                    dish_data[child.tag] = child.text
                data['tragedys'].append(dish_data)

        ScienceFictions = root.find('ScienceFictions')
        if ScienceFictions is not None:
            for i in ScienceFictions:
                drink_data = {}
                for child in i:
                    drink_data[child.tag] = child.text
                data['ScienceFictions'].append(drink_data)


        Fairytales = root.find('Fairytales')
        if Fairytales is not None:
            for Fairytale in Fairytales:
                Fairytale_data = {}
                for child in Fairytale:
                    Fairytale_data[child.tag] = child.text
                data['Fairytales'].append(Fairytale_data)

        Fantasys = root.find('Fantasys')
        if Fantasys is not None:
            for Fantasy in Fantasys:
                Fantasy_data = {}
                for child in Fantasy:
                    Fantasy_data[child.tag] = child.text
                data['Fantasys'].append(Fantasy_data)

        Adventures = root.find('Adventures')
        if Adventures is not None:
            for Adventure in Adventures:
                Adventure_data = {}
                for child in Adventure:
                    Adventure_data[child.tag] = child.text
                data['Adventures'].append(Adventure_data)

        CrimeAndMystery = root.find('CrimeAndMysterys')
        if CrimeAndMystery is not None:
            for product in CrimeAndMystery:
                product_data = {}
                for child in product:
                    product_data[child.tag] = child.text
                data['CrimeAndMysterys'].append(product_data)

        return data

    #Добавление книг
    def add_tragedy(data, tragedy):
        data['tragedys'].append(tragedy.to_dict())

    def add_Science_Fiction(data, drink):
        data['ScienceFictions'].append(drink.to_dict())

    def add_Fairytale(data, Fairytale):
        data['Fairytales'].append(Fairytale.to_dict())

    def add_Fantasy(data, Fantasy):
        data['Fantasys'].append(Fantasy.to_dict())

    def add_Adventure(data, Adventure):
        data['Adventures'].append(Adventure.to_dict())

    def add_CrimeAndMystery(data, CrimeAndMystery):
        data['CrimeAndMysterys'].append(CrimeAndMystery.to_dict())

