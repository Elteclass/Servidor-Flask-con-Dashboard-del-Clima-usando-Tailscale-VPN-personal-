# 🌤️ Mini Dashboard del Clima con Flask y Tailscale

Este proyecto es una práctica para la materia de **Sistemas programables** que demuestra cómo crear un servidor web ligero con Flask para mostrar datos del clima en tiempo real, ejecutarlo en un teléfono Android/iOS usando Termux y acceder a él de forma remota y segura desde cualquier dispositivo a través de una VPN personal con Tailscale.

---

## 🎯 Objetivo Principal

Construir un sistema funcional donde un teléfono móvil actúa como servidor, consultando la API de OpenWeatherMap para obtener datos del clima y presentarlos en un dashboard web dinámico. El acceso desde un PC u otro dispositivo se realiza de manera segura a través de la red privada virtual de Tailscale, sin necesidad de exponer el servidor directamente a internet.

---

## ✨ Características

- **Servidor Ligero**: Utiliza Flask, un micro-framework de Python ideal para aplicaciones pequeñas y rápidas.
- **Datos en Tiempo Real**: Se conecta a la API de OpenWeatherMap para obtener la información más reciente del clima para una ciudad específica (Tijuana por defecto).
- **Dashboard Dinámico**: La interfaz web, estilizada con Tailwind CSS, cambia su gradiente de color de fondo para reflejar la condición climática actual (soleado, nublado, lluvia, etc.).
- **Portabilidad Extrema**: El servidor está diseñado para correr directamente en un teléfono móvil mediante Termux.
- **Acceso Remoto y Seguro**: Implementa Tailscale para crear una red VPN privada y segura, permitiendo el acceso al dashboard desde cualquier otro dispositivo en la misma red sin configuraciones complejas de puertos o IP públicas.

---

## 🛠️ Tecnologías Utilizadas

| Componente       | Tecnología               |
|------------------|--------------------------|
| Backend          | Python 3, Flask          |
| Frontend         | HTML, Tailwind CSS       |
| Datos            | API de OpenWeatherMap    |
| Plataforma Móvil | Termux (Android/iOS)     |
| Redes            | Tailscale VPN            |

---

## 🚀 Puesta en Marcha

El proceso general es el siguiente:

1. **Configuración del Entorno**: Instalar Python y las dependencias (`Flask`, `requests`) en Termux dentro de un entorno virtual.
2. **API Key**: Obtener una clave de API gratuita de OpenWeatherMap y colocarla en el archivo `app.py`.
3. **Configuración de Red**: Instalar y configurar Tailscale tanto en el teléfono (servidor) como en el dispositivo cliente (PC, laptop, etc.).
4. **Ejecución**: Iniciar el servidor Flask en el teléfono.
5. **Acceso**: Abrir un navegador en el dispositivo cliente y acceder al dashboard usando la IP de Tailscale del teléfono y el puerto `5000`.

---

## 📸 Evidencias de Realización

- [**Terminal en Termux (Asciinema)**](https://asciinema.org/a/gRII9OJYxPj9GJD57AwaAtJH4): Grabación completa de la sesión en la terminal, desde la instalación de dependencias hasta la ejecución del servidor.
- [**Video de Demostración (Loom)**](https://www.loom.com/share/a33330efdb2c4d848fd2097a58d38bdc?sid=26112b54-7802-4151-8a81-5e9618ab85ce): Un video corto que muestra el dashboard en acción y su acceso remoto desde el PC.
- **Captura con Otras Ciudades**:
<img width="1594" height="773" alt="image" src="https://github.com/user-attachments/assets/6c095f12-b6a2-4216-ae2f-99272f42551d" />
<img width="1594" height="774" alt="image" src="https://github.com/user-attachments/assets/2a1ba4c6-60d1-4f7e-b9a4-bd878fbd393f" />
<img width="1596" height="776" alt="image" src="https://github.com/user-attachments/assets/27e8862b-dc67-441e-85c1-b30d32d57f99" />
<img width="1599" height="777" alt="image" src="https://github.com/user-attachments/assets/4b9ca6a1-ec60-481d-b121-7e1b187f4d81" />


---

## 🤖 Asistencia de IA

Para la estilización con Tailwind CSS y la elaboración de esta documentación, se utilizó la asistencia de la inteligencia artificial **Gemini de Google**.

---

**Autor**: Jaime Antonio Alvarez Crisostomo  
**Institución**: TECNM / Instituto Tecnológico de Tijuana  
**Materia**: Sistemas Programables  
**Año**: 2025
