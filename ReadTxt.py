class ReadTxt:
    '''
        Объект класса ReadTxt репрезентует данные одного человека из заданного файла
        Нужен для записи из текстового файла
    Attributes
    ----------
    Email : str
        Почта
    Height : float
        Рост
    Inn : str
        ИНН
    Passport_series : str
        Серия паспорта
    Occupation : str
        Мировозрение
    Age : int
        Возраст
    Academic_degree : str
        Академическая степень
    Worldview : str
        Мировозрение
    Address : str
        Адрес
    ----------
    '''
    Email: str
    Height: float
    Inn: str
    Passport_series: str
    Occupation: str
    Age: int
    Academic_degree: str
    Worldview: str
    Address: str

    def __init__(self, email, height, inn, passport_series, occupation, age, academic_degree, worldview, address):
        self.Email = email
        self.Height = height
        self.Inn = inn
        self.Passport_series = passport_series
        self.Occupation = occupation
        self.Age = age
        self.Academic_degree = academic_degree
        self.Worldview = worldview
        self.Address = address

    def __getitem__(self, item):
        return self

    def fwrite(self, wfile):
        wfile.write('email:')
        wfile.write(self.Email)
        wfile.write('\n')
        wfile.write('height:')
        s_height = str(self.Height)
        wfile.write(s_height)
        wfile.write('\n')
        wfile.write('inn:')
        wfile.write(self.Inn)
        wfile.write('\n')
        wfile.write('passport_series:')
        wfile.write(self.Passport_series)
        wfile.write('\n')
        wfile.write('occupation:')
        wfile.write(self.Occupation)
        wfile.write('\n')
        wfile.write('age:')
        s_age = str(self.Age)
        wfile.write(s_age)
        wfile.write('\n')
        wfile.write('academic_degree:')
        wfile.write(self.Academic_degree)
        wfile.write('\n')
        wfile.write('worldview:')
        wfile.write(self.Worldview)
        wfile.write('\n')
        wfile.write('address:')
        wfile.write(self.Address)
        wfile.write('\n')
        wfile.write('\n')

    def print_data(self):
        print(self.Email)
        print(self.Height)
        print(self.Inn)
        print(self.Passport_series)
        print(self.Occupation)
        print(self.Age)
        print(self.Academic_degree)
        print(self.Worldview)
        print(self.Address, '\n')