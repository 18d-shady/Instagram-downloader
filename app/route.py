from flask import render_template, request
import requests
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from app import app


@app.route('/')
def index():
	return render_template("index.html")

#get the link from the first webpage 
#and get the picture from there


@app.route('/download', methods=['POST'])
def index_2():

	linkk = request.form.get('linkk')
	#req = requests.get(linkk)
	driver = webdriver.Chrome(executable_path='C:/Users/VERA OLEHI/Downloads/chromedriver_win32/chromedriver.exe')
	driver.get(linkk)
	soup = BeautifulSoup(driver.page_source, "html.parser")
	imagen = soup.find("meta", attrs={"property": "og:image"})['content']
	response = requests.get(imagen)
	file = open("C:/Users/VERA OLEHI/Downloads/sample_image.png", "wb")
	file.write(response.content)
	file.close()
	return render_template("download.html", sourcee=imagen)
	
	
	
	
	


"""
@app.route('/download', methods=['GET'])
def download():
	
	url = request.form['linkk']
	req = requests.get(url)
	soup = BeautifulSoup(req.text, "html.parser")
	imagen = soup.find("meta", attrs={"property": "og:image"})
	sourcee = imagen['content']
	return render_template("download.html")

"""