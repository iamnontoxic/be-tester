# # 1. Откройте http://practice.automationtesting.in/
# # 2. Залогиньтесь
# # 3. Нажмите на вкладку "Shop"
# # 4. Откройте книгу "HTML 5 Forms"
# # 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
#
# ############# Shop: отображение страницы товара###########
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://practice.automationtesting.in/')
# print('# 1. Открыли http://practice.automationtesting.in/')
#
# # Переходим во вкладку My account для логина
# my_account = driver.find_element(By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/my-account/"]').click()
#
# # Вводим логин
# email_registration = driver.find_element(By.CSS_SELECTOR, '[id="username"]')
# email_registration.send_keys('rantest954@mail.com')
#
# # Вводим пароль
# password_registration = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
# password_registration.send_keys(f'rndtest954!p')
#
# # Нажимаем кнопку Login
# login = driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()
# print('# 2. Залогинились')
#
# # Переходим во вкладку Shop
# shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a').click()
# print('# 3. Нажали на вкладку "Shop"')
#
# # Открываем книгу "HTML 5 Forms"
# book_html5 = driver.find_element(By.CSS_SELECTOR, 'img[title="Mastering HTML5 Forms"]').click()
# print('# 4. Открыли книгу "HTML 5 Forms"')
#
# # Тест на заголок 'HTML5 Forms'
# test_header_book = driver.find_element(By.CSS_SELECTOR, 'h1[itemprop="name"]').text
# assert test_header_book == 'HTML5 Forms', f'Ожидали HTML5 Forms, а получили {test_header_book}'
# print('# 5. Добавили тест, что заголовок книги назвается: "HTML5 Forms"')















# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте категорию "HTML"
# 5. Добавьте тест, что отображается три товара

# ##############Shop: количество товаров в категории#############
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://practice.automationtesting.in/')
# print('# 1. Открыли http://practice.automationtesting.in/')
#
# # Переходим во вкладку My account для логина
# my_account = driver.find_element(By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/my-account/"]').click()
#
# # Вводим логин
# email_registration = driver.find_element(By.CSS_SELECTOR, '[id="username"]')
# email_registration.send_keys('rantest954@mail.com')
#
# # Вводим пароль
# password_registration = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
# password_registration.send_keys(f'rndtest954!p')
#
# # Нажимаем кнопку Login
# login = driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()
# print('# 2. Залогинились')
#
# # Переходим во вкладку Shop
# shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a').click()
# print('# 3. Нажали на вкладку "Shop"')
#
# # Открываем категори HTML
# html_category = driver.find_element(By.CSS_SELECTOR, 'li.cat-item-19>a').click()
# print('# 4. Открыли категорию "HTML"')
#
# # Проверяем, что товара 3 шт
# test_count_elements = len(driver.find_elements(By.CSS_SELECTOR, '.products>li'))
# assert test_count_elements == 3, f'Ожидаем 3 элемента, а их {test_count_elements}'
# print('# 5. Добавили тест, что отображается три товара')
#
# driver.quit()












