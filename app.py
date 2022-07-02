from unittest.mock import create_autospec
from flask import Flask, render_template, request
import pickle
#import numpy as np
import sklearn as sns
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', my_title = 'Home')

@app.route('/about')
def about():
    return render_template('about.html', my_title = 'About')

@app.route('/contact')
def contact():
    return render_template('contact.html', my_title = 'Contact')

@app.route('/project')
def project():
    return render_template('project.html', my_title = 'Project')

@app.route('/form')
def form():
    return render_template('form.html', my_title = 'form')

@app.route('/validate', methods= ['post'])
def validate():
    with open('gdprfr_model_pkl','rb') as f:
        lr = pickle.load(f)
    
    population = int(request.form.get('population'))
    area = int(request.form.get('area'))
    popdensity = float(request.form.get('popdensity'))
    coastline = float(request.form.get('coastline'))
    netmargin = float(request.form.get('netmigration'))
    infant = float(request.form.get('infant'))
    literacy = float(request.form.get('literacy'))
    phones = float(request.form.get('phones'))
    arables = float(request.form.get('arables'))
    crops = float(request.form.get('crops'))
    other = float(request.form.get('other'))
    climate = float(request.form.get('climate'))
    birthrates =float(request.form.get('birthrate'))
    deathrates = float(request.form.get('deathrate'))
    agriculture = float(request.form.get('agriculture'))
    industry = float(request.form.get('industry'))
    service = float(request.form.get('service'))
    regional_label = int(request.form.get('regional_label'))
    climate_label = int(request.form.get('climate_label'))
    #new_input = np.array([[population, area, popdensity, coastline, netmargin, infant, literacy, phones, arables, crops, other, climate, birthrates, deathrates, agriculture, industry, service, regional_label, climate_label]])
    new_input = [[population, area, popdensity, coastline, netmargin, infant, literacy, phones, arables, crops, other, climate, birthrates, deathrates, agriculture, industry, service, regional_label, climate_label]]
    result = lr.predict(new_input)
    

    #return str(result[0])
    return render_template('result.html',prediction=result[0], my_title = 'Result Page')





if __name__ == '__main__':
    app.run(debug = True)