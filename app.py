import json, requests, sys,bs4
import json
import os

from flask import Flask, render_template, json, request
from flask import request
from flask import make_response
from random import choice, randint

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return 'Hello Hoang'


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    url = 'https://7monngonmoingay.net/page'+ str(randint(1,290))
    print('Url: %s...' % (url))
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    mainthing = soup.find(id='content')
    first_link = mainthing.find_all('a')
    link = choice(first_link)
	link = link['href']
	res = {'fulfillmentText': link}
    return res

if __name__ == '__main__':
    app.run()