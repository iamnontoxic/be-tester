# 1. Откройте http://practice.automationtesting.in/
# 2. Проскролльте страницу вниз на 600 пикселей
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# 4. Нажмите на вкладку "REVIEWS"
# 5. Поставьте 5 звёзд
# 6. Заполните поле "Review" сообщением: "Nice book!"
# 7. Заполните поле "Name"
# 8. Заполните "Email"
# 9. Нажмите на кнопку "SUBMIT"

##########Home: добавление комментария
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get('http://practice.automationtesting.in/')
print('# 1. Открыли http://practice.automationtesting.in/')

driver.execute_script("window.scrollBy(0, 600);")
print('# 2. Проскроллили страницу вниз на 600 пикселей')

read_more_selenium = driver.find_element(By.CSS_SELECTOR,
    'a[href="http://practice.automationtesting.in/product/selenium-ruby/"]:nth-child(2)')
read_more_selenium.click()
print('# 3. Нажали на кнопку "READ MORE"')

reviews = driver.find_element(By.CSS_SELECTOR, '[href="#tab-reviews"]')
reviews.click()
print('# 4. Нажали на вкладку "REVIEWS"')

driver.execute_script("window.scrollBy(0, 800);")
print('Прокрутили страницу на 800 пикселей')


five_stars = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="star-5"]')))
five_stars.click()
print('# 5. Поставили 5 звёзд')

text_review = driver.find_element(By.CSS_SELECTOR, '[id="comment"]')
text_review.send_keys("Nice book!")
print('# 6. Заполнили поле "Review" сообщением: "Nice book!"')

name_reviewer = driver.find_element(By.CSS_SELECTOR, '[id="author"]')
name_reviewer.send_keys('Evgeny')
print('# 7. Заполнили поле "Name"')

email_reviewer = driver.find_element(By.CSS_SELECTOR, '[id="email"]')
email_reviewer.send_keys('random+test@mail.ru')
print('# 8. Заполнили "Email"')

submit = driver.find_element(By.CSS_SELECTOR, '[id="submit"]')
submit.click()
print('# 9. Нажали на кнопку "SUBMIT"')

driver.quit()
