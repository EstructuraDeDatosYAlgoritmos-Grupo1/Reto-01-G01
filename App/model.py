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


#Funciones para agregar datos a un catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    t = newCategory(category['id'], category['name'])
    lt.addLast(catalog['categories'], t)


def addvideoFromCatalog(catalog,catalogCC,bestCountry,bestCategoryid):
    range1 = lt.size(catalog["videos"])
    for position in range(1, range1 +1):
        element = lt.getElement(catalog['videos'] , position)
        if (element["country"] == bestCountry and element["category_id"]==bestCategoryid):
            addVideo(catalogCC, element)
    return catalogCC


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

#Funciones para comparar elementos dentro de una lista


#Funciones de ordenamiento