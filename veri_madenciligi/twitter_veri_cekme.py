from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import os
import pandas as pd
import time

surucu_yolu=os.path.join(os.getcwd(),"veri_madenciligi","geckodriver")
ayarlar=FirefoxOptions()
# ayarlar.add_argument("--headless")
surucu= webdriver.Firefox(options=ayarlar,executable_path=surucu_yolu)
surucu.get(url="https://twitter.com/search?q=python&src=typed_query")
time.sleep(5)
icerik = surucu.page_source
# print(icerik)
duzenli = BeautifulSoup(icerik,"html.parser")#"lxml"
k=[]
t=[]
b=[]
adr=[]
zmn=[]

twitler= duzenli.find_all(name="div",attrs={"data-testid":"tweet"})
for a in twitler:
    kisi = a.find(name="div",attrs={"class":"css-901oao css-bfa6kz r-9ilb82 r-18u37iz r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-qvutc0"}).text
    twit = a.find(name="div",attrs={"class":"css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}).text
    begeni=a.find(name="div",attrs={"class":"css-1dbjc4n r-18u37iz r-1wtj0ep r-1s2bzr4 r-1mdbhws"}).get("aria-label").split(",")[-1]
    adres= a.find(name="a",attrs={"class":"css-4rbku5 css-18t94o4 css-901oao r-9ilb82 r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-3s2u2q r-qvutc0"})
    #print("kişi:",kisi,"beğeni sayısı:",begeni,"-adres:",adres.get("href"),"\n",twit)
    k.append(kisi)
    t.append(twit)
    b.append(begeni)
    adr.append(adres.get("href"))
    zmn.append(adres.find("time").get("datetime"))

veri = {"kisi":k,"zaman":zmn,"adres":adr,"twit":t,"begeni_sayisi":b}
veri=pd.DataFrame(veri)
veri.to_csv("twitler.csv",index=False)

