from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Подключаемся к базе
    conn = sqlite3.connect('company.db')
    conn.row_factory = sqlite3.Row  # Чтобы результаты были как словари
    cursor = conn.cursor()
    
    # Получаем всех сотрудников с отделами
    cursor.execute('''
        SELECT e.name, e.position, e.salary, e.hire_date, d.name as department_name
        FROM employees e
        JOIN departments d ON e.department_id = d.id
        ORDER BY e.name
    ''')
    
    employees = cursor.fetchall()
    conn.close()
    
    # Передаём данные в шаблон
    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    # Создаём базу если её нет
    if not os.path.exists('company.db'):
        import database
        database.create_database()
    
    print("Запускаем веб-приложение...")
    print("Открой в браузере: http://localhost:5000")
    app.run(debug=True)