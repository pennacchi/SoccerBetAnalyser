
# site exemplo: site.com/.../{ano}/{numeroJogo}
# https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2019/228
# Classe dados time casa (DTC): <div class="col-xs-6 col-sm-3 text-center time-left"> </div>
# Nome time casa: (dentro da classe DTC): <H3 CLASS="time-nome color-white">
# Gols time casa: dentro da div, dentro do strong: <div class="time-escudo center-block m-t-10 m-b-30"> <strong class="time-gols block hidden-sm hidden-md hidden-lg">0</strong></div>
# DIV dados time visitante (DTV): <div class="col-xs-6 col-sm-3 text-center time-right"></div>
# Nome time visitante: (dentro da classe DTV):<h3 class="time-nome color-white">Flamengo - RJ</h3>
# Gols time visitante: <strong class="time-gols block hidden-sm hidden-md hidden-lg">1</strong>
# Cabeçalho - Data do jogo: <header class="section-content-header p-t-10 p-b-10 m-b-30"><div class="row"><div class="col-sm-8"><span class="text-2 p-r-20">
# Data do jogo: exitem 2 spans nesse cabeçalho, é o segundo span : <span class="text-2 p-r-20"><i aria-hidden="true" class="glyphicon glyphicon-calendar"></i> Domingo, 06 de Outubro de 2019</span>
# uma outra opção para pegar a data é pegar o próximo item após a class "glyphicon glyphicon-calendar"
# É necessário fazer tratamento da data 

from bs4 import BeautifulSoup
import requests
from datetime import datetime
from dateutil import parser
import converte_datetime_pt as dataPT
import xlsxwriter


# CRIANDO PLANILHA
workbook = xlsxwriter.Workbook('Jogos.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'DATA')
worksheet.write('B1', 'TIME CASA')
worksheet.write('C1', 'GOLS CASA')
worksheet.write('D1', 'TIME VISITANTE')
worksheet.write('E1', 'GOLS VISITANTE')
linhaPlanilha = 1

# EXTRAINDO DADOS

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}

for ano in range (2017, 2021):
    for i in range(1, 381):
        iteracao = str(i)

        url = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/"+str(ano)+"/"+iteracao
        print(url)
        
        site = requests.get(url, headers=headers)

        soup = BeautifulSoup(site.content, 'html.parser')

        nomeTimeCasa = soup.find_all('h3', class_='time-nome')[0].get_text()
        golsTimeCasa = soup.find_all('strong', class_='time-gols')
        if len(golsTimeCasa) == 0:
            print("WO")

            continue
        else:
            golsTimeCasa = golsTimeCasa[1].get_text()
        
        

        nomeTimeVisitante = soup.find_all('h3', class_='time-nome')[1].get_text()
        golsTimeVisitante = soup.find_all('strong', class_='time-gols')
        if len(golsTimeVisitante) == 0:
            print("WO")
            continue
        else:
            golsTimeVisitante = golsTimeVisitante[3].get_text()

        dataJogo = soup.find_all('span', class_='text-2 p-r-20')[1].get_text().strip()
        dataJogo = dataPT.parse_pt_date(dataJogo)

        print('pagina: ' + iteracao)
        print(nomeTimeCasa + ' gols: ' + golsTimeCasa)
        print(nomeTimeVisitante+ ' gols: ' + golsTimeVisitante)

        linhaPlanilha = linhaPlanilha+1

        worksheet.write('A'+str(linhaPlanilha), dataJogo)
        worksheet.write('B'+str(linhaPlanilha), nomeTimeCasa)
        worksheet.write('C'+str(linhaPlanilha), int(golsTimeCasa))
        worksheet.write('D'+str(linhaPlanilha), nomeTimeVisitante)
        worksheet.write('E'+str(linhaPlanilha), int(golsTimeVisitante))
        
workbook.close()
