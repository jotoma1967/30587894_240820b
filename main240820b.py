import pip


try:
    from flask import Flask

except ImportError:

    pip.main(["install","Flask"])

    from flask import Flask

try:
    from flask import  render_template
except ImportError:
     
    pip.main(["install","render_template"])

    from flask import  render_template  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main240820b__':
     app.run(debug=True)

@app.route('/')
def get_data():
    name1 = 'Alfonso'
    return render_template('index.html', name1)


print("Iniciando")


import sys
import os
import os.path
import io
import string
import datetime
import math
import statistics
import random

import pip

try:
     import matplotlib

except ImportError:

    pip.main(["install","matplotlib"])

    import matplotlib

try:
    import pandas     

except ImportError:
    pip.main(["install","pandas"])
    import pandas


try:
    import numpy

except ImportError:
    pip.main(["install","numpy"])
    import numpy

try:
    import requests

except ImportError:
    pip.main(["install","requests"])
    import requests

print ("linea 55")



try:
    import matplotlib.pyplot
except ImportError:
    ##from pip._internal import main as pip
    pip.main(['install', 'matplotlib.pyplot'])
    import matplotlib.pyplot


try:
    import dateutil.parser

except ImportError:
    ##from pip._internal import main as pip
    pip.main(['install', 'dateutil.parser'])
    import dateutil.parser

print("linea 75")
try:
    import datetime
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'datetime'])
    import datetime

try:
    import pathlib
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'pathlib'])
    import pathlib

try:
    import os
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'os'])
    import os

try:
    import json
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'json'])
    import json

try:
    import time
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'time'])
    import time

try:
    import pytz
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'pytz'])
    import pytz

from xml.dom import registerDOMImplementation
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from dateutil import parser
import requests
from datetime import date  
from datetime import datetime
import pathlib  
import os
import json
import time as ti

from datetime import timedelta
from datetime import time
import pytz

newYorkTz = pytz.timezone("America/New_York") 
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")
print("The current time in New York is:", timeInNewYork)##currentTimeInNewYork)
##print("Esta version tiene señuelo para bolsausa")

d =date.today()
# d es la fecha de hoy que se le aplica la hora de New York

dos = datetime(d.year, d.month, d.day, hour=8, minute=30, tzinfo=newYorkTz,  fold=0)
##if timeInNewYork.hour==9:
    ##print ("tiene  buena pinta")
    ##dos = datetime(d.year, d.month, d.day, timeInNewYork.hour-1, minute=30, tzinfo=newYorkTz,  fold=0)

##if timeInNewYork.hour==10:
    ##print ("tiene  buena pinta")
    ##dos = datetime(d.year, d.month, d.day, timeInNewYork.hour-2, minute=30, tzinfo=newYorkTz,  fold=0)


print("hora comienzo new york",dos)
tiempooperacionnewyork = timeInNewYork  > dos ## horacomienzonewyork ####es >, < es para pruebas

##else:
    ##print("la hora corriente en new york es ", timeInNewYork.hour)

print("La hora de comienzo de New York es ",dos)
horacomienzonewyork = dos

print ("comparacion tiempo new york > horacomienzonewyork ",tiempooperacionnewyork)


diahoy = date.today().isoformat()
momentohoy = str(datetime.now())
numdiasemana=date.fromisoformat(diahoy).isoweekday() #del 1 lunes a 7 domingo

sabadoodomingo = False ##date.fromisoformat(diahoy).isoweekday()>5 ##>5

#print(numdiasemana)
#print(momentohoy)
datos_resumen_fon ={} ##datos resumen del fondo
clave_unica=""
datosaccenelfondo={}
cotiz_dacci ={}
diccotiz={}
dictfondos= {}
dictacciones={} #numero de acciones fondo
dicfontic={} 
#acciones keys, y fondos values
coberturaFondo={} #participación del fondo en una acción
indicebolsafontic=""
bolsafontic={}
tickersunicos={}
fondossinorden={}
cotizaaccion=[]
fonvariacion={}
dicaccfon={} ##fondos con sus acciones
listatodosdatosaccenelfondo=[]
cadenalinealistadohistoricobak=''
txtlistadohistoricobak=[] #para escribir el historictickersocotiza.csv
itemhistorico=[]          #para hacer y tratar con python graficas
contador = 0
fonvariacion={}





archivonombresfondos ='./nombreFondos.csv'
archivotickers ='./tickers.csv'
rhcsv = './resumenhistoricocsv.csv'
cotizahoypython='./cotizahoypy.csv'
resucsv ='./resumencsv.csv'
tikercsv = './tikercsv.csv'

'''
##cotizahoypython='C://Auxiliares/cotizahoypy.csv'from
archivonombresfondos ='C:\\Auxiliares\\nombreFondos.csv'
archivotickers ='C:\\Auxiliares\\tickers.csv '
rhcsv = 'C:\\Auxiliares\\resumenhistoricocsv.csv'
cotizahoypython='C:\\Auxiliares\\cotizahoypy.csv'
resucsv ='C:\\Auxiliares\\resumencsv.csv'
tikercsv = 'C:\\Auxiliares\\tikercsv.csv'
'''

