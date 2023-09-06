import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

x = np.array([-2, 2, 0]).reshape((-1, 1))
y = np.array([0, 0, 2])

# (−2,0),(2,0),(0,2)

model = LinearRegression()

model.fit(x, y)

y_pred = model.predict(x)


# Рассчитываем метрики
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Выводим результаты
print("Средняя абсолютная ошибка (MAE):", mae)
print("Среднеквадратичная ошибка (MSE):", mse)
print("Коэффициент детерминации (R-squared):", r2)