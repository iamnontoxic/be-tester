Feature: Авторизации курьера
  # Enter feature description here

  Scenario: Авторизация
    Given Запрос на авторизацию
    Then Получение токена
    And Проверка получения токена