from flask import Flask,render_template
import requests 
from dotenv import load_dotenv,dotenv_values 


config = dotenv_values('.env')


app = Flask(__name__)

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=es&units=metric'
    r = requests.get(url).json()
    print(r)
    return r

@app.route('/Prueba')
def Prueba():
    Clima= get_weather_data('nobol')
    temperatura=str (Clima['main']['temp'])
    descripcion=str (Clima['weather'][0]['description'])
    icono=str (Clima['weather'][0]['icon'])

    r_json={
        'ciudad': 'nobol',
        'temperatura':temperatura,
        'descripcion':descripcion,
        'icono':icono
    }
    return render_template ('weather.html', Clima= r_json)

@app.route('/wen')
def wen():
    return get_weather_data('nobol')


@app.route('/weather')
def weather():
    return render_template('weather.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Clima')
def Clima ():
    return 'saber del clima es importante'

if __name__ == '__main__':
    app.run(debug=True)