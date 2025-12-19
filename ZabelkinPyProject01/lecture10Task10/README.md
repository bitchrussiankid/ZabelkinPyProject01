**Задача 5. Множественное наследование (Camera + GPS → SmartCamera)**

Создай **два независимых родительских класса**:

1. **Класс `Camera` (Камера):**
   - Атрибут: `resolution` (разрешение в мегапикселях)
   - Метод: `take_photo()` — возвращает `"Фото [resolution] Мп сделано"`

2. **Класс `GPS` (Навигатор):**
   - Атрибут: `has_gps` (есть ли GPS, булево значение)
   - Метод: `get_location()` — если `has_gps` True, возвращает `"Координаты получены"`, иначе `"GPS недоступен"`

Теперь создай **класс `SmartCamera`**, который наследует от **обоих родителей**:
- Добавляет атрибуты: `brand`, `model`
- Метод `device_info()` — возвращает `"[brand] [model] с камерой [resolution] Мп"`

**Требования:**
1. Используй множественное наследование: `class SmartCamera(Camera, GPS):`
2. Конструктор `SmartCamera` должен инициализировать атрибуты всех родителей
3. Покажи, как работают методы обоих родителей

**Пример:**
```python
camera = SmartCamera(brand="Canon", model="PowerShot", resolution=20, has_gps=True)

print(camera.take_photo())    # Фото 20 Мп сделано
print(camera.get_location())  # Координаты получены
print(camera.device_info())   # Canon PowerShot с камерой 20 Мп
```

**Подсказка:** В конструкторе явно вызови конструкторы обоих родителей:
```python
def __init__(self, brand, model, resolution, has_gps):
    Camera.__init__(self, resolution)
    GPS.__init__(self, has_gps)
    self.brand = brand
    self.model = model
```
