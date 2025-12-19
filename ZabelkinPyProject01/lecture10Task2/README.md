**Задача 2. Наследование с животными**

Создай **родительский класс** `Animal` (Животное):
- Атрибуты: `name` (имя), `species` (вид)
- Метод: `make_sound()` — возвращает строку `"Some generic animal sound"`

Создай **дочерний класс** `Dog` (Собака), который наследует от `Animal`:
- Добавляет атрибут: `breed` (порода)
- **Переопределяет** метод `make_sound()` — возвращает `"Woof! Woof!"`
- Добавляет новый метод: `fetch()` — возвращает `"[имя] is fetching the ball!"`

**Требования:**
1. Используй наследование: `class Dog(Animal):`
2. В конструкторе `Dog` используй `super().__init__()` для инициализации `name` и `species`
3. `species` для всех собак должен быть `"Canine"` (можно передавать фиксированно)

**Пример:**
```python
animal = Animal("Generic", "Unknown")
dog = Dog("Rex", "German Shepherd")

print(animal.make_sound())  # Some generic animal sound
print(dog.make_sound())     # Woof! Woof!
print(dog.fetch())          # Rex is fetching the ball!
print(f"Species: {dog.species}")  # Canine
```

**Подсказка:** При создании `Dog` передавай `species="Canine"` в родительский конструктор.