class construirtikercvs():

    def cabeceratikercsv(self):
        
        ##borrado de fichero
        hmt = open(tikercsv, 'w')
        cabecera=( 'Fecha'+";"+'Fondo'+";"+'Ticker'+";"+'accion'+';'+'porcentaje'+";"+"Modif_porc"+";"+'Peso_absoluto'+";"+"Precio"+";"+"banco"+";"+"cnmv"+'\n')
        ##print("CABECERA DE HISTORICO ",cabecera)
        hmt.write(cabecera)
        hmt.close()
    
    def cuerpotikercsv(self, dicfontic):

        ##cotiz_dacci[dacci]=[dacci,marketPriceArmp,changePercentA]
        hmc= open(tikercsv,'a')
        
        ##claveunicasorted = sorted(dicfontic.keys())

        for claveunica in dicfontic.keys(): ## debes esta el tickers.csv ordenado por fondos y porcentajes:
            
            if tiempooperacionnewyork ==False: ##True: ##False: ##False: 
                    #True: ##//no carga usa y descuajeringa Pru1ods
                    ##print("121")
                    if "^" in dicfontic[claveunica][2] or "." in claveunica:
                        tic =dicfontic[claveunica][4]
            ##print("133 ",tic)
                        part=float(dicfontic[claveunica][5])
                        ##print("135 ",part)
                        vari=float(cotiz_dacci[tic][2])

                        precio=float(cotiz_dacci[tic][1])
                        ##print("140 ",precio)
                        if  "ALPHA" not in claveunica:########and "BESTIDEAS" not in claveunica: ##### and "^" not in claveunica:
                            lineacuerpo = ""+str(datetime.now())+";"+dicfontic[claveunica][2]+";"+ dicfontic[claveunica][4]+";"+dicfontic[claveunica][3]+";"+dicfontic[claveunica][5]+";"+str(vari)+";"+str(vari*part)+";"+str(precio) +";"+"IBERCAJA"+";"+"NOSE"+"\n"
                            hmc.write(lineacuerpo)
                        ##print("linea 93 "+ lineacuerpo)
            
                                ### nueveymedia_list_dacci.append(dacci)
            else:
                ###print("125")

        ###set_dacci=set(list_dacci)

                tic =dicfontic[claveunica][4]
                ##print("133 ",tic)
                part=float(dicfontic[claveunica][5])
                ##print("135 ",part)
                vari=float(cotiz_dacci[tic][2])

                precio=float(cotiz_dacci[tic][1])
                ##print("140 ",precio)
                if  "ALPHA" not in claveunica:### and "BESTIDEAS" not in claveunica: ##### and "^" not in claveunica:
                    lineacuerpo = ""+str(datetime.now())+";"+dicfontic[claveunica][2]+";"+ dicfontic[claveunica][4]+";"+dicfontic[claveunica][3]+";"+dicfontic[claveunica][5]+";"+str(vari)+";"+str(vari*part)+";"+str(precio) +";"+"IBERCAJA"+";"+"NOSE"+"\n"
                    hmc.write(lineacuerpo)
                ##print("linea 93 "+ lineacuerpo)

        hmc.close()

        

class ver_comp():

    
    def ver_c(self,ave):

        vercomposicion='BOLSAESPANA'

        
        while vercomposicion!='':

            vercomposicion= vercomposicion.upper()

            for fon in datos_fon.lista_fondos: ##dictaccfon: 

                if vercomposicion in fon:

                    n_acciones_fondo =0

                    lista_datos_fondo=[]

                    valorparticipaciones =0.0 

                    valorpesoglobal=0.0          


                    datos_fon.peso_acumulado=0.0

                    ####datos_fon.variacion_ponderada=0.0000
                    
                    n_acciones_fondo=0

                    n_acciones_fondo_menos_2_5 =  0

                    n_acciones_fondo_menos_1_5 =  0


                    print("Fondo analizado","\t\t", "Part.", "\t", "Var","\t", "Peso","\t","Acción","\t","Precio","\t","por -2.5","\t","por -1.5")

                    for daccikey in datos_fon.dicaccfoncl[fon]:

                        if tiempooperacionnewyork ==False: ##False: 
                #True: ##//no carga usa y descuajeringa Pru1ods
               
                            if "^" in fon or "." in daccikey: 

                                if vercomposicion in fon:

                                        n_acciones_fondo =n_acciones_fondo+1
                            
                                            
                                        claveunica = fon+"_"+daccikey

                                        ##print("linea 428 ",claveunica)
                                        peso_accion_fondo= datos_fon.dictfontic[claveunica][5]           

                                        ##print(claveunica ," linea 160")
                                        
                                        var_ac=round(cotiz_dacci[daccikey][2]*100,3)

                                       
                                        peso_var_ac=round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,3)
                                        precio =round(cotiz_dacci[daccikey][1],4)

                                        print(("{:}\t\t{:}\t{:5.3f}\t{:5.3f}\t{:10}\t{:7.4f}").format(fon,peso_accion_fondo, var_ac,peso_var_ac,cotiz_dacci[daccikey][0],precio))
                                        
                                        valorparticipaciones=valorparticipaciones+   round(float(peso_accion_fondo),    3)

                                        valorpesoglobal= valorpesoglobal+round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,3)                    
                        else:
                             if vercomposicion in fon:
    
                                        n_acciones_fondo =n_acciones_fondo+1
                            
                                            
                                        claveunica = fon+"_"+daccikey

                                        ##print("linea 428 ",claveunica)
                                        peso_accion_fondo= datos_fon.dictfontic[claveunica][5]           

                                        ##print(claveunica ," linea 160")
                                        
                                        var_ac=round(cotiz_dacci[daccikey][2]*100,3)
                                        peso_var_ac=round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,3)
                                        precio =round(cotiz_dacci[daccikey][1],4)

                                        print(("{:}\t\t{:}\t{:5.3f}\t{:5.3f}\t{:10}\t{:7.4f}").format(fon,peso_accion_fondo, var_ac,peso_var_ac,cotiz_dacci[daccikey][0],precio))
                                        
                                        valorparticipaciones=valorparticipaciones+   round(float(peso_accion_fondo),    3)

                                        valorpesoglobal= valorpesoglobal+round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,3)                    
                        
                        if var_ac < -2.5:
                                            n_acciones_fondo_menos_2_5 +=1

                        if var_ac < -1.5:
                                            n_acciones_fondo_menos_1_5 +=1
                                    

                    print("numero de acciones ", n_acciones_fondo, " peso de participaciones ",round(valorparticipaciones,2), " variacion global ",round(valorpesoglobal/100,4), " porc menor a 2.5 ", round( n_acciones_fondo_menos_2_5/n_acciones_fondo*100, 3)," porc menor a 1.5 ", round( n_acciones_fondo_menos_1_5/n_acciones_fondo*100,3) )   
 
            
            vercomposicion = input("Ver composicion del fondo =")



