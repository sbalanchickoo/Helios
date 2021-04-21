from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("C:/Users/globetrekker/Downloads/chromedriver_win32/chromedriver")

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://online.hl.co.uk/my-accounts/security_details/sedol/B8HTXL7")
time.sleep(40)

content = driver.page_source
soup = BeautifulSoup(content, features="html")
div = soup.find("div", {"id": "top-holdings"})
content = str(div)
print(content)

driver.get("https://online.hl.co.uk/my-accounts/security_details/sedol/B5N9956")
content = driver.page_source
soup = BeautifulSoup(content, features="html")
div = soup.find("div", {"id": "top-holdings"})
content = str(div)
print(content)
# mydivs = soup.find_all("div", id_="watchlists")
#d
# for div in soup.find_all("div", id_="top-holdings"):
#     print(div.text)
# for a in soup.findAll('a',href=True, attrs={'class':'watchlists'}):
#     with open('myOutFile_orig.txt', 'w', encoding="utf-8") as f:
#         print(soup, file=f)
# outF = open("myOutFile_orig.txt", "w")

# for line in soup:
#     outF.write(str(line))
#     outF.write("\n")

# with open('myOutFile_orig.txt', 'w', encoding="utf-8") as f:
#     print(soup, file=f)

# outF.close()


