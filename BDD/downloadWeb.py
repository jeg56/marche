# -*- coding: UTF8 -*-
from selenium import webdriver
import time
import xlsxwriter
from bs4 import BeautifulSoup
import codecs
import re
import urllib.request
import dload

def readFile(path):
        fichier = open(path,"r")
        file = fichier.read()
        #return ligne
        fichier.close()

def writeFile(texte,path):
        fichier = open(path,"wb")
        fichier.write(texte.encode('utf-8'))
        fichier.close()

def writeFileAppend(texte,path):
        fichier = open(path,"a+b")
        fichier.write(texte.encode('utf-8'))
        fichier.close()
 

def downloadWebPage():
   browser = webdriver.Chrome(executable_path=r"C:\\Users\\frup68962\\Downloads\\chromedriver_win32\\chromedriver.exe")
   init=0

   for x in range(1,460):
      browser.get("http://annuaire.marchesdefrance.fr/liste-des-marches/page/{}".format(x))
      time.sleep(5)
      soup=BeautifulSoup(browser.page_source,'lxml')
      
      writeFile(soup.prettify(),'D:\\pmu\\Package\\data\\source.html')

      file = codecs.open('D:\\pmu\\Package\\data\\source.html', 'r','utf-8')
      
      topFlag=0
      infosMarche=''
      
      for line in file:
         if re.search(r'.*?((<div class="contentList">)(.*?))', line):
            topFlag=1
  
         if topFlag==1:
            infosMarche+=line
    
         if re.search(r'.*?((<div class="clear">)(.*?))', line) and topFlag==1:
        
            decoupage=re.search(r'.*?((<a href=")(.*?)(">))', infosMarche).group(1)
            print('{}-{}' .format(x,decoupage))
            url=decoupage.replace('<a href="','').replace('">','')
            if init==0:
               writeFile(url+'\n','D:\\pmu\\Package\\data\\Liste_Url.csv')
               init=1
            else:
               writeFileAppend(url+'\n','D:\\pmu\\Package\\data\\Liste_Url.csv')


            topFlag=0
            infosMarche=''
   
           
         
      
#downloadWebPage()

def downmloadMarket():
   browser = webdriver.Chrome(executable_path=r"C:\\Users\\frup68962\\Downloads\\chromedriver_win32\\chromedriver.exe")
   init=0
   marche = codecs.open('D:\\pmu\\Package\\data\\Liste_Url.csv', 'r','utf-8')
   for url in marche:
      print(url)
   
      browser.get(url)
      time.sleep(5)
      soup=BeautifulSoup(browser.page_source,'lxml')
      
      writeFile(soup.prettify(),'D:\\pmu\\Package\\data\\source_market.html')
      file = codecs.open('D:\\pmu\\Package\\data\\source_market.html', 'r','utf-8')
      topFlag=0
    
      infosMarche=''
      
      for line in file:
         if re.search(r'.*?((<section class="SingleMarcheResult">)(.*?))', line):
            topFlag=1
  
         if topFlag==1:
            infosMarche+=line.strip()
    
         if re.search(r'.*?((<div class="clear">)(.*?))', line) and topFlag==1:
            topFlag=0

      nomMarket=re.search(r'.*?((<a>)(.*?)(</a>))', infosMarche).group(3)
      print('{}' .format(nomMarket))
   
      Freq=re.search(r'.*?((<li><span class="iconSingleFrequence"></span><br/>)(.*?)(</li>))', infosMarche).group(3)
      print('{}' .format(Freq))

      dateMarket=re.search(r'.*?((<li><span class="iconSingleDate"></span><br/>)(.*?)(</li>))', infosMarche).group(3)
      print('{}' .format(dateMarket))

      nbre=re.search(r'.*?((<li><span class="iconSingleExposants"></span><br/>)(.*?)(<label>))', infosMarche).group(3)
      print('{}' .format(nbre))

      adres=re.search(r'.*?((<li><span class="iconSinglePlace"></span><br/>)(.*?)(</li>))', infosMarche).group(3)
      print('{}' .format(adres))

      typeProd=re.search(r'.*?((<li class="lastInfosHead"><span class="iconSingleCatMarche"></span><br/>)(.*?)(</li>))', infosMarche).group(3)
      print('{}' .format(typeProd))


      nbData=len(re.findall(r'.*?((<li)(.*?)(</li>))', infosMarche))
      
      if init==0:
         writeFile('{};{};{};{};{};{};{};{}\n'.format(url.strip(),nomMarket,Freq,dateMarket,nbre,adres,typeProd,nbData),'D:\\pmu\\Package\\data\\data.csv')
         init=1
      else:
         writeFileAppend('{};{};{};{};{};{};{};{}\n'.format(url.strip(),nomMarket,Freq,dateMarket,nbre,adres,typeProd,nbData),'D:\\pmu\\Package\\data\\data.csv')

         