class mostrarchartfondo():

    fonvariacion={}


    def mcf(self):

        ##alprint ("linea 124 ")

        ki = open(rhcsv,'r',encoding="utf8", errors='ignore')

        lineas = ki.readlines()

        saltarheader = 0 #numero de lineas o accion-fondo
        
        for linea in lineas:

            if "Fondo" in linea:
                saltarheader += 1
                next  
            if saltarheader <2:
                next

            ##print("linea 141 ",linea)

            trozos= linea.split(';')
            
            datos_accion_sinorden =[]

            if "Fondo" not in trozos[1]:

                for fn in trozos[1]:

                    acciones_fondo={}

                  


                    datos_accion_sinorden.append(trozos[4]) ##var porcentual

                
                    mostrarchartfondo.fonvariacion[trozos[4]]=datos_accion_sinorden

              
        ki.close()   
    
        return mostrarchartfondo.fonvariacion

    def antiguocf(self):

        df = pd.read_csv(rhcsv, header =0, index_col =5, sep=';',decimal='.')

        nombrefondos = df['Fondo'] ##ondo?

        eleccionfondo = 'esp'    

        while eleccionfondo !='':

            mayusculasf =eleccionfondo.upper()
            
            if mayusculasf =='':
                break
           
            for ni in nombrefondos:
                if mayusculasf in "TODOS":
                    ddfalfa= df.groupby('Fondo').get_group(ni) ##fecha por Fondo
                    ##print("linea 194 ", ni)
                    estadisticadfalfa= ddfalfa['Var_porc'].describe() ##Peso por Var_porc
                
                    ##print(estadisticadfalfa)

                                   
                    l=ddfalfa['Var_porc'] ##peso por Var_porc
                
                    cs= l.cumsum()
                    
                    n = ddfalfa['Var_porc'].count() ##peso por Var_porc
                
                    y=list(range(n))
                    


                    Var_p=list(ddfalfa['Var_porc'])[-1]

                    ##print("ultima variación ",Var_p)
                    cad_titulo = ni+"  Variación: "+str(round(float(Var_p),4))

                    fig, ax = plt.subplots()
                    ax.plot(y,l)
                    ax.plot(y,cs)
                    ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')

                    ax.set_title(cad_titulo, loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
                    plt.show()

                    

                if mayusculasf in  ni:
                    dfalfa= df.groupby('Fondo').get_group(ni)
                    ##print(ni)
                    estadisticadfalfa= dfalfa['Var_porc'].describe()
                
                    ##print(estadisticadfalfa)
                
                    input(" Estadistica")
                    l=dfalfa['Var_porc']

                    cs= l.cumsum()
                    
                    n = dfalfa['Var_porc'].count()
                
                    y=list(range(n))
                    
                    Var_p=list(dfalfa['Var_porc'])[-1]

                    print("ultima variación ",Var_p)
                    cad_titulo = ni+" "+str(round(float(Var_p),4))

                    fig, ax = plt.subplots()
                    ax.plot(y,l)
                    ax.plot(y,cs)
                    ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')

                    ax.set_title(cad_titulo, loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
                    plt.show()

                    eleccionfondo = input(" 251 Gráficos y estadísticas del fondo = ")

                    mayusculasf =eleccionfondo.upper()
                    
                    if mayusculasf =='':
                        break

              

            eleccionfondo = input(" 251 Gráficos y estadísticas del fondo = ")
  
            mayusculasf =eleccionfondo.upper()
            
            if mayusculasf =='':
            
                break


   
class dicacc():
    
    def cvf(self):
        
        fat = open(archivotickers, 'r',encoding="utf8", errors='ignore')

        lineas = fat.readlines()

        saltarheader = 0 #numero de lineas o accion-fondo
        
        num_fon=0 ## numero fondo
        num_acc=0 ## "numero accion"


        for linea in lineas:

            if "Fondo" in linea:
                saltarheader += 1
                next  
            if saltarheader <2:
                next

            trozos= linea.split(';')
            

            if "Fondo" not in trozos[2]:    

                acciones_fondo={}

                datos_accion_sinorden =[]


                datos_accion_sinorden.append(trozos[2]) ##fondo

                datos_accion_sinorden.append(trozos[4]) ##accion

                datos_accion_sinorden.append(trozos[5]) ##peso accion fondo

                stri = ""+trozos[2]+"_"+trozos[4]

                
                acciones_fondo[stri]= {0:datos_accion_sinorden[0],1:datos_accion_sinorden[1], 2:datos_accion_sinorden[2]}

                dictacciones[trozos[4]]=(trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7])

                num_acc =num_acc+1
                for t2 in dictacciones.values():

                    if t2 == trozos[2]:
                        claveunica = ""+trozos[2]+"_"+trozos[4]
                        s[claveunica]=(trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7],"trozos8","trozos9","trozos10","trozos11")
                        print(dicfontic[claveunica])
                        input("406")
                    num_fon = num_fon +1
                
       

       

        fat.close()     
        csflist=[]
        csflist=[num_fon, num_acc]
        return acciones_fondo


