from flask import Flask,render_template
import requests
import json
from bs4 import BeautifulSoup
from csv import writer

app= Flask(__name__)

@app.route('/')
def get_beer():
    r=requests.get('https://ifarm360.com')
    beerjson=r
    print(beerjson)
    return render_template("index.html")

response=requests.get('https://ifarm360.com')

     
soup=BeautifulSoup(response.text, 'lxml')

posts=soup.find_all("div", class_='post-preview')

with open('posts.csv','w') as csv_file:
    csv_writer=writer(csv_file)
    headers=('title','link','date')
    csv_writer.writerow(headers)

    for post in posts:
        title=post.find(class_=('post-title').get_text().replace("\n","")
        Link=post.find('a')['href']
        date=post.select('.post-date')[0].get_text()
        csv_writer.writerow(['title','link','date'])
        print(title,link,date)