################Shop: сортировка товаров################
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
# • Используйте проверку по value
# 5. Отсортируйте товары по цене от большей к меньшей
# • в селекторах используйте класс Select
# 6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# • Используйте проверку по value

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://practice.automationtesting.in/')
# print('# 1. Открыли http://practice.automationtesting.in/')
#
# # Переходим во вкладку My account для логина
# my_account = driver.find_element(By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/my-account/"]').click()
#
# # Вводим логин
# email_registration = driver.find_element(By.CSS_SELECTOR, '[id="username"]')
# email_registration.send_keys('rantest954@mail.com')
#
# # Вводим пароль
# password_registration = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
# password_registration.send_keys(f'rndtest954!p')
#
# # Нажимаем кнопку Login
# login = driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()
# print('# 2. Залогинились')
#
# # Переходим во вкладку Shop
# shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a').click()
# print('# 3. Нажали на вкладку "Shop"')
#
# # Проверяем, что селектор по умолчанию
# select_default = driver.find_element(By.CSS_SELECTOR, '[value="menu_order"]')
# test_select_default = select_default.get_attribute('selected')
# assert test_select_default == 'true'
# print('# 4. Добавили тест, что в селекторе выбран вариант сортировки по умолчанию')
#
# # Сортируем товары по цене от большей к меньшей
# sort_high_to_low = Select(driver.find_element(By.CSS_SELECTOR, '.orderby')).select_by_index(5)
# print('# 5. Отсортировали товары по цене от большей к меньшей')
#
# # Объявляем переменную с локатором основного селектора сортировки
# selector = driver.find_element(By.CSS_SELECTOR, '.orderby')
# print('# 6. Объявили переменную с локатором основного селектора сортировки')
#
# # тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# select_high_to_low = driver.find_element(By.CSS_SELECTOR, '[value="price-desc"]')
# test_select_high_to_low = select_high_to_low.get_attribute('selected')
# assert test_select_high_to_low == 'true'
# print('# 7. Добавили тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей')
#
# driver.quit()












#####################Shop: отображение, скидка товара#######################
# 1. Откройте http://practice.automationtesting.in/
# 2. Залогиньтесь
# 3. Нажмите на вкладку "Shop"
# 4. Откройте книгу "Android Quick Start Guide"
# 5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
# 6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
# 7. Добавьте явное ожидание и нажмите на обложку книги
# • Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://practice.automationtesting.in/')
# print('# 1. Открыли http://practice.automationtesting.in/')
#
# # Переходим во вкладку My account для логина
# my_account = driver.find_element(By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/my-account/"]').click()
#
# # Вводим логин
# email_registration = driver.find_element(By.CSS_SELECTOR, '[id="username"]')
# email_registration.send_keys('rantest954@mail.com')
#
# # Вводим пароль
# password_registration = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
# password_registration.send_keys(f'rndtest954!p')
#
# # Нажимаем кнопку Login
# login = driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()
# print('# 2. Залогинились')
#
# # Переходим во вкладку Shop
# shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a').click()
# print('# 3. Нажали на вкладку "Shop"')
#
# # Android book
# android_book = driver.find_element(By.CSS_SELECTOR, 'img[title="Android Quick Start Guide"]').click()
# print('# 4. Открыли книгу "Android Quick Start Guide"')
#
# # old price
# price_old = driver.find_element(By.CSS_SELECTOR, 'del > span').text
# assert price_old == '₹600.00'
# print('# 5. Добавили тест, что содержимое старой цены = "₹600.00" # используйте assert')
#
# # new price
# price_new = driver.find_element(By.CSS_SELECTOR, 'ins > span').text
# assert price_new == '₹450.00'
# print('# 6. Добавили тест, что содержимое новой цены = "₹450.00" # используйте assert')
#
# # image android book
# image_book = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '.images')))
# image_book.click()
# print('# 7. Добавили явное ожидание и нажмите на обложку книги')
# close_image = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close')))
# close_image.click()
# print('# 8. Добавили явное ожидание и закрыли предпросмотр нажав на крестик (кнопка вверху справа)')
#
# driver.quit()







