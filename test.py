class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        if isinstance(price, float) or isinstance(price, int):
            self.items[item_name] = price
        else:
            raise ValueError("Цена должна быть числом")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            if isinstance(new_price, float) or isinstance(new_price, int):
                self.items[item_name] = new_price
            else:
                raise ValueError("Новая цена должна быть числом")
        else:
            print(f"Товар '{item_name}' не найден.")

# Магазин №1: Продуктовый магазин "У дома"
store_1 = Store('Продукты У дома', 'Москва, ул. Красная, д. 10')
store_1.add_item('молоко', 70)
store_1.add_item('хлеб', 35)
store_1.add_item('сахар', 50)

# Магазин №2: Спортивный магазин "Форвард"
store_2 = Store('Спорт Форвард', 'Санкт-Петербург, Невский проспект, д. 50')
store_2.add_item('кроссовки', 3500)
store_2.add_item('шорты', 1200)
store_2.add_item('футболка', 1500)

# Магазин №3: Цветочный магазин "Цветик-Семицветик"
store_3 = Store('Цветик-Семицветик', 'Екатеринбург, ул. Пушкина, д. 20')
store_3.add_item('розы', 250)
store_3.add_item('тюльпаны', 150)
store_3.add_item('лилии', 300)


# Выбираем магазин "Цветик-Семицветик"
store_test = store_3

# Начальное состояние магазина
print(f"Начальный ассортимент магазина {store_test.name}: {store_test.items}")

# Добавляем новый товар "Георгины"
store_test.add_item('георгины', 180)
print(f"\nАссортимент после добавления георгин: {store_test.items}")

# Обновляем цену тюльпанов
store_test.update_price('тюльпаны', 160)
print(f"\nАссортимент после изменения цены тюльпанов: {store_test.items}")

# Просмотр цены нескольких товаров
print("\nЦены товаров:")
print(f"- Роз: {store_test.get_price('розы')}")      # Должно вернуть 250
print(f"- Георгины: {store_test.get_price('георгины')}")  # Должно вернуть 180
print(f"- Хризантемы: {store_test.get_price('хризантемы')}")  # Должно вернуть None

# Удаляем лилии
store_test.remove_item('лилии')
print(f"\nАссортимент после удаления лилий: {store_test.items}")






