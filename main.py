"""
Поменяйте значения переменных a и b в списке местами
"""


def power():
    a = 3
    b = "Буква"
    a, b = b, a
    print("a= {0}, b=  {1}" .format(a, b))


if __name__ == '__main__':
    power()