####################Shop: проверка цены в корзине##############
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
# 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
# • Используйте для проверки assert
# 5. Перейдите в корзину
# 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://practice.automationtesting.in/')
# print('# 1. Открыли http://practice.automationtesting.in/')
#
# # Переходим во вкладку Shop
# shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a').click()
# print('# 2. Нажали на вкладку "Shop"')
#
# html5_book = driver.find_element(By.CSS_SELECTOR, '[href="/shop/?add-to-cart=182"]').click()
# print('# 3. Добавили в корзину книгу "HTML5 WebApp Development"')
# driver.refresh()
#
# count_shoping_cart = driver.find_element(By.CSS_SELECTOR, '.cartcontents')
# amount_shoping_cart = driver.find_element(By.CSS_SELECTOR, 'a > .amount')
# count_shoping_cart_text = count_shoping_cart.text
# amount_shoping_cart_text = amount_shoping_cart.text
#
# assert [count_shoping_cart_text, amount_shoping_cart_text] == ["1 Item", "₹180.00"]
# print('# 4. Добавили тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"')
#
# shoping_cart = driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents').click()
# print('# 5. Перешли в корзину')
#
# subtotal = WebDriverWait(driver, 5).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, 'td[data-title="Subtotal"]>span')))
# subtotal_text = subtotal.text
# print(subtotal_text)
# assert subtotal_text == '₹180.00'
# print('# 6. Используя явное ожидание, проверили что в Subtotal отобразилась стоимость')
#
# total = WebDriverWait(driver, 5).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, 'strong>span')))
# total_text = total.text
# print(total_text)
# assert total_text == '₹189.00'
# print('# 7. Используя явное ожидание, проверили что в Total отобразилась стоимость')
# driver.quit()













######################Shop: работа в корзине########################
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop"
# 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# • Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# • После добавления 1-й книги добавьте sleep
# 4. Перейдите в корзину
# 5. Удалите первую книгу
# • Перед удалением добавьте sleep
# 6. Нажмите на Undo (отмена удаления)
# 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
# • Предварительно очистите поле с помощью локатор_поля.clear()
# 8. Нажмите на кнопку "UPDATE BASKET"
# 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
# 10. Нажмите на кнопку "APPLY COUPON"
# • Перед нажатимем добавьте sleep
# 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://practice.automationtesting.in/')
# print('# 1. Открыли http://practice.automationtesting.in/')
#
# # Переходим во вкладку My account для логина
# my_account = driver.find_element(By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/my-account/"]').click()
#
# # Вводим логин
# email_registration = driver.find_element(By.CSS_SELECTOR, '[id="username"]')
# email_registration.send_keys('rantest954@mail.com')
#
# # Вводим пароль
# password_registration = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
# password_registration.send_keys(f'rndtest954!p')
#
# # Нажимаем кнопку Login
# login = driver.find_element(By.CSS_SELECTOR, '[name="login"]').click()
# print('# 2. Залогинились')
#
# # Переходим во вкладку Shop
# shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a').click()
# print('# 3. Нажали на вкладку "Shop"')
#
# # Скролл на 500 пикселей вниз, тк 300 мало
# driver.execute_script("window.scrollBy(0, 500);")
#
# html5_book = driver.find_element(By.CSS_SELECTOR, '[href="/shop/?add-to-cart=182"]').click()
# time.sleep(1)
#
# js_book = driver.find_element(By.CSS_SELECTOR, '[href="/shop/?add-to-cart=180"]').click()
# print('# 3. Добавили в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"')
#
# shoping_cart = driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents').click()
# print('# 4. Перешли в корзину')
#
# time.sleep(1)
# remove_html_book = driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]').click()
# print('# 5. Удалили первую книгу')
#
# undo_remove = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.woocommerce-message > a'))).click()
# print('# 6. Нажали на Undo (отмена удаления)')
#
# count_js_book = driver.find_element(By.XPATH, '//input[@title="Qty"][1]')
# clear_count_js_book = count_js_book.clear()
# add_count_js_book = count_js_book.send_keys(3)
# print('# 7. В Quantity увеличили количесто товара до 3 шт для "JS Data Structures and Algorithm“')
#
# update_busket = driver.find_element(By.CSS_SELECTOR, 'input[name="update_cart"]').click()
# print('# 8. Нажали на кнопку "UPDATE BASKET"')
#
# value_count_js_book = count_js_book.get_attribute('value')
#
# assert value_count_js_book == '3'
# print('# 9. Добавили тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3')
#
# time.sleep(1)
# apply_coupon = driver.find_element(By.CSS_SELECTOR, 'input[name="apply_coupon"]').click()
# print('# 10. Нажали на кнопку "APPLY COUPON"')
#
# error_coupon = WebDriverWait(driver, 5).until(
#     EC.visibility_of_element_located((By.CSS_SELECTOR, '.woocommerce-error > li')))
# error_coupon_text = error_coupon.text
#
# assert error_coupon_text == "Please enter a coupon code."
# print('# 11. Добавили тест, что возникло сообщение: "Please enter a coupon code."')
#
# driver.quit()










