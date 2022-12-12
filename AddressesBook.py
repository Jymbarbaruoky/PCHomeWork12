from collections import UserDict
from datetime import datetime



class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value


class Name(Field):
    pass


class Phone(Field):

    @Field.value.setter
    def value(self, value: str):
        if value.isnumeric():
            self._value = value
        else:
            print('Number must contain only digits')


class Birthday(Field):

    @Field.value.setter
    def value(self, value: str):
        try:
            self._value = datetime.strptime(value, '%d %B %Y')
        except ValueError:
            print('Invalid input form. Need for example: 10 January 2020')


class Record:
    def __init__(self, name):
        self.birthday = None
        self.name = Name(name)
        self.phones = []

    def add_birthday(self, value):
        self.birthday = Birthday(value)

    def days_to_birthday(self):
        if self.birthday.value:
            birthday_in_this_year = datetime(year=datetime.now().year, month=self.birthday.value.month, day=self.birthday.value.day)
            birthday_in_next_year = datetime(year=datetime.now().year + 1, month=self.birthday.value.month, day=self.birthday.value.day)
            if birthday_in_this_year < datetime.now():
                days_to_birthday = birthday_in_next_year - datetime.now()
                return f'{days_to_birthday.days} days until the next birthday'
            else:
                days_to_birthday = birthday_in_this_year - datetime.now()
                return f'{days_to_birthday.days} days until the next birthday'

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        print(f"You added {phone} to {self.name.value}")

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                print(f"You remove {phone} from {self.name.value}")
                return True
        return False

    def editing(self, old_phone, new_phone):
        if self.delete_phone(old_phone):
            self.add_phone(new_phone)

    def get_contacts(self):
        result = []
        for phone in self.phones:
            result.append(phone.value)
        return result


class AddressBook(UserDict):
    def __init__(self):
        self.step = 3
        self.boundary = self.step
        self.count = -1
        self.keys = [i for i in self.data.keys()]

    def __iter__(self):
        return self

    def __next__(self):
        if self.count + 1 < self.boundary:
            if self.count + 1 == len(self.keys):
                self.boundary = self.step
                self.count = -1
                raise StopIteration
            self.count += 1
            return self.data[self.keys[self.count]]
        if self.count + 1 == self.boundary:
            self.boundary += self.step
            raise StopIteration

    def add_record(self, record):
        self.data[record.name.value] = record


        