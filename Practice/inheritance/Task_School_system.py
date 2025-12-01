class Person:
    def __init__(self, name: str, age: int, email: str, person_id: str):
        self._name = name
        self._age = age
        self._email = email
        self.__id = person_id
        self._contact_info: dict[str, int | str | None] = {
            'phone': None,
            'address': None
        }

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if len(new_name) < 2:
            raise AttributeError('Имя должно состоять из 2 и более букв')

        for letter in new_name:
            if not letter.isalpha() or letter != ' ':
                raise AttributeError('Имя должно содержать только буквы и пробелы')

        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age: int):
        if new_age < 5 or new_age > 100:
            raise AttributeError('Возраст должен быть от 5 до 100 лет')

        self._age = new_age

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email: int):
        if '@' not in new_email:
            raise AttributeError('Email адрес должен содержать символ @')

        self._email = new_email

    @property
    def id(self):
        return self.__id

    def get_info(self):
        return f'Name: {self.name}, Age: {self.age}, Email: {self.email}'

    def update_contact(self, phone: int | None = None, address: str | None = None):
        if phone is not None:
            self._contact_info['phone'] = phone

        if address is not None:
            self._contact_info['address'] = address

        print('Contact information updated')

    def send_notification(self, message: str):
        print(f'Notification: {message}')

class Student(Person):
    def __init__(self,
                 name: str,
                 age: int,
                 email: str,
                 person_id: str,
                 student_number: int,
                 grades: dict[str, list[int]],
                 attendance: float,
                 scholarship: int
                 ):
        super().__init__(name, age, email, person_id)
        self._student_number = student_number
        self._grades = grades
        self._attendance = attendance
        self._scholarship = scholarship

    def add_grade(self, subject: str, grade: int):
        pass

    def get_average(self, subject: str | None = None):
        pass

    def get_info(self):
        pass

    def calculate_scholarship(self):
        pass

    def mark_attendance(self, present: int):
        pass

# КЛАСС 2: Student (Студент - наследуется от Person)
# Дополнительные атрибуты:
#   • _student_number (номер студента) - защищённый
#   • _grades (словарь: {предмет: список оценок}) - защищённый
#   • _attendance (посещаемость в %) - защищённый
#   • _scholarship (размер стипендии) - защищённый
#
# Дополнительные методы:
#   • add_grade(subject, grade) - добавить оценку (проверка: 2-5)
#   • get_average(subject=None) - средний балл (по предмету или общий)
#   • get_info() - ПЕРЕОПРЕДЕЛИТЬ, добавить информацию о студенте
#   • calculate_scholarship() - рассчитать стипендию на основе среднего балла
#     ↳ Средний балл >= 4.5 → 5000 руб
#     ↳ Средний балл >= 4.0 → 3000 руб
#     ↳ Средний балл >= 3.5 → 2000 руб
#     ↳ Средний балл < 3.5 → 0 руб
#   • mark_attendance(present) - отметить посещаемость
#     ↳ Обновляет процент посещаемости
#
# Property:
#   • student_number - только getter (read-only)
#   • scholarship - только getter (вычисляемое через calculate_scholarship())
#   • grades_summary - вычисляемое свойство (словарь {предмет: средняя оценка})
#   • attendance - только getter (read-only)
#
#
# КЛАСС 3: Teacher (Преподаватель - наследуется от Person)
# Дополнительные атрибуты:
#   • _employee_id (ID сотрудника) - защищённый
#   • _subjects (список предметов) - защищённый
#   • _salary (зарплата) - защищённый
#   • _rating (рейтинг преподавателя 1-5) - защищённый
#   • _students (список студентов) - защищённый
#
# Дополнительные методы:
#   • __init__(name, age, email, person_id, employee_id, subjects, salary)
#     ↳ Использовать super().__init__()
#   • add_subject(subject) - добавить предмет
#   • remove_subject(subject) - удалить предмет
#   • assign_student(student) - назначить студента
#   • grade_student(student, subject, grade) - поставить оценку студенту
#     ↳ Проверка: преподаватель ведёт этот предмет
#     ↳ Вызывает student.add_grade()
#   • get_info() - ПЕРЕОПРЕДЕЛИТЬ, добавить информацию о преподавателе
#   • calculate_bonus() - рассчитать бонус на основе рейтинга
#     ↳ Рейтинг >= 4.5 → 20% от зарплаты
#     ↳ Рейтинг >= 4.0 → 15% от зарплаты
#     ↳ Рейтинг >= 3.5 → 10% от зарплаты
#     ↳ Рейтинг < 3.5 → 0%
#
# Property:
#   • subjects - только getter (возвращает копию списка)
#   • salary - getter и setter (проверка: salary > 0)
#   • rating - getter и setter (проверка: 1.0 <= rating <= 5.0)
#   • total_salary - вычисляемое свойство (salary + bonus)
#
#
# ТРЕБОВАНИЯ:
# ✅ Три класса с наследованием: Person → Student, Person → Teacher
# ✅ Использовать super().__init__() в дочерних классах
# ✅ Переопределить get_info() в обоих дочерних классах
# ✅ Использовать @property для множества вычисляемых свойств
# ✅ Использовать property с setter для валидации
# ✅ Защищённые атрибуты с одним подчёркиванием
# ✅ Приватный атрибут __id
# ✅ Сложные вычисления (средний балл, стипендия, бонус)
