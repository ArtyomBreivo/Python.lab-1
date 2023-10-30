#Реализуйте программу «Магазин автозапчастей», которая будет включать в себя
#шесть пунктов меню. У вас есть словарь, где ключ – название продукции.
#Значение – список, который содержит состав продукции, цену и кол-во (шт),
#которое есть в магазине.
#1. Просмотр описания: название – описание
#2. Просмотр цены: название – цена.
#3. Просмотр количества: название – количество.
#4. Всю информацию.
#5. Покупка
#В пункте «Покупка» необходимо совершить покупку, с клавиатуры вводите название продукции
#и его кол-во, n – выход из программы.
#Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке
shop_inventory = {
    'Масло моторное': ['Моторное масло для автомобилей', 25.0, 50],
    'Фильтр масляный': ['Фильтр масляный для автомобилей', 5.0, 100],
    'Свечи зажигания': ['Свечи зажигания для двигателя', 2.0, 200],
    'Тормозные колодки': ['Тормозные колодки для передних колес', 15.0, 30],
    'Антифриз': ['Антифриз для системы охлаждения', 8.0, 40],
    'Воздушный фильтр': ['Воздушный фильтр для автомобильного двигателя', 4.0, 60],
}


def view_description():
    product_name = input("Введите название продукции: ")
    if product_name in shop_inventory:
        print(f"Описание: {shop_inventory[product_name][0]}")
    else:
        print("Продукция не найдена.")


def view_price():
    product_name = input("Введите название продукции: ")
    if product_name in shop_inventory:
        print(f"Цена: {shop_inventory[product_name][1]} рублей за штуку")
    else:
        print("Продукция не найдена.")


def view_quantity():
    product_name = input("Введите название продукции: ")
    if product_name in shop_inventory:
        print(f"Количество: {shop_inventory[product_name][2]} штук")
    else:
        print("Продукция не найдена.")


def view_all():
    for product, info in shop_inventory.items():
        description, price, quantity = info
        print(f"Продукция: {product}")
        print(f"Описание: {description}")
        print(f"Цена: {price} рублей за штуку")
        print(f"Количество: {quantity} штук")
        print()


def make_purchase():
    total_cost = 0
    while True:
        product_name = input("Введите название продукции (n для завершения): ")
        if product_name == 'n':
            break
        if product_name in shop_inventory:
            quantity_to_buy = int(input(f"Введите количество {product_name}: "))
            if quantity_to_buy <= shop_inventory[product_name][2]:
                cost = quantity_to_buy * shop_inventory[product_name][1]
                total_cost += cost
                shop_inventory[product_name][2] -= quantity_to_buy
                print(f"Вы купили {quantity_to_buy} штук {product_name} за {cost} рублей.")
            else:
                print("Недостаточно товара на складе.")
        else:
            print("Продукция не найдена.")
    print(f"Общая стоимость покупки: {total_cost} рублей")


while True:
    print("Меню:")
    print("1. Просмотр описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        view_description()
    elif choice == '2':
        view_price()
    elif choice == '3':
        view_quantity()
    elif choice == '4':
        view_all()
    elif choice == '5':
        make_purchase()
    elif choice == '6':
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите существующий пункт меню.")
