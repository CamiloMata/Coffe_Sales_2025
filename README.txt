☕ Dashboard de Ventas de Café
Este proyecto es un dashboard interactivo creado con Streamlit para visualizar y analizar datos de ventas de una tienda de café. El dashboard carga datos desde un archivo CSV y presenta las métricas clave en una interfaz web limpia e intuitiva.

📊 Vista Previa
(Aquí puedes añadir una captura de pantalla de tu dashboard en funcionamiento)

✨ Características Principales
El dashboard está dividido en dos secciones principales:

1. Resumen de Ventas Totales
Una vista de alto nivel que muestra las ventas totales (money) para cada día de la semana, presentadas como métricas (KPIs).

2. Análisis Detallado de Ventas
Un diseño de 2x2 con cuatro visualizaciones interactivas creadas con Plotly:

Ventas por Momento del Día: Un gráfico de pastel (dona) que muestra la distribución porcentual de las ventas (ej. Mañana, Tarde).

Tendencia de Ventas por Mes: Un gráfico de líneas que muestra la evolución de las ventas a lo largo de los meses.

Ventas por Hora del Día: Un gráfico de barras horizontal que detalla las ventas totales en cada hora operativa.

Ventas por Tipo de Café: Un gráfico de barras vertical que clasifica los tipos de café por sus ventas totales, permitiendo identificar los productos más populares.

Además, el script utiliza st.cache_data para optimizar la carga de datos, asegurando un rendimiento rápido incluso con datasets más grandes.

🛠️ Requisitos
Este proyecto requiere las siguientes bibliotecas de Python:

streamlit

pandas

plotly (específicamente plotly.express)

⚙️ Instalación
Asegúrate de tener Python 3.7 o superior instalado.

Instala las dependencias necesarias usando pip:

Bash

pip install streamlit pandas plotly
🚀 Cómo Ejecutar el Dashboard
Asegúrate de tener tu archivo de datos nombrado Coffe_sales.csv en la misma carpeta que el script coffe_dashboard.py.

Abre tu terminal o línea de comandos.

Navega al directorio donde se encuentra el archivo coffe_dashboard.py.

Ejecuta el siguiente comando:

Bash

streamlit run coffe_dashboard.py
Streamlit abrirá automáticamente una pestaña en tu navegador web con el dashboard en funcionamiento.

📄 Estructura de Datos (Requerida en Coffe_sales.csv)
Para que el script funcione correctamente, tu archivo Coffe_sales.csv debe contener, como mínimo, las siguientes columnas:

money: (Numérico) El valor monetario de cada venta.

Weekday: (Texto) El nombre del día de la semana (ej. "Lunes", "Martes").

Weekdaysort: (Numérico) Un índice para ordenar los días de la semana (ej. 0 para Lunes, 1 para Martes...).

Time_of_Day: (Texto) El período del día (ej. "Mañana", "Tarde", "Noche").

Month_name: (Texto) El nombre del mes (ej. "Enero", "Febrero").

Monthsort: (Numérico) Un índice para ordenar los meses (ej. 1 para Enero, 2 para Febrero...).

hour_of_day: (Numérico o Texto) La hora específica de la venta (será tratada como una categoría).

coffee_name: (Texto) El nombre o tipo del café vendido.