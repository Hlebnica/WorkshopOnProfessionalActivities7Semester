def point_in_area(x, y, x1, y1, x2, y2, r, s):
    if s == 0:  # Объединение
        in_rectangle = (x1 <= x <= x2) and (y1 <= y <= y2)
        in_circle = (x ** 2 + y ** 2) <= r ** 2
        return in_rectangle or in_circle
    elif s == 1:  # Пересечение
        in_rectangle = (x1 <= x <= x2) and (y1 <= y <= y2)
        in_circle = (x ** 2 + y ** 2) <= r ** 2
        return in_rectangle and in_circle
    else:
        return False

x, y, x1, y1, x2, y2, r, s = map(float, input().split())

result = point_in_area(x, y, x1, y1, x2, y2, r, s)
print(result)
