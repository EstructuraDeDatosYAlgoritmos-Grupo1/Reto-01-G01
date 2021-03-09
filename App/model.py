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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shes
from DISClib.Algorithms.Sorting import insertionsort as inss
from DISClib.Algorithms.Sorting import selectionsort as sels
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
assert cf


"""
En el modelo, se crean las estructuras de datos, es decir,
las variables donde se van a guardar los datos leidos de los
archivos CSV.

El modelo debe ser el unico sitio donde se modifican y manipulan
los datos.
"""


#Construccion de catalogos
def createCatalog():
    catalog = {'videos': None,'categories': None,}
    catalog['videos']= lt.newList(datastructure='ARRAY_LIST')
    catalog['categories'] = lt.newList(datastructure='ARRAY_LIST')
    return catalog

def createCatalogOfCountry(catalog, country):
    catalogCountry = createCatalog()
    catalogCountry = addVideosFromCatalogByCountry(catalog,catalogCountry,country)
    return catalogCountry


#Funciones para agregar datos a un catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    t = newCategory(category['id'], category['name'])
    lt.addLast(catalog['categories'], t)


def addvideoFromCatalogByCountryCategory(catalog,bestCountry,bestCategoryid):
    bestVideos = createCatalog()
    for videoPos in range(1, lt.size(catalog["videos"])):
        video = lt.getElement(catalog["videos"], videoPos)
        if (video["country"]== bestCountry and int(video["category_id"])==int(bestCategoryid)):
            addVideo(bestVideos, video)
    return bestVideos

def addVideosFromCatalogByCountry(catalog,catalogVideos,country):
    range1 = lt.size(catalog["videos"])
    for position in range(1, range1 + 1):
        element = lt.getElement(catalog["videos"] , position)
        if element["country"] == country:
            addVideo(catalogVideos, element)
    return catalogVideos


#Funciones para crear datos

def newCategory(category_id,name):
    category = {'id': category_id, 'name': name}
    return category


#Funciones de consulta

def findCategoryid(catalog, category):
    range1 = lt.size(catalog["categories"])
    for position in range(1, range1 + 1):
        element = lt.getElement(catalog["categories"], position)
        if (element["name"].strip()==category):
            return element["id"]
    return -1

def findTopVideoByTrendingTime(catalogCountry):
    pass
#Funciones para comparar elementos dentro de una lista

def cmpVideosByViews(video1, video2):
    if float(video1['views']) < float(video2['views']):
        return True
    else:
        return False

#Funciones de ordenamiento

def mergeSortByViews(catalog,size):
    subList = lt.subList(catalog["videos"],0,size)
    subList = subList.copy()
    sortedList = merge.sort(subList, cmpVideosByViews)
    return sortedList