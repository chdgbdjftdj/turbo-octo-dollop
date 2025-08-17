# Базовый класс
class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        raise NotImplementedError("Метод area() должен быть переопределен в производном классе")
    
    def info(self):
        print(f"Фигура цвета {self.color}")

# Производный класс 1
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def info(self):
        super().info()
        print(f"Это круг с радиусом {self.radius}")

# Производный класс 2
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def info(self):
        super().info()
        print(f"Это прямоугольник {self.width}x{self.height}")

# Тестовая программа
def main():
    # Создаем объекты
    circle = Circle("красный", 5)
    rectangle = Rectangle("синий", 4, 6)
    
    # Демонстрация работы методов
    print("\nДемонстрация работы с кругом:")
    circle.info()
    print(f"Площадь круга: {circle.area()}")
    
    print("\nДемонстрация работы с прямоугольником:")
    rectangle.info()
    print(f"Площадь прямоугольника: {rectangle.area()}")
    
    # Полиморфизм в действии
    shapes = [circle, rectangle]
    print("\nИтерация по списку фигур:")
    for shape in shapes:
        shape.info()
        print(f"Площадь: {shape.area()}\n")

if __name__ == "__main__":
    main()