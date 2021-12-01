# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import json
import re
from tqdm import tqdm
from ReadTxt import ReadTxt
import argparse

class Validator:
    users_data: ReadTxt = []

    def __init__(self, users_data):
        self.users_data = users_data

    # @staticmethod
    def check_email(self, email: str) -> bool:
        '''
        Выполняет проверку корректности адреса электронной почты.

        Если в строке присутствуют пробелы, запятые, двойные точки,
        а также неверно указан домен адреса, то будет возвращено False.

        Parameters
        ----------
          email : str
            Строка с проверяемым электронным адресом

        Returns
        -------
          bool:
            Булевый результат проверки на корректность
        '''
        pattern = r"^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, str(email)):
            return True
        return False

    # @staticmethod
    def check_height(self, height: float):
        '''
                Выполняет проверку корректности роста.

                Если рост меньше 0.6 или больше 2.79 возвращается False.
                Если рост записан в виде отличном от числа с плавающей точой, возвращается False

                Parameters
                ----------
                  height : float
                    Строка с проверяемым ростом

                Returns
                -------
                  bool:
                    Булевый результат проверки на корректность
        '''
        pattern1 = r"^1\.\d{2}$"
        pattern2 = r"^2\.[0-7]{1}\d{1}$"
        pattern3 = r"^0\.[6-9]{1}\d{1}$"
        if re.match(pattern1, str(height)):
            return True
        if re.match(pattern2, str(height)):
            return True
        if re.match(pattern3, str(height)):
            return True
        return False

    # @staticmethod
    def check_inn(self, inn: str) -> bool:
        '''
                        Выполняет проверку корректности ИНН.

                        Если ИНН состоит не из 12 цифр возвращается False.

                        Parameters
                        ----------
                          inn : str
                            Строка с проверяемым ИНН

                        Returns
                        -------
                          bool:
                            Булевый результат проверки на корректность
        '''
        pattern = r"\d{12}"
        if re.match(pattern, str(inn)):
            return True
        return False

    # @staticmethod
    def check_passport_series(self, passport_series: str) -> bool:
        '''
                                Выполняет проверку корректности серии паспорта.

                                Если серия паспорта состоит не из 2 цифр пробела 2 цифр возвращается False.

                                Parameters
                                ----------
                                  passport_series : str
                                    Строка с проверяемой серией паспорта
                                Returns
                                -------
                                  bool:
                                    Булевый результат проверки на корректность
                                '''
        pattern = r"\d{2}\s\d{2}"
        if re.match(pattern, str(passport_series)):
            return True
        return False

    # @staticmethod
    def check_occupation(self, occupation: str) -> bool:
        '''
                                Выполняет проверку корректности профессии.

                                Если профессия не одна из прописанных в паттернах, возвращается False.

                                Parameters
                                ----------
                                  occupation : str
                                    Строка с проверяемой профессией

                                Returns
                                -------
                                  bool:
                                    Булевый результат проверки на корректность
                                '''
        pattern1 = "Мерчендайзер|Окулист|Пожарный|Диктор|Дегустатор|Прозектор|Повар|Диджей|Супервайзер|Редактор|Кинолог"
        pattern2 = "Преподаватель|Флорист|Билетный кассир|Официант|Рыбак|Промышленный альпинист|Бренд-менеджер|Грузчик"
        pattern3 = "Монтажник|Web-дизайнер|Сапожник|Ювелир|Реставратор|Гинеколог|Менеджер по продажам"
        pattern4 = "Секретарь-стенографистка|Писатель|Оператор call-центра|Бригадир железнодорожного пути|Психолог"
        pattern5 = "Маркетолог|Контент-менеджер|Банковский кассир-операционист|Венеролог|Политолог|Шлифовщик|Религиовед"
        pattern6 = "Продавец-консультант|Кондитер|Бондарь|Педиатр|Агент по туризму|Изобретатель|Проходчик|Фальцовщик"
        pattern7 = "Проктолог|Ассистент менеджера по продажам|Фотомодель|Реабилитолог|Web-интегратор"
        pattern8 = "Менеджер по закупкам|Журналист|Оператор машинного доения|Бортмеханик|Слесарь|Востоковед"
        pattern9 = "Мусоропроводчик|Главный конструктор|Сценарист|Художник|Инфекционист|Врач скорой помощи|Уролог"
        pattern10 = "Электромонтажник|Бизнес-консультант|Бульдозерист|Нефролог|Телохранитель|Дизайнер-модельер"
        pattern11 = "Крановщик|Штукатур|Геодезист|Кладовщик|Нанотехнолог|Вирусолог|Тестировщик|Экономист|Месильщик"
        pattern12 = "Стоматолог|Финансовый аналитик|Охранник|Фрезеровщик|Бортпроводник|Автомеханик|Комбайнер|Литейщик"
        pattern13 = "Иллюстратор|Постановщик трюков|Тележурналист|Медицинская сестра|Композитор|Детектив|Киномеханик"
        pattern14 = "Дерматовенеролог|Сварщик|Пастух|Мастер|Мультипликатор|Маклер|Лингвист|Животновод|Кассир|Брокер"
        pattern15 = "Менеджер по логистике|Библиограф|Кинодраматург|Маникюрша|Бухгалтер|Технолог|Конструктор"
        pattern16 = "Консультант по туризму|Бармен|Винодел|Художник по костюму|Учитель|Космонавт"
        pattern17 = "Специалист по стрижке овец|Инженер-конструктор|Терапевт|Дипломат|Спортивный врач|Психиатр"
        pattern18 = "Администратор гостиницы|Биоинженер|Режиссер|Главный технолог|Педагог|Лаборант|Сексолог|Ортопед"
        pattern19 = "Адвокат|Швея|Секретарь-референт|Генный инженер|Плотник|Бизнес-аналитик|Зоолог|Металлург"
        pattern20 = "Тюремный надзиратель|Менеджер по работе с клиентами|Оториноларинголог|Системный администратор"
        pattern21 = "Реаниматолог|Шеф-повар|Следователь|Модель|Массажист|Химик|Охотник|Закройщик|Акушер|Бренд-дизайнер"
        pattern22 = "Аудитор|Уборщица|Автослесарь|Сталевар|Радиомеханик|Косметолог|Летчик|Лоббист|Таксист|Хореограф"
        pattern23 = "Садовник|Стрелочник|Шахтер|HTML-верстальщик|Историк|Заведующий складом|Риелтор|Водитель|Статистик"
        pattern24 = "Капитан судна|Мусорщик|Тифлопедагог|Фотограф|Токарь|Манекенщица|Диспетчер|Правовед|Банкир|Биохимик"
        pattern25 = "Администратор ресторана|Каменщик|Штурман|Типограф|Дизайнер|Нотариус|Программист|Оценщик|Электрик"
        pattern26 = "Администратор базы данных|Матрос|Оператор ПК|Ландшафтный дизайнер|Метеоролог|Спортивный тренер"
        pattern27 = "Офтальмолог|Ботаник|Менеджер по рекламе|Артист цирка|Библиотекарь|Специалист по ВЭД|Каскадер"
        pattern28 = "Сантехник|Анестезиолог|Инкассатор|Отделочник|Проводник|Печатник|Конвоир|Кардиохирург|Генетик"
        pattern29 = "Авиадиспетчер|Логист|Дистрибутор|Копирайтер|Референт|Кровельщик|Главный инженер|Философ"
        pattern30 = "Палеонтолог|Невролог|Пекарь|Цветочница|Строитель|Торговый представитель|Дизайнер рекламы|Геолог"
        pattern31 = "Стюардесса|Картограф|Микробиолог|Инженер|Столяр|Менеджер по PR|Бортинженер|Кинооператор|Астроном"
        pattern32 = "Почтальон|Краснодеревщик|Горняк|Дирижер|Менеджер торгового зала|Выпускающий редактор|Звукооператор"
        pattern33 = "Хирург|Визажист|Товаровед|Судебный пристав|Скотник|Судья|Финансист|Фермер|Воздухоплаватель"
        pattern34 = "Мануалист|Налоговый инспектор|Машинист|Критик|Водолаз|Энергетик|Эндокринолог|Биофизик|Физик|Радист"
        pattern35 = "Моряк|Татуировщик|Гидролог|Кинорежиссер|Социолог|Кардиолог|Нейрохирург|Почвовед|Ремонтник"
        pattern36 = "Архитектор-проектировщик|Аппаратчик-оператор|Ихтиолог|Настройщик музыкальных инструментов"
        pattern37 = "Иммунолог|Менеджер|Священнослужитель|Ветеринар|Облицовщик|Издатель|Автогонщик|Министр|Стилист"
        pattern38 = "Невропатолог|Архивариус|Проректор|Дорожный инспектор|Портной|Переплетчик|Экспедитор"
        pattern39 = "Консультант телефона доверия|Врач-диетолог|Администратор предприятия торговли|Инженер-химик|Эколог"
        pattern40 = "Машинистка|Агроном|Юрист|Геоэколог|Дерматолог|Продавец|Прокурор|Тракторист|Теолог|Инженер-технолог"
        pattern41 = "Переводчик|Медиа-байер|Корректор|Маляр|Этнограф|Web-программист|Имиджмейкер|Администратор сайта"
        pattern42 = "Рихтовщик|Холодильщик|Делопроизводитель|Искусствовед|Офис-менеджер|Логопед|Монах|Зубной техник"
        pattern43 = "Слесарь-механик|Наладчик|Психотерапевт|Андролог|Трейдер|Фармацевт|Балетмейстер|Скульптор"
        pattern44 = "Звукорежиссер|Вышивальщица|Культуролог|Химик-технолог|Промоутер|Парикмахер|Доярка|Травматолог"
        pattern45 = "Археолог|Моторист|Дворник|Снабженец|Упаковщик|Сурдопедагог|Менеджер по персоналу|Испытатель"
        pattern46 = "Верстальщик|Менеджер по туризму|Токсиколог|Страховой агент|Ректор|Кризис-менеджер|Курьер"
        pattern47 = "Технический писатель|Маркшейдер|Актер|Дефектолог|Биолог|Мясник|Спичрайтер|Продюсер|Диетолог"
        pattern48 = "Булочник|Полицейский|Архитектор|Администратор салона красоты|Драпировщик|Пчеловод|Бизнес-тренер"
        pattern49 = "Прораб|Телеграфист|Музыкант|Гид-переводчик|Сметчик|Аниматор|Онколог|Фельдшер|Орнитолог|Спортсмен"
        if re.match(pattern1, occupation):
            return True
        if re.match(pattern2, occupation):
            return True
        if re.match(pattern3, occupation):
            return True
        if re.match(pattern4, occupation):
            return True
        if re.match(pattern5, occupation):
            return True
        if re.match(pattern6, occupation):
            return True
        if re.match(pattern7, occupation):
            return True
        if re.match(pattern8, occupation):
            return True
        if re.match(pattern9, occupation):
            return True
        if re.match(pattern10, occupation):
            return True
        if re.match(pattern11, occupation):
            return True
        if re.match(pattern12, occupation):
            return True
        if re.match(pattern13, occupation):
            return True
        if re.match(pattern14, occupation):
            return True
        if re.match(pattern15, occupation):
            return True
        if re.match(pattern16, occupation):
            return True
        if re.match(pattern17, occupation):
            return True
        if re.match(pattern18, occupation):
            return True
        if re.match(pattern19, occupation):
            return True
        if re.match(pattern20, occupation):
            return True
        if re.match(pattern21, occupation):
            return True
        if re.match(pattern22, occupation):
            return True
        if re.match(pattern23, occupation):
            return True
        if re.match(pattern24, occupation):
            return True
        if re.match(pattern25, occupation):
            return True
        if re.match(pattern26, occupation):
            return True
        if re.match(pattern27, occupation):
            return True
        if re.match(pattern28, occupation):
            return True
        if re.match(pattern29, occupation):
            return True
        if re.match(pattern30, occupation):
            return True
        if re.match(pattern31, occupation):
            return True
        if re.match(pattern32, occupation):
            return True
        if re.match(pattern33, occupation):
            return True
        if re.match(pattern34, occupation):
            return True
        if re.match(pattern35, occupation):
            return True
        if re.match(pattern36, occupation):
            return True
        if re.match(pattern37, occupation):
            return True
        if re.match(pattern38, occupation):
            return True
        if re.match(pattern39, occupation):
            return True
        if re.match(pattern40, occupation):
            return True
        if re.match(pattern41, occupation):
            return True
        if re.match(pattern42, occupation):
            return True
        if re.match(pattern43, occupation):
            return True
        if re.match(pattern44, occupation):
            return True
        if re.match(pattern45, occupation):
            return True
        if re.match(pattern46, occupation):
            return True
        if re.match(pattern47, occupation):
            return True
        if re.match(pattern48, occupation):
            return True
        if re.match(pattern49, occupation):
            return True

    # @staticmethod
    def check_age(self, age: int) -> bool:
        '''
                                Выполняет проверку корректности возраста.

                                Если возраст менее 10 лет или более 99, возвращается False
                                Если возраст состоит не из цифр, возвращается False.

                                Parameters
                                ----------
                                  age : int
                                    Строка с проверяемым возрастом

                                Returns
                                -------
                                  bool:
                                    Булевый результат проверки на корректность
                                '''
        pattern1 = r"^[1-9]\d{1}$"
        # pattern2 = r"^1[0]{1}\d{1}$"
        if re.match(pattern1, str(age)):
            return True
        # if re.match(pattern2, str(age)):
            # return True
        return False

    def check_academic_degree(self, academic_degree: str) -> bool:
        '''
                                Выполняет проверку корректности академической степени.

                                Если академическая степень не одна из прописанных в паттерне, возвращается False.

                                Parameters
                                ----------
                                  academic_degree : str
                                    Строка с проверяемой академической степенью

                                Returns
                                -------
                                  bool:
                                    Булевый результат проверки на корректность
                                '''
        pattern = "Бакалавр|Кандидат наук|Магистр|Специалист|Доктор наук"
        if re.match(pattern, academic_degree):
            return True
        return False

    # @staticmethod
    def check_worldview(self, worldview: str) -> bool:
        '''
                                        Выполняет проверку корректности мировозрения.

                                        Если мировозрение не одно из прописанных в паттерне, возвращается False.

                                        Parameters
                                        ----------
                                          worldview : str
                                            Строка с проверяемым мировозрением

                                        Returns
                                        -------
                                          bool:
                                            Булевый результат проверки на корректность
                                        '''
        pattern = "Секулярный гуманизм|Агностицизм|Иудаизм|Пантеизм|Католицизм|Конфуцианство|Деизм|Атеизм|Буддизм"
        if re.match(pattern, worldview):
            return True
        return False

    # @staticmethod
    def check_address(self, address: str) -> bool:
        '''
                Выполняет проверку корректности академической степени.

                Если адрес не соответствует формату "ул." пробел, название улицы с большой буквы, в некоторых случачях
                 номер улицы в формате число-я, например 1-я, 7-я, возвращается False.
                Если адрес не соответствует формату "Аллея" пробел, название улицы с большой буквы, в некоторых случачях
                 номер улицы в формате число-я, например 1-я, 7-я, возвращается False.

                Parameters
                ----------
                    address : str
                    Строка с проверяемым адресом

                    Returns
                    -------
                        bool:
                            Булевый результат проверки на корректность
        '''
        pattern1 = r"^(ул\.\s){1}(\S{1,}\s)+(\d+)$"
        pattern2 = r"^(Аллея\s){1}(\S{1,}\s)+(\d+)$"
        if re.match(pattern1, address) or re.match(pattern2, address):
            return True
        return False