#######################Shop: покупка товара######################
# 1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
# 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
# 3. Добавьте в корзину книгу "HTML5 WebApp Development"
# 4. Перейдите в корзину
# 5. Нажмите "PROCEED TO CHECKOUT"
# • Перед нажатием, добавьте явное ожидание
# 6. Заполните все обязательные поля
# • Перед заполнением first name, добавьте явное ожидание
# • Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
# • Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
# 7. Выберите способ оплаты "Check Payments"
# • Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
# 8. Нажмите PLACE ORDER
# 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
# 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://practice.automationtesting.in/')
print('# 1. Открыли http://practice.automationtesting.in/')

# Переходим во вкладку Shop
shop = driver.find_element(By.CSS_SELECTOR, '#menu-item-40 > a').click()
print('# 2. Нажали на вкладку "Shop"')

# # Скролл на 300 пикселей вниз
driver.execute_script("window.scrollBy(0, 300);")
html5_book = driver.find_element(By.CSS_SELECTOR, '[href="/shop/?add-to-cart=182"]').click()
print('# 3. Добавили в корзину книгу "HTML5 WebApp Development"')
time.sleep(2)
shoping_cart = driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents').click()
print('# 4. Перешли в корзину')

checkout_button = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.wc-proceed-to-checkout>a')))
checkout_button.click()
print('# 5. Нажали "PROCEED TO CHECKOUT"')

first_name = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#billing_first_name')))
first_name.send_keys('Evgeny')
last_name = driver.find_element(By.CSS_SELECTOR, '#billing_last_name').send_keys('Goryunov')
email_input = driver.find_element(By.CSS_SELECTOR, '[name="billing_email"]').send_keys('asdqwdfqv@mail.ru')
phone_number = driver.find_element(By.CSS_SELECTOR, '#billing_phone').send_keys('88009998877')
driver.execute_script("window.scrollBy(0, 300);")
country = driver.find_element(By.CSS_SELECTOR, '.select2-choice').click()
country_input = driver.find_element(By.CSS_SELECTOR, '.select2-input').send_keys('Russia')
country_select_first = driver.find_element(By.CSS_SELECTOR, '#select2-results-1>li').click()
address = driver.find_element(By.CSS_SELECTOR, '[name="billing_address_1"]').send_keys('Pushkina')
city = driver.find_element(By.CSS_SELECTOR, '[name="billing_city"]').send_keys('Moscow')
state = driver.find_element(By.CSS_SELECTOR, '[name="billing_state"]').send_keys('Moscow')
postcode = driver.find_element(By.CSS_SELECTOR, '[name="billing_postcode"]').send_keys('123456')
driver.execute_script("window.scrollBy(0, 600);")
print('# 6. Заполнли все обязательные поля')

time.sleep(2)
check_payments = driver.find_element(By.CSS_SELECTOR, '#payment_method_cheque').click()
print('# 7. Выбрали способ оплаты "Check Payments"')

place_order = driver.find_element(By.CSS_SELECTOR, '#place_order').click()
print('# 8. Нажали PLACE ORDER')

thanks_message = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received')))
thanks_message_text = thanks_message.text
assert thanks_message_text == 'Thank you. Your order has been received.'
print('# 9. Используя явное ожидание, проверили что отображается надпись "Thank you. Your order has been received."')

payment_method = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'tfoot>tr:nth-child(3)>td')))
payment_method_text = payment_method.text
assert payment_method_text == 'Check Payments'
print('# 10. Используя явное ожидание, проверили что в Payment Method отображается текст "Check Payments"')

driver.quit()