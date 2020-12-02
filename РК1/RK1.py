from operator import itemgetter

class ProgLang:
    """Языки программирования"""
    def __init__(self, id, name, indextiobe, environment_id):
        self.id = id
        self.name = name
        self.indextiobe = indextiobe
        self.environment_id = environment_id

class DevEnvironment:
    """Средства разработки"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class LangDev:
    """Языки программирования в средствах разработки"""
    def __init__(self, lang_id, dev_id):
        self.lang_id = lang_id
        self.dev_id = dev_id
        
# Языки программирования
Langs = [
    ProgLang(1, 'Java', 16.7, 1),
    ProgLang(2, 'C', 15.2, 1),
    ProgLang(3, 'Python', 9.9, 2),
    ProgLang(4, 'C++', 5.6, 3),
    ProgLang(5, 'C#', 3.4, 3),
    ProgLang(6, 'JavaScript', 2.1, 3),
    ProgLang(7, 'SQL', 1.9, 4),
    ProgLang(8, 'PHP', 1.9, 4)
]

# Средства разработки
Devs = [
    DevEnvironment(1, 'MS Visual Studio'),
    DevEnvironment(2, 'Eclipse'),
    DevEnvironment(3, 'Aptana Studio'),
    DevEnvironment(4, 'Xcode')
]

# Языки программирования в средствах разработки
Langs_Devs = [
    LangDev(1,1),
    LangDev(2,1),
    LangDev(3,2),
    LangDev(4,3),
    LangDev(5,3),
    LangDev(6,3),
    LangDev(7,4),
    LangDev(8,4),
    LangDev(1,2),
    LangDev(2,4),
    LangDev(6,1)
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(l.name, l.indextiobe, d.name) 
        for d in Devs 
        for l in Langs 
        if l.environment_id==d.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ld.lang_id) 
        for d in Devs 
        for ld in Langs_Devs
        if d.id==ld.dev_id]
    
    many_to_many = [(dev_name, l.name, l.indextiobe) 
        for dev_name, lang_id in many_to_many_temp
        for l in Langs if l.id==lang_id]

    print('Задание Г1')
    List_1 = {}
    Needed_Devs = [Selected_Dev[2] for Selected_Dev in one_to_many if Selected_Dev[2].startswith('A')]
    for Name_Dev in Needed_Devs:
        Langs_Dev = [(Selected_Lang[0],Selected_Lang[1]) for Selected_Lang in one_to_many if Selected_Lang[2]==Name_Dev]
        List_1.update({Name_Dev:Langs_Dev})
    print(List_1)

    print('\nЗадание Г2')
    List_2 = []
    for d in Devs:
        d_langs = list(filter(lambda i: i[2]==d.name, one_to_many))
        if len(d_langs) > 0:
            d_indexes = [indextiobe for _,indextiobe,_ in d_langs]
            d_index_max = max(d_indexes)
            List_2.append((d.name, d_index_max))
    List_2 = sorted(List_2, key=itemgetter(1), reverse=True)
    print(List_2)
    
    print('\nЗадание Г3')
    List_3 = sorted(many_to_many, key=lambda i: (i[0], i[1]))
    print(List_3)

if __name__ == '__main__':
    main()
