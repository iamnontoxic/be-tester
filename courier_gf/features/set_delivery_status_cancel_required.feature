Feature: Перевести доставку в статус "запрос на отмену"
  # Enter feature description here

  Scenario: Установка доставки в статус "запрос на отмену"
    Given Создание заказа, планирование, назначение курьера и выдача коробки
    When Запрос "запрос на отмену"
    Then Доставка в статусе "запрос на отмену"