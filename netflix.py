from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('netflix_titles.csv')

#print(data.describe())


print(data.fillna('0'))

print(data.isna())

print(data['rating'].info)


data_filled = data.fillna('0')

print(data_filled['rating'])


#filtrar los datos entre 2010 y 2021
filtrar_datos = data[(data['release_year']>=2010) & (data['release_year']<=2021)]

filtrar_datos['type'] = filtrar_datos['type'].replace({'Movie': 'Películas', 'TV Show': 'Series'})


#contar el numero de peliculas y series

cantidad_por_año = filtrar_datos.groupby(['release_year', 'type']).size().unstack(fill_value=0)

#crear el gráfico


cantidad_por_año.plot(kind = 'bar')
plt.title('peliculas vs series')
plt.xlabel('Año')
plt.ylabel('Cantidad')
plt.legend(title='Tipo')
plt.show()