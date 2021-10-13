# 1. дан следующий код
# f = func("a", "b", "c")
# print(f("x"))
# Результат должен быть
# ["xa", "xb", "xc"]
from functools import reduce


def func(a="a", b="b", c="c"):
    return lambda x: [x + a, x + b, x + c]


def task_1():
    f = func()
    print(f("x"))


# 2. дан лист листов
# l = [[1,2,3,4,5,6], [0,0,0,0], ["a", "b", "c"]]
# Необходимо написать код который превратит его в простой лист
# [1,2,3,4,5,6,0,0,0,0,"a", "b", "c"]
# для решения данной задачи нельзя использовать доп массива

# def task_2(l):
#     return reduce(lambda a, b: a + b, l)
task_2 = lambda l: reduce(lambda a, b: a + b, l)


if __name__ == "__main__":
    task_1()

    l = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0], ["a", "b", "c"]]
    print(task_2(l))