class dicaccfonclase():
    
    def cvf(self):
        
        dicaccfoncl={}

        fat = open(archivotickers, 'r',encoding="utf8", errors='ignore')

        lineas = fat.readlines()

        saltarheader = 0 #numero de lineas o accion-fondo
        
        num_fon=0 ## numero fondo
        num_acc=0 ## "numero accion"


        for linea in lineas:

            if "Fondo" in linea:
                saltarheader += 1
                next  
            if saltarheader <2:
                next

            trozos= linea.split(';')
            
                                                                    
            trozos8=0.0 ##precio
            trozos9=0.0 ##variacion

        
            if "Fondo" not in trozos[2]:

                

                fondossinorden[trozos[2]]=0

                dictacciones[trozos[4]]=(trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7],trozos8,trozos9)

                num_acc =num_acc+1
                if True: ##for t2 in dictacciones.values():

                    if True: ##t2 == trozos[2]:
                        claveunica =trozos[2]+"_"+trozos[4]
                        dicfontic[claveunica]=[trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7],trozos8,trozos9]
                       
                    num_fon = num_fon +1
                
        listadicaccfon=[]

        dicaccfoncl={}

        for fon in sorted(fondossinorden.keys()):
        
            

            for linea in lineas:

                trozos2 = linea.split(";")
                ##print(trozos2)
                ##print("165")
           
                if trozos2[2]==fon:
                    
                    listadicaccfon.append(trozos2[4])
                    ##print(fon, " ",listadicaccfon)
                    ##print ("171")
            dicaccfoncl[fon]=listadicaccfon
            ##print(dicaccfoncl[fon])
           
            listadicaccfon=[]
        lista_fondos =sorted(fondossinorden.keys())
        
        fat.close()   

        csflist=[]
        csflist=[num_fon, num_acc]
        ''' 240819
        ctv=construirtikercvs()
        ctv.cabeceratikercsv()
        
        fg=dicaccfonclase()
        fgcvf=fg.cvf()
        ctv.cuerpotikercsv(fgcvf[0])
        '''
        return [dicfontic,dicaccfoncl,lista_fondos]   ##dicaccfon


