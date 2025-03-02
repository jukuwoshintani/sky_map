import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astroquery.vizier import Vizier

# Загружаем данные из каталога Hipparcos
Vizier.ROW_LIMIT = -1
hip_data = Vizier.get_catalogs("I/239/hip_main")[0].to_pandas()

# Выводим список столбцов для проверки
print(hip_data.columns)

# Убираем строки с отсутствующей яркостью и фильтруем по Vmag < 6.0
hip_data = hip_data.dropna(subset=['Vmag'])
hip_data = hip_data[hip_data['Vmag'] < 6.0]

# Используем координаты из столбцов RAICRS и DEICRS (в градусах)
ra_deg = hip_data['RAICRS']
dec_deg = hip_data['DEICRS']

# Переводим градусы в радианы
ra_rad = np.radians(ra_deg)
dec_rad = np.radians(dec_deg)

# Преобразуем координаты для 2D-проекции
x = np.cos(ra_rad) * np.cos(dec_rad)
y = np.sin(ra_rad) * np.cos(dec_rad)

# Масштабируем размер точек в зависимости от яркости
sizes = 10 / (hip_data['Vmag'] + 2)

# Строим карту звездного неба
plt.figure(figsize=(8, 8), facecolor='black')
plt.scatter(x, y, s=sizes, color='white', alpha=0.8)
plt.title("🌌 Звездное небо (Hipparcos)", color='white')
plt.axis('off')
plt.show()