parser = argparse.ArgumentParser("Input & output parser")
parser.add_argument("-input", type=str, default="C:\\Lab_2\\23.txt")
parser.add_argument("-output", type=str, default="C:\\Lab_2\\23valid.txt")
pars = parser.parse_args()
default_path = pars.input
valid_path = pars.output
# rpath = 'C:\\Lab_2\\23.txt'
# wpath = 'C:\\Lab_2\\23valid.txt'
data_list_of_dict = json.load(open(default_path, encoding='windows-1251'))
users_list = []
valid_list = []
# occupation_list = []
# worldview_list = []
email_flag: bool = False
height_flag: bool = False
inn_flag: bool = False
passport_series_flag: bool = False
occupation_flag: bool = False
age_flag: bool = False
academic_degree_flag: bool = False
worldview_flag: bool = False
address_flag: bool = False
email_counter: int = 0
height_counter: int = 0
inn_counter: int = 0
passport_series_counter: int = 0
occupation_counter: int = 0
age_counter: int = 0
academic_degree_counter: int = 0
worldview_counter: int = 0
address_counter: int = 0
valid_counter: int = 0
for i in data_list_of_dict:
    users_list.append(ReadTxt(i['email'], i['height'], i['inn'], i['passport_series'], i['occupation'], i['age'],
                              i['academic_degree'], i['worldview'], i['address']))