class datos_fon(): 


    el = dicacc()
    
    dicaccfon=  el.cvf()

    cl=dicaccfonclase()  ## listado de acciones de un fondo

    dictaccfon = cl.cvf() ##dicfontic acciones_fondo dict clave unica

    dictfontic = cl.cvf()[0]         ## dicfontic claveunica acciones
    dicaccfoncl=cl.cvf()[1] ## diccionario accuibes del fondo
    lista_fondos = cl.cvf()[2]

    tuli =dicacc()

    acciones_fondo = tuli.cvf()

    peso_acumulado= 0.0

    variacion_ponderada =0.0

    peso_accion_fondo=0.0
    
    changePercentA=0.0

    abi = "" ##accion

    abidic= {}
     


    def cot_acc(self, dacci):
                        if  sabadoodomingo:
                            print("Hoy es fin de semana y no hay cotización")
                        else:
                            


                            url = "https://query1.finance.yahoo.com/v8/finance/chart/"+str(dacci)

                            r = requests.get(url,  headers={'User-agent': 'Mozilla/5.0'})
                            contenido   = r.json()

                            data = json.dumps(contenido)

                            ##print(data)

                            if "regularMarketPrice" not in data:

                                print(dacci," no encontrado")
                                input("no encontrada")
                                next
                            

                            else:
                                
                                ##print( " ", dacci," 511")
                                busqueda =""
                                
                                symb = ""
                                
                                            
                                symbA = dacci
            
                                '''
                                busqueda = "regularMarketPrice"
                                
                                mlidot = data.index(busqueda)

                                posterior = "fiftyTwoWeekHigh"

                                print (data)
                                       
                            
                                variableA = data[mlidot+len(busqueda)+2: data.index(posterior)-3]
                
                                marketPriceArmp = float(variableA)
                            
                            
                            
                                busqueda = "\"chartPreviousClose\":"
                                
                                rmlidot = data.index(busqueda)

                                posterior = "priceHint"
                        
                                variableA = data[rmlidot+len(busqueda)+1: data.index(posterior)-3]

                                changePercentA = (marketPriceArmp-float(variableA))/float(variableA)
    '''        
                                resultado = json.loads(data)

       
                                for meta, meta in resultado.items():
                                    i = 0;
                                    #print ("linea 643 ",meta,"\n")  

                                    #print( " linea 645 ",meta['result'],"\n")

                                    #print( " linea 647 ",meta['result'][0],"\n")

                                    #for key, value in meta['result'][0].items():
                                        
                                        #print ("linea 651 ",key, "\n")
                                       
                                        #print ( "linea 653 ",value, "\n");


                                    #print (" linea 656 ",meta['result'][0]['meta'],"\n")
                                      

                                    #print (" linea 658 ",meta['result'][0]['meta']['symbol'], "\n")

                                    
                                    regularPrice = meta['result'][0]['meta']['regularMarketPrice']

                                    chartPrevious = meta['result'][0]['meta']['chartPreviousClose'] 

                                    changePercentA = (float(regularPrice)-float(chartPrevious))/float(chartPrevious) ##(float(marketPriceArmp)-float(changePercentA))/float(changePercentA) ##(marketPriceArmp-float(variableA))/float(variableA)   
                        
                                                     

                                cotiz_dacci[dacci]=[dacci,regularPrice,changePercentA]
                                print ("635 ", dacci, " Precio mercado: ", regularPrice, " Variación: ", changePercentA) 
                                return cotiz_dacci[dacci]

                                

    def dat_acc(self):

        peso_accion_fondo=0.0

        datosaccenelfondo={}

        
        list_dacci=[]

        nueveymedia_list_dacci = [] 


        for fon in fondossinorden:
        
            for dacci in datos_fon.dicaccfoncl[fon]:
                  print(dacci)
                  print("656")
                  list_dacci.append(dacci)
           
        if tiempooperacionnewyork ==False: ##False: 
                #True: ##//no carga usa y descuajeringa Pru1ods
            for dacci in list_dacci:    
                if "^" in fon or "." in dacci: 
                    nueveymedia_list_dacci.append(dacci)
        else:

            for dacci in list_dacci:
                nueveymedia_list_dacci.append(dacci)

        ##print(nueveymedia_list_dacci) 
        ##input("642")       
            
        numerodeaccion=1

        ##print(list_dacci)

        ##print("590")
        
        ###set_dacci=set(list_dacci)

        ##print(set_dacci)

        ##print ("596")   
        
        
        ###set_dacci=set(list_dacci)

        list_dacci_sin_duplicados = []

        list_dacci_sin_duplicados =list(nueveymedia_list_dacci)

        ##print(list_dacci_sin_duplicados)

        ##print("604 list_dacci_sin_duplicados")

        list_dacci_sin_duplicados.sort()

        ##print(list_dacci_sin_duplicados)
        ##print("sort 697")

        set_dacci=set(list_dacci_sin_duplicados)

        ##print(set_dacci) ##list_dacci_sin_duplicados)
        ##print("701")
        list_dacci_sorted = list(set_dacci)
        list_dacci_sorted.sort()
        print(list_dacci_sorted)
        ##input("705 set_dacci")

        #acciones_ordenadas = acciones_ordenadas.sort(reverse=False, key=any)
        vez_respiro = 0

        for dacci in list_dacci_sorted: ##list_dacci_sin_duplicados:##(dicc_dacci.keys()).sort(): ##datos_fon.dicaccfoncl[fon]: 
                    ##print(" 573 ", dacci)
                    ##print("número de acción",numerodeaccion, " ", dacci)

                    ##numerodeaccion= numerodeaccion +1

                    vez_respiro = vez_respiro +1

                    if vez_respiro%80 == 0:
                        print ("respiro")
                        ti.sleep(9)
                       
                        ##input("respiro")

                    if tiempooperacionnewyork ==False: ##False: 
                        #True: ##//no carga usa y descuajeringa Pru1ods
                        

                        if "^" in dacci or "." in dacci: ##fon zv

                            cotiz_deacci=datos_fon.cot_acc(self,dacci) ##cotiz_deacci

                            print("número de acción no usa ",numerodeaccion, " ", dacci)

                            numerodeaccion= numerodeaccion +1

                    else:

                        cotiz_deacci=datos_fon.cot_acc(self,dacci) ##cotiz_deacci
                        
                        print("número de acción incluido usa ",numerodeaccion, " ", dacci)

                        numerodeaccion= numerodeaccion +1

                    ##print(cotiz_deacci)

        print("numero de acciones sin repetición ")
        print( len(list_dacci_sin_duplicados))        
        ##input("677")
        for fon in datos_fon.lista_fondos: ##dictaccfon: 

            n_acciones_fondo =0

            lista_datos_fondo=[]

            
            datos_fon.peso_acumulado=0.0

            ####datos_fon.variacion_ponderada=0.0000
            #####print(datos_fon.dicaccfoncl[fon])
            #####print(fon)
            ##input(689)

            for daccikey in nueveymedia_list_dacci: ###set_dacci:
                
                if daccikey in datos_fon.dicaccfoncl[fon]:

                    n_acciones_fondo =n_acciones_fondo+1
                
                    if True:
                        for fon in datos_fon.lista_fondos: ##dictaccfon: 

                            n_acciones_fondo =0

                            lista_datos_fondo=[]

                            valorparticipaciones =0.0 

                            valorpesoglobal=0.0          

                            n_acciones_menos_1_5 = 0

                            n_acciones_menos_2_5 = 0


                            datos_fon.peso_acumulado=0.0

                            ####datos_fon.variacion_ponderada=0.0000
                            
                            n_acciones_fondo=0

                            for daccikey in datos_fon.dicaccfoncl[fon]:

                                if daccikey in list_dacci_sin_duplicados:

                                ###if True:

                                        n_acciones_fondo =n_acciones_fondo+1
                            
                                            
                                        claveunica = fon+"_"+daccikey

                                        ##print("linea 428 ",claveunica)
                                        peso_accion_fondo= datos_fon.dictfontic[claveunica][5]           

                                        ##print(claveunica ," linea 160")

                                        ##print("Fondo ","\t\t", "\t", "Part.", "\t", "Var","\t", "Peso","\t","Accion","\t","Precio")
                    
                                        

                                        valorparticipaciones=valorparticipaciones+   round(float(peso_accion_fondo),    3)

                                        valorpesoglobal= valorpesoglobal+round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2]),3)   

                                        if cotiz_dacci[daccikey][2] < -2.5/100.0:
                                            n_acciones_menos_2_5 = n_acciones_menos_2_5 + 1 

                                        if cotiz_dacci[daccikey][2] < -1.5/100.0:
                                            n_acciones_menos_1_5 = n_acciones_menos_1_5 + 1

                                
                            
                            lista_datos_fondo.append(fon)
                            lista_datos_fondo.append(n_acciones_fondo)
                            lista_datos_fondo.append(valorparticipaciones)
                            lista_datos_fondo.append(valorpesoglobal)
                            if n_acciones_fondo ==0 or n_acciones_fondo == None:
                                n_acciones_fondo = 1
                            lista_datos_fondo.append(round(n_acciones_menos_1_5/n_acciones_fondo*100.0,3)) ##(n_acciones_menos_1_5/n_acciones_fondo)
                            lista_datos_fondo.append(round(n_acciones_menos_2_5/n_acciones_fondo*100.0,3)) ##(n_acciones_menos_2_5)  
                            
                            datos_resumen_fon[fon]=lista_datos_fondo
            
            lista_datos_fondo =[]
    
                
        
                    
                    
                    
                    
                    
                    
                    
                    
                       
                       
                       
                       
        return [datos_resumen_fon, datosaccenelfondo] ##resumen y detalle               
                
          


