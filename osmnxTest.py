#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: osmnxTest.py 
@time: 2018/05/{DAY} 
描述: 

"""

import osmnx as ox
from folium import folium



ox.config(log_file=True, log_console=True, use_cache=True)


# from some place name, create a GeoDataFrame containing the geometry of the place
city = ox.gdf_from_place('雁塔区, 西安, 中国')
#lding = ox.buildings.buildings_from_place('陕西省, 中国')
# save the retrieved data as a shapefile
ox.save_gdf_shapefile(city,u'雁塔区',r'./data/')



#Get building footprints within the boundaries of some place.
aaaBuilding = ox.buildings.buildings_from_place(place=u'雁塔区, 西安, 中国')
#gdf = ox.buildings_from_place(place='Piedmont, California, USA')
ox.save_gdf_shapefile(aaaBuilding,'test',r'./data/')





#Get building footprints within some distance north, south, east, and west of an address.
#address_rect = ox.buildings.buildings_from_address('钟楼, 南大街, 南院门街道, 碑林区, 西安市, 陕西省, 710001, 中国', 3000)

point_rect = ox.buildings.buildings_from_point((34.374944,107.129382), 300, retain_invalid=False)
#Get building footprints within some distance north, south, east, and west of a lat-long point.
ox.plot_shape(point_rect)


#道路网下载保存
#osmnx.core.graph_from_place(query, network_type='all_private', simplify=True, retain_all=False, truncate_by_edge=False, name='unnamed', which_result=1, buffer_dist=None, timeout=180, memory=None, max_query_area_size=2500000000, clean_periphery=True, infrastructure='way["highway"]', custom_filter=None)
street_graph = ox.graph_from_place("金台区, 宝鸡市, 陕西省", network_type='all_private',which_result=2)                   #返回结果为graph 对象
street_gdfs = ox.save_load.graph_to_gdfs(street_graph, nodes=False, edges=True, node_geometry=True, fill_edge_geometry=True)        #将graph_转化为_gdf 对象
ox.save_load.save_graph_shapefile(street_graph, filename='Baoji_jintai', folder=None, encoding='utf-8')                     #保存graph 对象为shape文件
ox.save_gdf_shapefile(street_gdfs, 'Baoji_jintai',r'./data/')     # 保存gdf类型的对象
ox.plot_graph(street_graph)                                             #graph 对象绘图


foliumHtml = ox.plot.plot_graph_folium(street_graph, graph_map=None, popup_attribute=None, tiles='cartodbpositron', zoom=1, fit_bounds=True, edge_color='#333333', edge_width=5, edge_opacity=1)
foliumHtml.save('./Features_0.html')        #保存为网页
print('ppp')
map_osm = folium.Map(location=[45.5236, -122.6750])
#此处 map_osm.create_map()  方法 貌似失效了  替换为 map_osm.save()  方法可用
map_osm.save('./Features_0.html')


#address_rect
city