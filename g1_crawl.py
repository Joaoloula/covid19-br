from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
)
from time import sleep
from tqdm import tqdm
from os import path
import pickle
import csv

year = 2020
month = 3
start_day = 22
current_day = 22

month_number_to_name = {3: "marco", 2: "fevereiro"}

url_template = "https://g1.globo.com/bemestar/coronavirus/noticia/{}/{:02d}/{:02d}/casos-de-coronavirus-no-brasil-em-{:02d}-de-{}.ghtml"
file_template = "data/g1_{}{:02d}{:02d}.csv"

# g1 starts reporting tables on March 17th
dates = [(year, month, day, day, month_number_to_name[month]) for day in range(start_day, current_day + 1)]

options = Options()
options.add_argument("--headless")
browser = webdriver.Firefox(options=options)

for date in dates:
    url = url_template.format(*date)
    browser.get(url)
    table = browser.find_element_by_css_selector("tbody")
    with open(file_template.format(*date[:3]), 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for row in table.find_elements_by_css_selector('tr'):
            wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