class manejarhistorico():
    
    contador =0
    
    txtlistadohistoricobak=[]

    def chuparmh(self): ##re dic datos hoy

        historicocotizapython = rhcsv   

              
    

        h = open(rhcsv, 'r',encoding="utf8", errors='ignore')

        lineah= h.readlines()

        saltarcabecera =0

        for line in lineah:
            
            saltarcabecera = saltarcabecera +1
      
            if saltarcabecera==1:
                continue

            trozoslin=line.split(';')


            
            if (not (trozoslin[0] is None)) and len(trozoslin[0])>4:##and ('/' in trozoslin[0]) :

                if '-' in trozoslin[0]:

                    primerslash = trozoslin[0].index('-')
                    segundoslash = trozoslin[0].rfind('-')

                    diahoyprimerguion= (diahoy).index('-')
                    diahoysegundoguion = ( diahoy).rfind("-")

                    #print("linea 718 ano historico",str(int(trozoslin[0][0:primerslash])))
                    #print("linea 719 mes historico ",str((trozoslin[0][primerslash+1:segundoslash])))
                    #print("linea 720 dia historico", str(int (trozoslin[0][segundoslash+1:])))

                    anoh=(int(trozoslin[0][0:primerslash])) ##aqui hemos cambiado diah por anoh al ser guion
                    mesh=(int(trozoslin[0][primerslash+1:segundoslash]))
                    diah=(int (trozoslin[0][segundoslash+1:])) ##aqui hemos cambiado anoh por diah al ser guion



                    anohoy =(int(diahoy[0:diahoyprimerguion]))
                    meshoy=(int(diahoy[diahoyprimerguion+1: diahoysegundoguion]))
                    diahoynum= (int(diahoy[diahoysegundoguion+1:]))

                    
                    ##print("linea 561 dia hoy  ",(diahoynum))
                    ##print("linea 562 meshoy ",(mesh))
                    ##print("lineahoy 563 anohoy ", (anoh))

                    ##print("linea 574 ", trozoslin[1], trozoslin[0])

                    #print(("linea 739 con guiones ",(datetime.isoweekday(datetime(anoh,mesh,diah)))), "  ", datetime(anoh,mesh,diah), " today ",datetime(anohoy,meshoy,diahoynum))
                            

                    if  (datetime(anoh,mesh,diah)<datetime(anohoy, meshoy, diahoynum)):
                        registro = trozoslin[0]+";"+trozoslin[1]+";"+trozoslin[2]+";"+trozoslin[3].replace(',','.')+";"+(trozoslin[4].replace(',','.'))
                        registro = registro +";;\n"

                        ##print("linea 568 ",registro)
                        manejarhistorico.txtlistadohistoricobak.append(registro)
                        ##print("linea 554 ",txtlistadohistoricobak)
                        itemhistorico.append([trozoslin[0],trozoslin[1],trozoslin[2],trozoslin[3],trozoslin[4]])
    


                if '/' in trozoslin[0]:    
                   
                    primerslash = trozoslin[0].index('/')
                    segundoslash = trozoslin[0].rfind('/')

                    diahoyprimerguion= (diahoy).index('-')
                    diahoysegundoguion = ( diahoy).rfind("-")

                    #print("linea 760 dia historico",str(int(trozoslin[0][0:primerslash])))
                    #print("linea 761 mes historico ",str((trozoslin[0][primerslash+1:segundoslash])))
                    #print("linea 762 ano historico", str(int (trozoslin[0][segundoslash+1:])))

                    diah=(int(trozoslin[0][0:primerslash]))
                    mesh=(int(trozoslin[0][primerslash+1:segundoslash]))
                    anoh=(int (trozoslin[0][segundoslash+1:]))



                    anohoy =(int(diahoy[0:diahoyprimerguion]))
                    meshoy=(int(diahoy[diahoyprimerguion+1: diahoysegundoguion]))
                    diahoynum= (int(diahoy[diahoysegundoguion+1:]))

                    
                    ##print("linea 561 dia hoy  ",(diahoynum))
                    ##print("linea 562 meshoy ",(mesh))
                    ##print("lineahoy 563 anohoy ", (anoh))

                    ##print("linea 574 ", trozoslin[1], trozoslin[0])

                    #print(("linea 781",(datetime.isoweekday(datetime(anoh,mesh,diah)))), "  ", datetime(anoh,mesh,diah), " yesteday  ",(datetime.today()-timedelta(days=0, seconds=0, microseconds=0,           milliseconds=0, minutes=0, hours=23, weeks=0)))
                            

                    if   ((datetime.isoweekday(datetime(anoh,mesh,diah)))<6) and datetime(anoh,mesh,diah)<(datetime.today()-timedelta(days=0, seconds=0, microseconds=0,
                milliseconds=0, minutes=0, hours=23, weeks=0)):
                        registro = trozoslin[0]+";"+trozoslin[1]+";"+trozoslin[2]+";"+trozoslin[3].replace(',','.')+";"+(trozoslin[4].replace(',','.'))
                        registro = registro +";;\n"
                        ##print("linea 568 ",registro)
                        manejarhistorico.txtlistadohistoricobak.append(registro)
                        ##print("linea 554 ",txtlistadohistoricobak)
                        itemhistorico.append([trozoslin[0],trozoslin[1],trozoslin[2],trozoslin[3],trozoslin[4]])
    
        h.close()
        return manejarhistorico.txtlistadohistoricobak

    def recrearficheromh(self):
        
        ##borrado de fichero
        hm = open(rhcsv, 'w')
        cabecera=( 'Fecha'+";"+'Fondo'+";"+'n'+";"+'Peso'+';'+'Var_porc'+";"+"Actualizacion"+";"+"porc_1_5"+";"+"porc_2_5"+'\n')
        ##print("CABECERA DE HISTORICO ",cabecera)
        hm.write(cabecera)
        hm.close()
        

    def incorporarmh(self):  ##manejarhistorico.txtlistadohistoricobak historico

    
        
        #reconstitución de fichero
               
        h = open(rhcsv, 'a')

        for registro in manejarhistorico.txtlistadohistoricobak:
            ##print("linea 609 ", registro)
            ll=h.write(registro)
            #print("576 ", ll)
            ##print("642",registro)

        h.close()

    def incorporarhoy(self):      

        re = datos_resumen_fon
        
        h= open(rhcsv,'a')

        for cad in re.keys():
            #print("linea 283 ", cad)
            if  sabadoodomingo:
                print("Hoy es fin de semana y no hay cotización")
            else: #elimina los de hoy  y fines para que no se dupliquen
         
                recad=datos_resumen_fon[cad]
                ##print(recad)
                cadenaretxt= str(diahoy)+";"+str(recad[0])+";"+str(recad[1])+";"+str(recad[2])+";"+str(recad[3])+";"+momentohoy+";"+str(recad[4])+";" +str(recad[5])+"\n"
                ##print ("REGISTROS DE HOY ",cadenaretxt)

                ##print ("589 ",cadenaretxt)
                
                h.write(cadenaretxt)
                itemhistorico.append(re[cad])
        
        h.close()

       

