class Person:
    def __init__(self):
        self.__name = "Default"
        self.__age = 0
        self.__driving_licence_number = 0
        self.__english_marks = 0
        self.__science_marks = 0
        self.__maths_marks = 0
        self.__history_marks = 0
        self.__geography_marks = 0

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def get_driving_licence_number(self):
        return self.__driving_licence_number

    def get_marks(self):
        return [self.__english_marks, self.__science_marks, self.__maths_marks, self.__history_marks, self.__geography_marks]

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age

    def set_driving_licence_number(self, new_number):
        self.__driving_licence_number = new_number

    def set_english_marks(self, new_marks):
        self.__english_marks=new_marks

    def set_science_marks(self, new_marks):
        self.__science_marks=new_marks

    def set_maths_marks(self, new_marks):
        self.__maths_marks=new_marks

    def set_history_marks(self, new_marks):
        self.__history_marks=new_marks

    def set_geography_marks(self, new_marks):
        self.__geography_marks=new_marks

p = Person()
print(p.get_name())
p.set_name("Akash")
p.set_age(21)
p.set_driving_licence_number(234334)
p.set_english_marks(50)
p.set_science_marks(30)
p.set_maths_marks(45)
p.set_history_marks(50)
p.set_geography_marks(35)
print(p.get_name())
print(p.get_age())
print(p.get_driving_licence_number())
print(p.get_marks())


