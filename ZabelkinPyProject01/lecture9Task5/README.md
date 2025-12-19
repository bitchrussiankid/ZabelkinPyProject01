Создайте класс Calculator (Калькулятор) для демонстрации работы параметра self.

Требования:

Конструктор должен инициализировать атрибут result со значением 0

Добавьте четыре метода:

add(self, x) - добавляет x к result

subtract(self, x) - вычитает x из result

multiply(self, x) - умножает result на x

get_result(self) - возвращает текущее значение result

Продемонстрируйте, что self обеспечивает доступ к атрибутам конкретного объекта

Пример использования:

calc = Calculator()
calc.add(5)
calc.multiply(3)
calc.subtract(2)
print(calc.get_result())  # Должно вывести: 13