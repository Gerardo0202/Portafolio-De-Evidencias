import requests, time
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

def noticias(pag):
    try:
        libro= Workbook()
        pa=libro.active
        pa.title="Noticias"
        pa["A1"]="Titulos"
        print("Se logro")
    except:
        print("No se pudo crear")
        
    count=2
    url=pag
    pagina=requests.get(url)
    if pagina.status_code==200:
        print("Pagina encontrada")
        soup=bs(pagina.content,"html.parser")
        info=soup.find_all("h2")
        i=0
        libro.active=0
        for title in info:
            po=info[i].getText()
            pa.cell(count,1,po)
            print(po)
            i=i+1
            count+=1
    libro.save("Noticias.xlsx")
    
if __name__=="__main__":
    pagina="https://www.milenio.com/temas/daniel-corral"
    noticias(pagina)
