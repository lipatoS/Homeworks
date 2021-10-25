# Задача 2
#
# Напишите функцию, которая изменит переданный текст.
#
# Исходная строка разбивается на части.
# Функция возвращает преобразованный текст, собранный с тем же разделителем.
#
# Ввод
# message = 'An amazing, wooden man, who can dance, fence, turn somersaults in the air.'
#
# До первой запятой ничего не изменяется
# со второй до третьей запятой — всё большими буквами
# с третье до четвертой — только первые буквы большие
# с четвертой до пятой — дублируется само слово 2 раза
# после последней запятой— ничего не происходит.
#
# Строка может быть разная и количество запятых может быть меньше.
# Но с последней часть и первой ничего не должно происходить.
#
# Вывод
# An amazing, WOODEN MAN, Who Can Dance, fencefence, turn somersaults in the air.

def rename(strings):
    lst = [i + "," for i in strings.split(",")]
    cols = len(lst)
    lst[-1] = lst[-1][:-1]
    for i in range(0, len(lst)):
        if len(lst) <= 2:
            lst[-1] = lst[-1][:-1]
            break
        if cols == len(lst):
            cols -= 1
            continue
        if cols == 1:
            break
        if cols == len(lst) - 1:
            lst[i] = lst[i].upper()
            cols -= 1
            continue
        if cols == len(lst) - 2:
            lst[i] = lst[i].title()
            cols -= 1
            continue
        if cols == len(lst) - 3:
            lst[i] = f" {lst[i][1:-1] * 2},"
            cols -= 1
            continue
    last_string = "".join(lst)
    return f"{last_string}"


print(rename(
    "An amazing, wooden man, who can dance, fence, turn somersaults in the air."))