validator = Validator(users_list)
# wfile = open(wpath, 'w')
with tqdm(total=len(users_list)) as progressbar:
    for i in range(len(users_list)):

        if validator.check_email(validator.users_data[i].Email):    # check email
            email_flag = True
        else:
            email_counter += 1

        if validator.check_height(validator.users_data[i].Height):    # check height
            height_flag = True
        else:
            height_counter += 1

        if validator.check_inn(validator.users_data[i].Inn):    # check inn
            inn_flag = True
        else:
            inn_counter += 1

        if validator.check_passport_series(validator.users_data[i].Passport_series):    # check passport series
            passport_series_flag = True
        else:
            passport_series_counter += 1

        if validator.check_occupation(validator.users_data[i].Occupation):  # check occupation
            occupation_flag = True
        else:
            occupation_counter += 1

        if validator.check_age(validator.users_data[i].Age):    # check age
            age_flag = True
        else:
            age_counter += 1

        if validator.check_academic_degree(validator.users_data[i].Academic_degree):  # check academic degree
            academic_degree_flag = True
        else:
            academic_degree_counter += 1

        if validator.check_worldview(validator.users_data[i].Worldview):  # check worldview
            worldview_flag = True
        else:
            worldview_counter += 1

        if validator.check_address(validator.users_data[i].Address):  # check address
            address_flag = True
        else:
            address_counter += 1

        if email_flag and height_flag and inn_flag and passport_series_flag and occupation_flag and age_flag\
                and academic_degree_flag and worldview_flag and address_flag:
            # validator.users_data[i].fwrite(wfile)
            user = {"email": validator.users_data[i].Email, "height": validator.users_data[i].Height,
                    "inn": validator.users_data[i].Inn,
                    "passport_series": validator.users_data[i].Passport_series,
                    "occupation": validator.users_data[i].Occupation, "age": validator.users_data[i].Age,
                    "academic_degree": validator.users_data[i].Academic_degree,
                    "worldview": validator.users_data[i].Worldview, "address": validator.users_data[i].Address}
            valid_list.append(user)
            # valid_list.append(validator.users_data[i].Email)
            # valid_list.append(validator.users_data[i].Height)
            # valid_list.append(validator.users_data[i].Inn)
            # valid_list.append(validator.users_data[i].Passport_series)
            # valid_list.append(validator.users_data[i].Occupation)
            # valid_list.append(validator.users_data[i].Age)
            # valid_list.append(validator.users_data[i].Academic_degree)
            # valid_list.append(validator.users_data[i].Worldview)
            # valid_list.append(validator.users_data[i].Address)
            valid_counter += 1
        email_flag: bool = False
        height_flag: bool = False
        inn_flag: bool = False
        passport_series_flag: bool = False
        occupation_flag: bool = False
        age_flag: bool = False
        academic_degree_flag: bool = False
        worldview_flag: bool = False
        address_flag: bool = False
        progressbar.update(1)
# file = open(wpath, 'w', encoding='windows-1251')
with open(valid_path, "w", encoding='windows-1251') as file:
    json.dump(valid_list, file)
# print(valid_list)

print("count of valid data:", valid_counter, "\ncount of not valid data:", len(users_list)-valid_counter,
      "\nfalse mail:", email_counter, "\nfalse height:", height_counter,
      "\nfalse inn:", inn_counter, "\nfalse passport series:", passport_series_counter, "\nfalse occupation:",
      occupation_counter, "\nfalse age:", age_counter, "\nfalse academic degree:", academic_degree_counter,
      "\nfalse worldview:", worldview_counter, "\nfalse address:", address_counter)

# print("\n", worldview_list)
# print("\n", len(worldview_list))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
