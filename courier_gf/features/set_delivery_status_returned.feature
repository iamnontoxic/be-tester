Feature: Перевести доставку в статус "возврат на склад"
  # Enter feature description here

  Scenario: Установка доставки в статус "возврат на склад"
    Given Создание обращения в КЦ
    And Создание заказа
    And Запланировать доставку
    And Закрыть обращение
    And Назначить курьера на доставку
    And Выдать коробку курьеру
    When Запрос "Возрат на склад"
    #Then Доставка в статусе "Возврат на склад"