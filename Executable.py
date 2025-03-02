"""
Created on Fri Aug 21 17:36:09 2020
Analiza pruebas de decremento
@author: Ruben
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import joblib
from scipy.optimize import curve_fit
'''Paquetes para escribir reporte'''
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch

NOMBRE="datos41.2"
C=pd.read_table(NOMBRE+'.dat', sep=' ')
''' abre el archivo con el modelo entrenado'''
classifer = joblib.load("FluxRegimes.pkl")
Y=C.keys

#print(C[["DT","DP","OD", "SD"]])
Y=classifer.predict(C[["DT","DP","OD", "SD"]])
C["periodo"]=Y
#print (C)
colors={"Storage":"tab:blue","Trans":"tab:orange","IARF":"tab:green","LF":"tab:red","CC":"tab:brown","ret":"tab:cyan"}
dif=C["P"]-C["OD"]
C["dif"]=dif
'''Condicion que ajusta los datos de almacenamiento'''
cond=C["dif"]<10
C["periodo"][C.loc[cond,].index]=0
'''#################################################################################'''
'''Código de visión'''

for j in range (C["periodo"].size):
    if j>1 and j<(C["periodo"].size-2):
        if C["periodo"][j-2]==C["periodo"][j+2]:
            C["periodo"][j-1]=C["periodo"][j+2]
            C["periodo"][j]=C["periodo"][j+2]
            C["periodo"][j+1]=C["periodo"][j+2]

'''Genera el entorno de graficación, tomando de un directorio colors, las etiquetas y el color que le corresponde a cada uno'''
INCP=plt.plot(C["T"],C["P"],marker='+', color ="indigo",label="INCP")
m=0
for i in colors:
    if C.loc[C["periodo"]==m]["OD"].size>3:
        Graphicer=plt.scatter(C.loc[C["periodo"]==m]["T"],C.loc[C["periodo"]==m]["OD"],marker='o', color =colors[i],label=i)
    m=m+1    

'''Formato del fráfico'''
plt.title(NOMBRE +'\n'+ 'Diagnóstico')
leg = plt.legend()
leg.get_frame().set_facecolor('#fafafa')
plt.ylabel("DP")
plt.xlabel("t (h)")
plt.xscale('log')
plt.yscale('log')
plt.xticks(rotation=90)
plt.savefig("Diagnostico"+ NOMBRE+".png")
plt.show()

'''###############################################################################'''
'''Realiza el análisis MDH'''
y=(C.loc[C["periodo"]==2]["Plect"])
x=(C.loc[C["periodo"]==2]["T"])
def funMDH (x,A,C):
            return (A*np.log(x)+C)
'''Algo'''
popt, pcov = curve_fit(funMDH, x, y)
MDHPRE=funMDH(C["T"],*popt)

#print (AGPrediction)
RR=funMDH(1,*popt)-funMDH(10,*popt)
DAta=plt.plot(C["T"],C["Plect"],marker='', color ='blue',label="Datos")
#print (C.loc[C["periodo"]==2]["T"])
#ajuste=plt.plot(C.loc[C["periodo"]==2]["T"],AGPRE,marker='',ls='solid',color='olive',label="Ajuste")
ajuste=plt.scatter(C["T"],MDHPRE,marker='*',ls='solid',color='olive',label="m="+str(RR))
Poneh=(funMDH(1,*popt))
'''Evaluar Kh'''
print(RR)
Q=float (input('enter the Q in BPD\t: '))
B=float (input('enter the Bo\t: '))
Mu=float (input('enter the mu,cp \t: '))
h=float (input('enter h,ft \t: '))
CT=float(input('enter ct, $psi^-1$: '))
phi=float(input('enter phi: '))
wr=float(input('enter wr,ft: '))
K=((162.6/(RR))*(Q*B*Mu))/h


plt.title(NOMBRE +'\n'+ 'MDH IARF')
leg = plt.legend()
leg.get_frame().set_facecolor('#fafafa')
plt.ylabel("P psia")
plt.xlabel("t (h)")
plt.xscale('log')
#plt.yscale('log')
plt.xticks(rotation=90)
plt.savefig("MDH"+ NOMBRE+".png")
plt.show()
'''##################################################################################'''
'''Análisis del almacenamiento''' 
storagey=(C.loc[C["periodo"]==0]["P"])
storagex=(C.loc[C["periodo"]==0]["T"])
def funSTR (storagex,A,C):
            return (A*(storagex)+C)

popt, pcov = curve_fit(funSTR,(storagex[1:]),(storagey[1:]))
D=(0.234/5.615)*(2500*1.21)*(1/((funSTR(1,*popt))))
STRPRE=funSTR(C["T"][1:20],*popt)
StorageData=plt.plot(C["T"],C["P"],marker='', color ='blue',label="Datos")
StorageAjust=plt.plot(C["T"][1:20],STRPRE,marker='*',ls='solid',color='olive',label="C="+str (D))

'''DAÑo'''
S=1.151*(((C["Plect"][0]-Poneh)/abs(RR))-np.log(K/(phi*Mu*CT*(wr**2)))+3.2274)
#print(funMDH(1,*popt))
plt.title(NOMBRE +'\n'+ 'Almacenamiento')
leg = plt.legend()
leg.get_frame().set_facecolor('#fafafa')
plt.ylabel("DP")
plt.xlabel("t (h)")
plt.xscale('log')
plt.yscale('log')
plt.xticks(rotation=90)
plt.savefig("Almacenamiento"+ NOMBRE+".png")
plt.show()

'''#################################################################################'''
'''Escribir el reporte'''

titulo="Reporte: "+ NOMBRE 
seccion1="Secciones"
seccion2="IARF"
pdf=canvas.Canvas("Reporte"+NOMBRE+".pdf")
pdf.setTitle("Reporte"+NOMBRE)
#Write title 
pdf.drawCentredString(300,770,titulo)
#Ajustar el color del siguiente texto 
pdf.setFillColorRGB(0,0,255)
pdf.drawCentredString(80,730,"Propiedades del fluido:")
pdf.drawCentredString(400,730,"Propiedades del Yacimiento:")
#Dibujar una linea 
pdf.line(20,727,550,727)
#pdf.setFillColorRGB (0,0,255)
pdf.setFillGray(0)
pdf.drawString(20,710,"qo BPD: "+str(Q))
pdf.drawString(20,690,"Bo, bbl/STB: "+str(B))
pdf.drawString(20,670,"Ct, 10^-6 psi: "+str(CT))
pdf.drawString(20,650,"Viscosidad, cp: "+str(Mu))
############################################################################
pdf.drawString(340,710,"Porosidad: "+str(phi))
pdf.drawString(340,690,"Radio de pozo, ft :"+str(wr))
pdf.drawString(340,670,"Espesor h, ft :"+str(h))
############################################################################
pdf.setFillColorRGB(0,0,255)
pdf.drawCentredString(40,630,"Gráficos:")
pdf.line(20,625,550,625)
#########################################################################
pdf.drawImage("Diagnostico"+ NOMBRE+".png", 20,370, width=3.5*inch,height=3*inch,mask=None)
pdf.drawImage("MDH"+ NOMBRE+".png", 320,370, width=3.5*inch,height=3*inch,mask=None) 
pdf.drawImage("Almacenamiento"+ NOMBRE+".png", 20,150, width=3.5*inch,height=3*inch,mask=None) 
############################################################################
pdf.setFillColorRGB(0,0,255)
pdf.drawCentredString(80,140,"Propiedades Evaluadas:")
pdf.line(20,135,550,135)
#########################################################################
pdf.setFillGray(0)
pdf.drawString(20,100,"Permeabilidad, k md: "+ str(K))
pdf.drawString(20,80,"Almacenamiento, C bbl/psi: "+str(D))
pdf.drawString(20,60,"Daño, s : "+str(S))

pdf.save() 


