"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv
from DISClib.ADT import list as lt


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.createCatalog()
    return catalog


# Funciones para la carga de datos
def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)

def loadVideos(catalog):
    """
    Carga los videos del archivo. 
    """
    videosfile =  cf.data_dir + 'videos/videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategories(catalog):
    """
    Carga los videos del archivo. 
    """
    categoryfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        model.addCategory(catalog, category)


#Funciones para la consulta de datos

def bestVideosCategoryCountryViews(catalog,bestCountry,bestCategory,numberVideos):
    catalogCC = initCatalog()
    bestCategoryid = model.findCategoryid(catalog,bestCategory)
    if bestCategoryid == -1:
        return -1
    else:
        catalogCC = model.addvideoFromCatalog(catalog,catalogCC,bestCountry,bestCategoryid)
        topVideos = lt.newList(datastructure='ARRAY_LIST')
        if lt.size(catalogCC["videos"]) < numberVideos:
            return -2
        else:
            for i in range(1, numberVideos + 1):
                lt.addLast(topVideos, lt.getElement(catalogCC["videos"],i) )
            if lt.size(topVideos)==0:
                return -3
            else:
                return topVideos

def videoMoreTimeTrendingCountry(country):
    pass