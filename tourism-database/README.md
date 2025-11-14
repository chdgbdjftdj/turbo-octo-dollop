# База данных "Туризм"

## Описание проекта
Проектирование реляционной базы данных для туристического агентства.

## Структура базы данных
- **Таблицы-справочники (4):** 
  - countries (страны)
  - tour_types (типы туров) 
  - services (дополнительные услуги)
  - clients (клиенты)
- **Таблицы переменной информации (2):**
  - orders (заказы)
  - order_services (связь заказов и услуг)

## Связи между таблицами
- orders.client_id → clients.client_id
- orders.country_id → countries.country_id
- orders.tour_type_id → tour_types.type_id
- order_services.order_id → orders.order_id  
- order_services.service_id → services.service_id

## Файлы проекта
- `tourism_database.sql` - полный SQL-код базы данных
- Скриншоты работы базы данных

## Используемые технологии
- SQLite
- Онлайн-редактор SQLiteOnline
