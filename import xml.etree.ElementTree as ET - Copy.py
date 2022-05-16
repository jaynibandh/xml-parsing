from os import remove
import xml.etree.ElementTree as ET
import re
import csv
from bs4 import BeautifulSoup

f = open("patent.txt", "r",encoding="utf-8")
dict={}

title=[]
fan=[]
cpc=[]
clms=[]
desc=[]
pdg=[]
ab=[]
titlev=[]
fanv=[]
cpcv=[]
clmsv=[]
descv=[]
pdgv=[]
abv=[]