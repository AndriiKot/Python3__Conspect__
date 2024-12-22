
Example_01 = 1

if Example_01:
    import re
    s = "some string"
    result = re.split(r'\s+', s)
    print(result)
    # s.is -> tab tab information about methods
    # s.spli -> tab tab information about methods
    # s.split(       s.splitlines()  )

Example_02 = 2

if Example_02:
    # 1. Использование `readline` для сохранения истории
    # Что бы команды сохранялись между сесиями
    # Создайте или отредактируйте файл `~/.pythonrc.py` и добавьте следующий код:

    '''python
    import atexit
    import os
    import readline

    histfile = os.path.join(os.path.expanduser("~"), ".python_history")

    try:
        readline.read_history_file(histfile)
    except FileNotFoundError:
        pass

    atexit.register(readline.write_history_file, histfile)
    ```

    Теперь, когда вы будете запускать интерактивный режим Python,
    ваши команды будут сохраняться в файле `~/.python_history`.
    Вы сможете использовать клавиши стрелок вверх и вниз для навигации по истории команд.
    '''

    ### 2. Поиск по истории
    ### Ctrl + R


    ### 3. Использование IPython
    '''
    Если вам нужна более функциональная среда интерактивного программирования,
    рассмотрите возможность использования IPython.
    IPython предоставляет мощные средства работы с историей команд, включая поиск.
    Чтобы установить IPython, используйте pip:

    ```bash
    pip install ipython
    ```

    В IPython вы можете использовать `Ctrl + R` для поиска по истории,
    а также команды такие как `%history` для просмотра всей истории команд.
    '''

Example_03 = 3

if Example_03:
    tuple1 = (1, 3, 3,)
    print(tuple1)
    print(type(tuple1))      # <class 'tuple'>
    print(tuple1.count(3))   # 2
    print(tuple1.index(3))   # 1
    print(len(tuple1))       # 3


Example_04 = 4

if Example_04:
    tuple1 = (1, 3, 3,)
    tuple2 = (1, 3, 3,)
    print(tuple1 == tuple2)          # True
    print(id(tuple1) == id(tuple2))  # False sometimes True
    print(tuple1 is tuple2)          # False sometimes True
    print(id(tuple1),id(tuple2))
    print(hex(id(tuple1)),hex(id(tuple2)))

Example_05 = 5

if Example_05:
    print(type(2)) # <class 'int'>
    print(type(2.0)) # <class 'float'>
    print(type(2j)) # <class 'complex'>


Example_06 = 6

if Example_06:
    T_int = type(0)
    print(T_int)    # <class 'int'>
    int2 = T_int('23123')       # !!!
    print(int2)     # 23123


Example_07 = 7

if Example_07:
    T_str = str
    print(T_str)        # <class 'str'>
    str2 = T_str(12345)
    print(str2)         # '12345'
    print(type(str2))   # <class 'str'>


Example_08 = 8

if Example_08:
    def func(a, b):
        return print(a * 2 + b)

    func(1, 2)    # 4
    func('sting 1', 'string 2')    # sting 1sting 1string 2


Example_09 = 9

if Example_09:
    int1 = 2
    print(int1 + 3)  # 5
    print(int1.__add__(3))  # 5


Example_10 = 10

if Example_10:
    def fun(a, b):
        return a + b
    print(fun)    # <function fun at 0x000002A6F9B0B6D0>


Example_11 = 11

if Example_11:
    def Fun(a, b, fn):
        return fn(a, b)

    print(Fun(1, 2, int.__add__)) # 3
    print(Fun(1., 2., float.__truediv__))  # 0.5


Example_12 = 12

if Example_12:
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return Vector(self.x - other.x, self.y - other.y)

        def __repr__(self):
            return f"Vector({self.x}, {self.y})"

    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1 + v2)  # Vector(4, 6)
    print(v1 - v2)  # Vector(-2, -2)
