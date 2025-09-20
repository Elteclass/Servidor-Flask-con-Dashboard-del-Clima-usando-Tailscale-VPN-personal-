# ╔═══════════════════════════════════════════════════════════════╗
# ║        🌤️ Mini Dashboard del Clima con Flask + Tailscale       ║
# ║        Sistemas Programables - TECNM / ITT - 2025               ║
# ║        Autor: Jaime Antonio Alvarez Crisostomo                  ║
# ║        Descripción: Servidor Flask consultando OpenWeatherMap ║
# ╚═══════════════════════════════════════════════════════════════╝

from flask import Flask, render_template_string # Flask para el servidor web y render_template_string para usar HTML desde una variable.
import requests  # Para hacer la petición a la API del clima.
import datetime  # Para mostrar la fecha actual en el dashboard.

# Inicio mi aplicación Flask.
app = Flask(__name__)

# --- Mi Configuración Personal ---
# Clave de la API y la ciudad que se quiere consultar.
API_KEY = "48e2797b0f9b3ac46c4f15532ad439ae"
CITY = "Tijuana"
AUTHOR_NAME = "Jaime Antonio Alvarez Crisostomo"

# --- Plantilla HTML con Tailwind CSS ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard del Clima - {{ city }}</title>
    <!-- Aquí incluyo Tailwind CSS para que se vea moderno sin necesidad de un archivo CSS. -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Definí mis propios gradientes para el fondo. Cambian según el clima. */
        .bg-clear { background: linear-gradient(to top, #4facfe 0%, #00f2fe 100%); }
        .bg-clouds { background: linear-gradient(to top, #cfd9df 0%, #e2ebf0 100%); }
        .bg-rain { background: linear-gradient(to top, #6b7280 0%, #4b5563 100%); }
        .bg-thunderstorm { background: linear-gradient(to top, #2c3e50 0%, #4b5563 100%); }
        .bg-snow { background: linear-gradient(to top, #e6dada 0%, #ffffff 100%); }
        .bg-mist { background: linear-gradient(to top, #d3d3d3 0%, #f5f5f5 100%); }
        .bg-default { background: linear-gradient(to top, #89f7fe 0%, #66a6ff 100%); }
    </style>
</head>
<!-- El body tiene una clase especial {{ weather_bg_class }} que cambiará el fondo dinámicamente. -->
<body class="min-h-screen flex flex-col items-center justify-center font-sans p-4 {{ weather_bg_class }} transition-all duration-500">

    <!-- Esta es la tarjeta principal donde muestro toda la información. -->
    <div class="w-full max-w-md bg-white/30 backdrop-blur-md rounded-2xl shadow-2xl p-6 text-center text-gray-800">
        <h1 class="text-3xl font-bold mb-2">Clima en {{ city }}</h1>
        <p class="text-sm text-gray-700 mb-4">{{ date }}</p>

        <!-- Si ocurre un error, muestro una alerta en lugar de los datos del clima. -->
        {% if error %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-lg" role="alert">
              <strong class="font-bold">¡Error!</strong>
              <span class="block sm:inline">{{ error }}</span>
            </div>
        {% else %}
            <!-- Si todo sale bien, muestro el ícono, la temperatura y la descripción. -->
            <div class="flex items-center justify-center my-4">
                <img src="http://openweathermap.org/img/wn/{{ icon }}@2x.png" alt="Icono del clima" class="w-24 h-24">
                <p class="text-6xl font-extrabold ml-4">{{ temp }}°C</p>
            </div>
            <p class="text-2xl capitalize font-semibold mb-6">{{ description }}</p>

            <!-- Aquí organicé los detalles adicionales en una cuadrícula. -->
            <div class="grid grid-cols-2 gap-4 text-left bg-white/20 p-4 rounded-lg">
                <div>
                    <p class="font-bold">Sensación Térmica:</p>
                    <p>{{ feels_like }}°C</p>
                </div>
                <div>
                    <p class="font-bold">Humedad:</p>
                    <p>{{ humidity }}%</p>
                </div>
                <div>
                    <p class="font-bold">Viento:</p>
                    <p>{{ wind_speed }} m/s</p>
                </div>
                 <div>
                    <p class="font-bold">Presión:</p>
                    <p>{{ pressure }} hPa</p>
                </div>
            </div>
        {% endif %}
    </div>

    <!-- El pie de página con mi nombre. -->
    <footer class="mt-8 text-white/80 text-center text-sm">
        <p>Desarrollado por: <span class="font-semibold">{{ author }}</span></p>
        <p>Lenguajes de Interfaz - TECNM / ITT - 2025</p>
    </footer>

</body>
</html>
"""

# HFuncion que see encarga de hacer la llamada a la API.
def get_weather_data(city, api_key):
    """Obtiene los datos del clima desde la API de OpenWeatherMap."""
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es"
    try:
        # Intento de conectarse a la URL con un tiempo de espera de 10 segundos.
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Esto es útil porque si la API devuelve un error (ej. 404 o 500), el programa se detiene aquí y pasa al 'except'.
        return response.json(), None # Si todo sale bien, se devuelven los datos en formato JSON y 'None' para el error.
    except requests.exceptions.RequestException as e:
        # Si no se puede conectar, se devuelve 'None' para los datos y un mensaje de error claro.
        return None, f"No se pudo conectar con el servicio del clima: {e}"
    except Exception as e:
        # Por si ocurre cualquier otro error inesperado.
        return None, f"Ocurrió un error inesperado: {e}"

# Esta función ayuda a elegir qué clase CSS de fondo usar según el clima.
def get_background_class(weather_main):
    """Determina la clase CSS para el fondo según el clima."""
    # Es un diccionario que mapea la condición principal del clima (que viene en inglés) con el nombre de la clase CSS que definí arriba.
    return {
        "Clear": "bg-clear",
        "Clouds": "bg-clouds",
        "Rain": "bg-rain",
        "Drizzle": "bg-rain",
        "Thunderstorm": "bg-thunderstorm",
        "Snow": "bg-snow",
        "Mist": "bg-mist",
        "Fog": "bg-mist",
    }.get(weather_main, "bg-default") # Si la condición no está en mi diccionario, uso una por defecto.

@app.route("/")
def weather_dashboard():
    """Esta es la función principal que se ejecuta para mostrar el dashboard."""
    # Se llama la función para obtener los datos del clima. Me devuelve los datos y un posible error.
    data, error = get_weather_data(CITY, API_KEY)
    
    # Si la función devuelve un error, se pasa ese error a la plantilla HTML para que lo muestre.
    if error:
        return render_template_string(HTML_TEMPLATE, city=CITY, author=AUTHOR_NAME, error=error, date=datetime.datetime.now().strftime("%A, %d de %B de %Y"))

    if data and data.get("cod") == 200:
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        wind = data.get("wind", {})
        
        weather_main = weather.get("main")
        
        context = {
            "city": data.get("name", CITY),
            "temp": f"{main.get('temp', 0):.1f}",
            "feels_like": f"{main.get('feels_like', 0):.1f}",
            "humidity": main.get('humidity', 0),
            "pressure": main.get('pressure', 0),
            "description": weather.get("description", "No disponible"),
            "icon": weather.get("icon", "01d"),
            "wind_speed": wind.get('speed', 0),
            "author": AUTHOR_NAME,
            "weather_bg_class": get_background_class(weather_main),
            "date": datetime.datetime.now().strftime("%A, %d de %B de %Y"),
            "error": None
        }
        return render_template_string(HTML_TEMPLATE, **context)
    else:
        # Si la API devolvió una respuesta pero no es válida, muestra un error.
        error_message = data.get("message", "Respuesta inválida de la API.")
        return render_template_string(HTML_TEMPLATE, city=CITY, author=AUTHOR_NAME, error=error_message, date=datetime.datetime.now().strftime("%A, %d de %B de %Y"))

# Punto de entrada del programa
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


