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
 * contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
import sys
import controller
import model
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar buenos videos por categoría y país")
    print("3- Encontrar video tendencia por país ")
    print("4- Encontrar video tendencia por categoría")
    print("5- Buscar los videos con más likes")
    print("0- Salir")


def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printResults(catalogVideos, sample):
    size = lt.size(catalogVideos)
    if size > sample:
        i = 0
        while abs(i) < sample:
            video = lt.getElement(catalogVideos, i)
            print('Titulo: '+video["title"]+"\nTitulo del canal: "+video["channel_title"]+"\nFecha en tendencia: "+video["trending_date"]+"\nViews: "+video["views"]+"\nDislikes: "+video["dislikes"])
            i-=1

def printResults2(results):
    video = results[0]
    print('Titulo: '+video["title"]+"\nTitulo del canal: "+video["channel_title"]+"\nPais: "+video["country"]+"\nDias: "+str(results[1]))

def printResults3(results):
    video = results[0]
    print('Titulo: ' + video["title"]+"\nTitulo del canal: " + video["channel_title"] + "\nCategory_id "+ video["category_id"] + "\nDias: " + str(results[1]))

catalog = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de libros....")
        catalog = initCatalog()
        loadData(catalog)
        print('Total de libros cargados: ' + str(lt.size(catalog['videos'])))

    elif int(inputs[0]) == 2:
        numberVideos = int(input("Ingrese el número de videos con más views que desea encontrar: "))
        bestCountry = input("Ingrese el pais sobre el cual quiere encontrar los mejores videos: ").lower()
        bestCategory = input("Ingrese la categoria de videos que desea consultar: ")
        result = controller.bestVideosCategoryCountryViews(catalog,bestCountry,bestCategory)
        printResults(result,numberVideos)
        if result == -1:
            print("\nIngrese una categoria valida\n")
        else:
            print("Estos son el top " + str(numberVideos)+ " videos encontrados para el pais y la categoria.")
        
    elif int(inputs[0]) == 3:
        bestCountry = input("Ingrese el pais sobre el cual quiere encontrar los mejores videos: ").lower()
        printResults2(controller.videoMoreReps(catalog,bestCountry))

    elif int(inputs[0]) == 4:
        category = input("Ingrese la categoria de videos que desea consultar: ")
        printResults3(controller.videoMoreRepsCategory(catalog,category))
        


    else:
        sys.exit(0)
sys.exit(0)
