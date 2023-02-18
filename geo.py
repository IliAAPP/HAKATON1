# отражение всех точек заказчика на карте с подсказками
# (территория Краснодарского края

import folium

m = folium.Map(location=[45.026368, 39.087620], start_zoom=8)

tooltip = 'Бородинская улица, 14'
tooltip_2 = 'Уральская ул., 75/1к2, Краснодар'
tooltip_3 = 'Северная ул., 327, Краснодар'
tooltip_4 = 'Командорская ул., 9/2, Краснодар'
tooltip_5 = 'Фабрициуса ул., 16, Сочи'
tooltip_6 = 'Ленина ул., 173А, Анапа'

folium.Marker([45.026368, 39.087620], popup='Главный офис', tooltip=tooltip).add_to(m)
folium.Marker([45.032948184839086, 39.04587970041479], popup='Аквамарин', tooltip=tooltip_2).add_to(m)
folium.Marker([45.038868593006484, 38.9864721887298], popup='Кристалл', tooltip=tooltip_3).add_to(m)
folium.Marker([45.092971, 39.032167], popup='Командорская ул., 9/2', tooltip=tooltip_4).add_to(m)
folium.Marker([43.577172, 39.748951], popup='Фабрициуса ул., 16', tooltip=tooltip_5).add_to(m)
folium.Marker([44.874605, 37.329995], popup='Ленина ул., 173А', tooltip=tooltip_6).add_to(m)

m.save('name.html')

# 45.026368, 39.087620

# popup - значение если тыкнуть на сам маркер
# если наводимся - tooltip