class preguntarchartfondo():

    mayusculasf =""


    ## fufu =mostrarchartfondo()
    def pcf(self):
        
        repetir = 'S'

        while repetir in 'SI':

            eleccionfondo ='BOLSAESPANA'

            ##eleccionfondo = 'si'    

            while eleccionfondo !='':
              
                mayusculasf =eleccionfondo.upper()
                if mayusculasf =='':
                    repetir ="no"
                    break
                
                
        
            repetir = input("De qué fondo desea ver más gráficos?")

       


class maino():
    saltarheader2=0
    
    def creaccionnombresfondos(self):
        
        

        fsog = open(archivonombresfondos,'w')

        fsog.close()

        ##print ("646 fichero renovado ", archivonombresfondos)

    def anadidosfondos(self):

        ##print("650 ejecutando anadidosfondos")
               
        arcnomfon =archivonombresfondos

        er = dicaccfonclase()
        listafondos = er.cvf()[2]
   
        fso = open(arcnomfon, 'a')

    

        for fond9 in listafondos: ##archivo nombres fondos
            
            cadfon =fond9+"\n"
            py =fso.write(cadfon)
          
        fso.close()

    
    def creacotizahoypython(self):


        f = cotizahoypython
        ##if os.path.isfile(f):
            ##  os.remove(f)

        chp = cotizahoypython

        g=open(chp,'w')
        
        g.write( 'Fecha'+";"+'Fondo'+";"+'n'+";"+'Peso'+';'+'Var_porc'+";"+"Actualizacion"+";"+"porc_1_5"+";"+"porc_2_5"+'\n')

        g.close()

    def anadircotizahoypython(self):
        
       
        cothoypyt = cotizahoypython


        re = datos_resumen_fon

        ##print (re)

        gi = open(cothoypyt, 'a')


        for resumen in re:
        
            ##print(resumen)

            listado = re[resumen]
            
            ##print(listado)

            linea_resumen = ""+str(diahoy)+";"+str(listado[0])+";"+ str(listado[1])+";" +str(listado[2])+";"+str(listado[3])+";" +str(momentohoy)+";" +str(listado[4])+";" +str(listado[5])+"\n"

            ##print(linea_resumen)

            ilo = gi.write (linea_resumen)
            
      
        gi.close()
        
        if os.path.isfile(resucsv):
            os.remove(resucsv)



        resumcsv = open(resucsv,'w')
        resumcsv.close()

        resumcsv = open(resucsv,'a')

        resumcsv.write("dia;fondo;n;peso;var_por;actualizacion;porc_1_5;porc_2_5\n")

        for resumen in re:
            
            ##print(resumen)

            listado = re[resumen]
            
            ##print(listado)

            linea_resumen = ""+str(diahoy)+";"+str(listado[0])+";"+ str(listado[1])+";" +str(listado[2])+";"+str(listado[3])+";" +str(momentohoy)+";" +str(listado[4])+";" +str(listado[5])+"\n"

            ##print(linea_resumen)

            ilo = resumcsv.write (linea_resumen)
            
      
        resumcsv.close()

    def pantallahoy(self):

        h = open(cotizahoypython, 'r',encoding="utf8", errors='ignore')

        lineah= h.readlines()

        eliminadorcabeza=0;

        for line in lineah:

            campos= line.split(";")
            
            if eliminadorcabeza==0:
                eliminadorcabeza= eliminadorcabeza +1
                fecha = str(campos[0])
                fondos = campos[1],
                n=campos[2]
              
              
                
                
              
                print('{:3}\t\t{:4}\t{:4}\t{:4}\t{:}\t\t{:4}\t{:4}'.format(str(campos[0]),str(campos[2]),str(campos[3]),str(campos[4]),campos[1],str(campos[6]),str(campos[7])))
                next

                       
            else: 

                pesof=round(float(campos[3]),4)
                variacionf=round(float(campos[4]),4)
                fecha = str(campos[0])
                fondos = campos[1]
                n=str(int(campos[2]))
                var = str(round(float(campos[3]),2))
                


                ##print(pesof,  "  var: ",variacionf)

                print('{:3}\t{:4}\t{:4}\t{:4}\t{:10}\t\t{:4}\t{:4}'.format(fecha,n,pesof,variacionf,fondos,str(campos[6]),str(campos[7])))
                
                ##print(str(campos[0]),'\t',campos[1],'\t',str(campos[2]),'\t',str(pesof), '\t',str(variacionf))
        ##print(tabulate(lineah, headers = ['fecha','fondo','n','Peso','Variacion']))
        h.close()

    def procesomanejarhistorico(self):
       
      
        mhu=manejarhistorico()
        bu =mhu.mh()



