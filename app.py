import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Заголовок приложения
st.title('Интерактивный график с Streamlit')

# Текстовое описание
st.write('Это пример интерактивного приложения, созданного с помощью Streamlit.')

# Слайдер для выбора числа
number = st.slider('Выберите количество точек для графика', 10, 1000, 500)

# Генерация данных для графика
data = np.random.normal(0, 1, size=number)

# Построение графика
fig, ax = plt.subplots()
ax.hist(data, bins=30, color='blue', alpha=0.7)
ax.set_title('Гистограмма случайных данных')
ax.set_xlabel('Значение')
ax.set_ylabel('Частота')

# Отображение графика в Streamlit
st.pyplot(fig)

# Информация о данных
st.write(f'Вы выбрали {number} точек. График показывает распределение случайных данных.')