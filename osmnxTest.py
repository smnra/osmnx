#!usr/bin/env python  
#-*- coding:utf-8 _*-  

""" 
@author:Administrator 
@file: osmnxTest.py 
@time: 2018/05/{DAY} 
描述: 

"""

import osmnx as ox
ox.config(log_file=True, log_console=True, use_cache=True)


# from some place name, create a GeoDataFrame containing the geometry of the place
city = ox.gdf_from_place('雁塔区, 西安, 中国')
#lding = ox.buildings.buildings_from_place('陕西省, 中国')
# save the retrieved data as a shapefile
ox.save_gdf_shapefile(city,u'雁塔区',r'./data/')



#Get building footprints within the boundaries of some place.
aaaBuilding = ox.buildings.buildings_from_place(place=u'雁塔区, 西安, 中国')
#gdf = ox.buildings_from_place(place='Piedmont, California, USA')
ox.save_gdf_shapefile(aaaBuilding,u'雁塔区',r'./data/')






city