class mainje():  

    def maindef(self): 
        ##actualizardatos = input("Actualizar datos? (s) ")
        if True: ##actualizardatos  in "Sisi":      
            momentoinicio = str(datetime.now())
            print(momentoinicio)
            print("trabajando ...")
            gir=datos_fon()
            ejec0 = gir.dat_acc() ##da datos_resume_fon
            ctv=construirtikercvs()
            ctv.cabeceratikercsv()
            fg=dicaccfonclase()
            fgcvf=fg.cvf()
            ctv.cuerpotikercsv(fgcvf[0])
            ejecutar = maino()
            ejec1 = ejecutar.creaccionnombresfondos()
            ejec2 = ejecutar.anadidosfondos()
            ejec3= ejecutar.creacotizahoypython()
            ejec4= ejecutar.anadircotizahoypython()
            ejec5= ejecutar.pantallahoy()

            print(momentoinicio)
            momentofinalizacion = str(datetime.now())
            print(momentofinalizacion)

                    
            mhejecutar =manejarhistorico()
            meje1= mhejecutar.chuparmh()
            meje2= mhejecutar.recrearficheromh()
            meje3= mhejecutar.incorporarmh()
        
            meje4= mhejecutar.incorporarhoy();
        '''        
            print(momentoinicio)
            momentofinalizacion = str(datetime.now())
            print(momentofinalizacion)
            
            ##input("873")
            hy=ver_comp()
            hy.ver_c(ejec0[1])

        repetir = input( " 875 Quiere ver el gráfico de algún fondo (n = ninguno) ")
        while repetir not in "Nn":
            ##io = preguntarchartfondo()
            ##iou= io.pcf()
            jijo=mostrarchartfondo()
            jijomcf=jijo.mcf( )   
            jijomoc0= jijo.antiguocf()
            
            repetir = input( " 883 Quiere ver el gráfico de algún fondo (n = ninguno) ")
        '''
    momentohoy = str(datetime.now())
    print(momentohoy)

if False: ##numdiasemana>5:
    print("el fin de semana esto no funciona")
    input("854")
    exit()
cl= mainje()
cl.maindef()

   
