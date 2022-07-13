# # 1. Откройте http://practice.automationtesting.in/
# # 2. Нажмите на вкладку "My Account Menu"
# # 3. В разделе "Register", введите email для регистрации
# # 4. В разделе "Register", введите пароль для регистрации
# # • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# # • почту и пароль сохраните, потребуюутся в дальнейшем
# # 5. Нажмите на кнопку "Register"
#
# ########Registration_login: регистрация аккаунта###############
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
# my_account = driver.find_element(By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/my-account/"]')
# my_account.click()
# print('# 2. Нажали на вкладку "My Account Menu"')
#
# email_registration = driver.find_element(By.CSS_SELECTOR, '[id="reg_email"]')
# email_registration.send_keys(f'rantest954@mail.com')
# print('# 3. В разделе "Register", ввели email для регистрации')
#
# password_registration = driver.find_element(By.CSS_SELECTOR, '[id="reg_password"]')
# password_registration.send_keys(f'rndtest954!p')
# print('# 4. В разделе "Register", ввели пароль для регистрации')
#
# # Кнопка регистрации не кликабельно, разобраться как исправить
# register_button = WebDriverWait(driver, 20).until_not(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="woocomerce-FormRow form-row"]>[type="submit"]')))
# register_button_click = driver.find_element(By.CSS_SELECTOR, '[class="woocomerce-FormRow form-row"]>[type="submit"]')
# print('# 5. Нажмите на кнопку "Register"')











# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
# 5. Нажмите на кнопку "Login"
# 6. Добавьте проверку, что на странице есть элемент "Logout"
# ##########Registration_login: логин в систему############
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get('http://practice.automationtesting.in/')
# print('# 1. Открыли http://practice.automationtesting.in/')
#
# my_account = driver.find_element(By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/my-account/"]')
# my_account.click()
# print('# 2. Нажали на вкладку "My Account Menu"')
#
# email_registration = driver.find_element(By.CSS_SELECTOR, '[id="username"]')
# email_registration.send_keys('rantest954@mail.com')
# print('# 3. В разделе "Login", ввели email для логина')
#
# password_registration = driver.find_element(By.CSS_SELECTOR, '[id="password"]')
# password_registration.send_keys(f'rndtest954!p')
# print('# 4. В разделе "Login", ввели пароль для логина')
#
# login = driver.find_element(By.CSS_SELECTOR, '[name="login"]')
# login.click()
# print('# 5. Нажали на кнопку "Login"')
#
# sign_out = driver.find_element(By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/my-account/customer-logout/"]')
# check_sign_out = sign_out.text
# print(f'# 6. Добавили проверку, что на странице есть элемент "Logout"')
# assert check_sign_out == 'Logout', f'Элемент имеет текст {check_sign_out}, а должен "Logout"'
#
# driver.quit()





