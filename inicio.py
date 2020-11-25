import requests
import lxml.html as html
from ScrapingPIM.test import get_doc_text

registrosAbuscar=["xxxx"]
salida = open("Salida.txt", "a")


def openUrl():
    try:
        pageIni=requests.get('xxx', auth=('user', 'pass'))
        print(pageIni.status_code)
        if pageIni.status_code==200:
          home=pageIni.content.decode('utf-8')
          parseHome=html.fromstring(home)
          Archivos=parseHome.xpath('//a/@href')
          for n in range(len(Archivos)):
             print(Archivos[n])
             rawImage= requests.get('xxxx'+Archivos[n], auth=('user', 'pass'),stream=True)
             print(rawImage.status_code)
             if Archivos[n].find('docx')>-1:
               generaArchivo(rawImage,'docx',Archivos[n])
             else:
               generaArchivo(rawImage, 'doc',Archivos[n])
          salida.close()
        else:
          raise Exception(f'Error: {pageIni.status_code}')
    except Exception as ex:
        print(ex)

def generaArchivo(rawImage,extend,archivo):
    with open('archivo.'+extend, 'wb') as fd:
        for chunk in rawImage.iter_content(chunk_size=1024):
            fd.write(chunk)
    BuscaEnArchivoDocx(extend, archivo)

def BuscaEnArchivoDocx(extend,archivo):
    text=get_doc_text('ScrapingPIM\\','archivo.'+extend)
    for x in registrosAbuscar:
     if text.lower().find(x.lower()) > -1:
        reg=(f'El registro: {x} \n Se encuentra en el documento:{archivo}\n')
        print(reg)
        salida.write(reg)


if __name__=='__main__':
    openUrl()