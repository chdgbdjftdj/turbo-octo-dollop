-- БАЗА ДАННЫХ "ТУРИЗМ"
-- Создано: [Ваше ФИО]
-- Дата: [Сегодняшняя дата]

-- 1. Таблицы-справочники
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY AUTOINCREMENT,
    country_name TEXT NOT NULL,
    visa_required BOOLEAN DEFAULT 0
);

CREATE TABLE tour_types (
    type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL,
    description TEXT
);

CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    passport_data TEXT
);

-- 2. Таблицы переменной информации
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    country_id INTEGER,
    tour_type_id INTEGER,
    order_date TEXT NOT NULL,
    start_date TEXT,
    end_date TEXT,
    total_price REAL,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (country_id) REFERENCES countries(country_id),
    FOREIGN KEY (tour_type_id) REFERENCES tour_types(type_id)
);

CREATE TABLE order_services (
    order_id INTEGER,
    service_id INTEGER,
    quantity INTEGER DEFAULT 1,
    PRIMARY KEY (order_id, service_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- 3. Тестовые данные
INSERT INTO countries (country_name, visa_required) VALUES 
('Турция', 0), ('Египет', 1), ('Таиланд', 1), ('ОАЭ', 0);

INSERT INTO tour_types (type_name, description) VALUES 
('Пляжный отдых', 'Отдых на море с отелем'),
('Экскурсионный', 'Обзорные туры по достопримечательностям');

INSERT INTO services (service_name, price) VALUES 
('Страховка', 5000.00), ('Трансфер', 3000.00), ('Экскурсия', 7000.00);

INSERT INTO clients (full_name, phone, email, passport_data) VALUES 
('Иванов Иван', '+79161234567', 'ivanov@mail.ru', '4510 123456'),
('Петрова Мария', '+79167654321', 'petrova@yandex.ru', '4511 654321');

INSERT INTO orders (client_id, country_id, tour_type_id, order_date, total_price) VALUES 
(1, 1, 1, '2024-01-15', 120000.00),
(2, 2, 2, '2024-01-16', 185000.00);

INSERT INTO order_services (order_id, service_id, quantity) VALUES 
(1, 1, 1), (1, 2, 1), (2, 1, 1), (2, 3, 2);