def downmloadMarket_fruits():
   browser = webdriver.Chrome(executable_path=r"C:\\Users\\frup68962\\Downloads\\chromedriver_win32\\chromedriver.exe")

   browser.get("https://www.fruits-legumes.org/liste-fruits/")
   time.sleep(5)
   soup=BeautifulSoup(browser.page_source,'lxml')

   writeFile(soup.prettify(),'D:\\pmu\\Package\\data\\source.html')


def exploiteFruit():
   browser = webdriver.Chrome(executable_path=r"C:\\Users\\frup68962\\Downloads\\chromedriver_win32\\chromedriver.exe")
   file = codecs.open('D:\\pmu\\Package\\data\\source.html', 'r','utf-8')
   for line in file:
      if re.search(r'.*?((<a href=")(.*?)(onmouseout="document.getElementById))', line):
         listFruit=line.split('"')[1]
      
         browser.get("https://www.fruits-legumes.org/"+listFruit)
         time.sleep(5)
         soup=BeautifulSoup(browser.page_source,'lxml')

         writeFile(soup.prettify(),'D:\\pmu\\Package\\data\\fruits.html')
         
         filefruits = codecs.open('D:\\pmu\\Package\\data\\fruits.html', 'r','utf-8')
         
         for linefruits in filefruits:
            if re.search(r'.*?((<img alt=")(.*?)(.jpg"/>))', linefruits):
               nom=linefruits.split('"')[1]
               adres=linefruits.split('"')[3]
               print('{} - {}'.format(nom,adres))
               resource = urllib.request.urlretrieve("https://www.fruits-legumes.org/"+adres,"C:\\Images\\" +nom+".jpg")
   
               dload.save("https://www.fruits-legumes.org/"+adres)
               print("https://www.fruits-legumes.org/"+adres)



      
def downmloadMarket_legumes():
   browser = webdriver.Chrome(executable_path=r"C:\\Users\\frup68962\\Downloads\\chromedriver_win32\\chromedriver.exe")

   browser.get("https://www.fruits-legumes.org/liste-legumes/")
   time.sleep(5)
   soup=BeautifulSoup(browser.page_source,'lxml')

   writeFile(soup.prettify(),'D:\\pmu\\Package\\data\\source.html')


def exploiteLegumes():
   browser = webdriver.Chrome(executable_path=r"C:\\Users\\frup68962\\Downloads\\chromedriver_win32\\chromedriver.exe")
   file = codecs.open('D:\\pmu\\Package\\data\\source.html', 'r','utf-8')
   for line in file:
      if re.search(r'.*?((<a href=")(.*?)(onmouseout="document.getElementById))', line):
         listFruit=line.split('"')[1]
      
         browser.get("https://www.fruits-legumes.org/"+listFruit)
         time.sleep(5)
         soup=BeautifulSoup(browser.page_source,'lxml')

         writeFile(soup.prettify(),'D:\\pmu\\Package\\data\\legumes.html')
         
         fileLegumes = codecs.open('D:\\pmu\\Package\\data\\legumes.html', 'r','utf-8')
         
         for linelegumes in fileLegumes:
            if re.search(r'.*?((<img alt=")(.*?)(.jpg"/>))', linelegumes):
               nom=linelegumes.split('"')[1]
               adres=linelegumes.split('"')[3]
               print('{} - {}'.format(nom,adres))
               resource = urllib.request.urlretrieve("https://www.fruits-legumes.org/"+adres,"C:\\Images\\" +nom+".jpg")
   
               dload.save("https://www.fruits-legumes.org/"+adres)
               print("https://www.fruits-legumes.org/"+adres)

downmloadMarket_legumes()
exploiteLegumes()