# Техническое задание.
***
### Цель проекта
Программа-обозреватель NFT коллекции, их  айтемов, отслеживать изменения по коллекции,
такие как:
- Предложения покупка/продажа
- Наличие на биржах

Гибкая система отслеживания по цене которую можно настроить по вашему усмотрению.

Информирование происходит прогрессивным способом - в мессенджер, с линком на объект.

#### UPD

 - В данном случае определяется, нужен веб или только ТГ-бот или все сразу использовать.
 - 26.04.22.
   - Определиться с фреймворком для API (Flask, DRF, FastAPI)
   - Клиентские запросы будут находиться в очереди посредством Redis/Celery

### Описание системы

Система и ее функциональный блоки:

- Интеграция со сторонними API для отслеживания
- Интеграция с telegram для оповещения а также для установки пользовательских параметров
  - уведомления
  - интуитивный подход для ввода/изменения параметров
- Легковесный веб

### Интеграция со сторонними API

Интеграция для отслеживания покупок/продаж NFT на интересующей бирже

***
### Интеграция с telegram

Используется для информирование а также для пользовательских настроек.
Настройки могут быть вида: Информировать если по коллекции 0x1(monkey) появилась предложение продажи
если цена меньше 1 eth.
Обозревать по данному условию на интересующих сайтах юзера.
Также добавление/изменение самих коллекций которые отслеживаются.
#### Функционал
- keyboards - кнопки
- handlers - обработчики
- 
- старт - командой /start
- Кнопки KeyboardButton()
  - I) Добавить коллекцию btn1
    - Добавляет коллекию по адрессу или наименованию на мониторинг, закрепляется за юзером по тг нику @username
  - II) Далее появляется следующее меню для реализации условия (пока что одно условие если floor_price < interesting_price)
***
### Легковесный веб
Также решение для добавления/изменения условий по отслеживанию коллекции,
также добавление/изменение самих коллекций которые отслеживаются.


### Стек технологий

- Python
- API Framework
- aiogram
  - uvloop
  - ujson
  - cchardet
  - aiodns
  - aiohttp[speedups]
- postgresql или какое-нибудь другое решение
  - orm sqalchemy or peewee
- Redis/Celery