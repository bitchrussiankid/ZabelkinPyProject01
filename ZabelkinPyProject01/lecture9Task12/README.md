## **Задача 5: Shop и Product (финальная)**

**Цель:** Создать систему, где **объекты двух классов активно взаимодействуют**, с проверкой условий и управлением состоянием.

**Класс `Product`:**
- `__init__(self, name, price, quantity)` — название, цена, количество на складе
- `update_quantity(self, amount)` — изменить количество (может быть отрицательным для продажи)
- `display_info(self)` — вернуть строку с информацией о товаре

**Класс `Shop`:**
- `__init__(self, name)` — название магазина
- `products` — словарь товаров `{name: product_object}`
- `add_product(self, product)` — добавить товар в магазин
- `sell_product(self, product_name, quantity)` — продать товар:
  - Проверить, есть ли товар
  - Проверить, хватает ли количества
  - Уменьшить количество у товара
  - Вернуть стоимость продажи
- `restock_product(self, product_name, quantity)` — пополнить склад
- `display_inventory(self)` — показать все товары

**Требования:**
1. Создай несколько товаров (минимум 3)
2. Создай магазин "TechStore"
3. Добавь товары в магазин
4. Продемонстрируй:
   - Продажу товара (успешную)
   - Попытку продажи при недостатке товара
   - Пополнение склада
5. Выведи итоговый инвентарь

**Пример вывода:**
```
TechStore inventory:
1. Laptop - $1000, Quantity: 5
2. Mouse - $50, Quantity: 10

Sold 2 Laptops. Revenue: $2000
Error: Not enough Smartphones in stock
Restocked Smartphones. New quantity: 8

Final inventory:
1. Laptop - $1000, Quantity: 3
2. Mouse - $50, Quantity: 10
3. Smartphone - $800, Quantity: 8
```