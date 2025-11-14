import sqlite3

print("=== СОЗДАНИЕ БАЗЫ ДАННЫХ ===")

def create_database():
    try:
        # Подключаемся к базе
        conn = sqlite3.connect('company.db')
        cursor = conn.cursor()
        print("✓ База данных подключена")
        
        # Создаём таблицу отделов
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                manager TEXT
            )
        ''')
        print("✓ Таблица 'departments' создана")
        
        # Создаём таблицу сотрудников
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT,
                department_id INTEGER,
                salary REAL,
                hire_date TEXT,
                FOREIGN KEY (department_id) REFERENCES departments(id)
            )
        ''')
        print("✓ Таблица 'employees' создана")
        
        # Очищаем старые данные
        cursor.execute("DELETE FROM employees")
        cursor.execute("DELETE FROM departments")
        
        # Добавляем отделы
        departments = [
            ('IT отдел', 'Иванов И.И.'),
            ('Бухгалтерия', 'Петрова П.П.'),
            ('Отдел продаж', 'Сидоров С.С.')
        ]
        
        for dept in departments:
            cursor.execute("INSERT INTO departments (name, manager) VALUES (?, ?)", dept)
        print("✓ Отделы добавлены")
        
        # Добавляем сотрудников
        employees = [
            ('Алексей Козлов', 'Программист', 1, 80000, '2023-01-15'),
            ('Мария Новикова', 'Бухгалтер', 2, 60000, '2022-03-10'),
            ('Дмитрий Волков', 'Менеджер', 3, 70000, '2023-11-01')
        ]
        
        for emp in employees:
            cursor.execute("INSERT INTO employees (name, position, department_id, salary, hire_date) VALUES (?, ?, ?, ?, ?)", emp)
        print("✓ Сотрудники добавлены")
        
        # Сохраняем изменения
        conn.commit()
        conn.close()
        print("✓ База данных успешно создана!")
        
    except Exception as e:
        print("✗ ОШИБКА:", e)

if __name__ == "__main__":
    create_database()