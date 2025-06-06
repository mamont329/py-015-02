class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Словарь: товар -> цена

    def add_item(self, item_name, price):
        """Добавить товар в ассортимент"""
        self.items[item_name] = price
        print(f"Товар '{item_name}' с ценой {price} добавлен в магазин '{self.name}'.")

    def remove_item(self, item_name):
        """Удалить товар из ассортимента"""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён из магазина '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")

    def get_price(self, item_name):
        """Получить цену товара по названию"""
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """Обновить цену товара"""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price} в магазине '{self.name}'.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'.")

    def __str__(self):
        """Вывод информации о магазине"""
        items_list = ', '.join([f"{item}: {price}" for item, price in self.items.items()]) or "Нет товаров"
        return f"Магазин '{self.name}', Адрес: {self.address}, Ассортимент: {items_list}"

# Создаем три магазина
store1 = Store("Фруктовый Рай", "ул. Ленина, д. 10")
store2 = Store("Бакалея у дома", "ул. Пушкина, д. 5")
store3 = Store("Супермаркет XXL", "пр. Мира, д. 20")

# Добавляем товары в каждый магазин
store1.add_item("яблоки", 0.6)
store1.add_item("бананы", 0.8)

store2.add_item("сахар", 1.2)
store2.add_item("соль", 0.5)

store3.add_item("вода", 0.9)
store3.add_item("хлеб", 1.1)

# Вывод информации о магазинах
print("\n--- Информация о магазинах ---")
print(store1)
print(store2)
print(store3)

# Тестируем методы одного из магазинов (например store1)
print("\n--- Тестирование методов store1 ---")

# Добавляем новый товар
store1.add_item("апельсины", 0.7)

# Обновляем цену
store1.update_price("бананы", 0.75)

# Запрашиваем цену
print("Цена яблок:", store1.get_price("яблоки"))

# Удаляем товар
store1.remove_item("апельсины")

# Вывод финального состояния
print("\nИтоговый список товаров в store1:")
print(store1)