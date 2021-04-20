from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import Reto
from json import loads
import psycopg2


'''
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads
from . models import Reto
import psycopg2
'''
def grafica(request):
    data = [ ['Age', 'Weight'], [ 8,      12], [ 4,      5.5], [ 11,     14],
          [ 4,      5],
          [ 3,      3.5],
          [ 6.5,    7]
        ]
    datos_formato = dumps(data)    
    return render(request,'grafica.html', {'losDatos':datos_formato})

def inicio(request):
    return render(request, "roboworld_app/index.html")

def stats(request):
    return render(request, "roboworld_app/stats.html")

def juego_unity(request):
    return render(request, "roboworld_app/juego_unity/index_unity.html")

def iniciar_sesion(request):
    return render(request, "roboworld_app/iniciar_sesion.html")

def proceso(request):
    nombre = request.POST['nombre']
    nombre=nombre.upper()
    
    return render(request, "proceso.html", {"nombre":nombre}) 

@login_required
def datos(request):
    jugadores = Reto.objects.all() #select * from Reto;
    return render(request, 'datos.html', {'lista_jugadores':jugadores})

@login_required
def score(request):
    usuario = request.user
    resultados = Reto.objects.filter(nombre=usuario)
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
    return render(request, 'score.html', {"nombreUsuario":nombre,"score":score})

@csrf_exempt
def unity(request):
    nombre = "Martin"
    score = "1234"
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)


'''
@csrf_exempt

def micuenta(request):
    session={
    num_engranes = "43"
    min_jugados = "53"
    veces_jugadas = "5"
    }
    return JsonResponse(session)
'''
@csrf_exempt

def buscaJugadorBody(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    resultados = Reto.objects.filter(nombre=jugador_nombre)  #select * from Reto where nombre = jugador_nombre
    
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
   
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)

@csrf_exempt
def ejemploSQL(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    nombre = ""
    score = ""

    try:
        connection = psycopg2.connect(
            user = "admin",
            password = "adminpass",
            host = "localhost",
            port = "5432",
            database = "dataroboworld"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roboworld_app_reto;")
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == jugador_nombre:
                nombre = row[1]
                score = row[2]
            print(row)
    
    except(Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL database', error)
        connection = None
    
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)

'''
Level

@csrf_exempt
def Level(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    Levelid = body_json['Levelid']
    Lvelid = ""
    level_number = ""
    enemigo = ""
    dificultad = ""
    duracion_individual=""

    try:
        connection = psycopg2.connect(
            user = "admin",
            password = "adminpass",
            host = "localhost",
            port = "5432",
            database = "dataroboworld"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ***createnewone***roboworld_app_reto;")
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == Levelid:
               
                Levelid = row[1]
                level_number = row[2]
                enemigo = row[3]
                dificultad = row[4]
                duracion_individual=row[5]
            print(row)
    
    except(Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL database', error)
        connection = None
    
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
    retorno = {"nivelID":Levelid,
        "level_number":level_number,
         "enemigo":enemigo,
         "dificultad":dificultad,
              " duracion_individual": duracion_individual}
    return JsonResponse(retorno)
'''
def micuenta(request):
    nombre = "Rebeca"
    num_engranes = "43"
    min_jugados = "53"
    veces_jugadas = "5"
    return render(request, "roboworld_app/micuenta.html", {"nombre":nombre,"num_engranes":num_engranes,"min_jugados":min_jugados,"veces_jugadas":veces_jugadas}) 


'''
def login(request):
    return render(request, "roboworld_app/login.html")

def logged_out(request):
    return render(request, "roboworld_app/logged_out.html")


def score(request):
    return render(request, "roboworld_app/score.html")
'''
