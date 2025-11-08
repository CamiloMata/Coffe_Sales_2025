import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de la página
st.set_page_config(
    page_title="Dashboard de Ventas de Café",
    page_icon="☕",
    layout="wide"
)

# 2. Carga de Datos (con caché para mejor rendimiento)
@st.cache_data
def load_data(filepath):
    """Carga el archivo CSV y lo devuelve como un DataFrame."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        st.error(f"Error: No se encontró el archivo en la ruta: {filepath}")
        return None

# Cargar los datos
df = load_data("Coffe_sales.csv")

if df is not None:

    # 3. Título principal
    st.title("☕ Dashboard de Ventas de Café")

    # --- INICIO DEL RESUMEN SUPERIOR ---
    
    # 4. Procesamiento para el Resumen Superior
    # Agrupar por día de la semana y ordenar usando Weekdaysort
    df_weekday_sales = df.groupby(['Weekday', 'Weekdaysort'])['money'].sum().reset_index()
    df_weekday_sales = df_weekday_sales.sort_values('Weekdaysort')

    st.subheader("Ventas Totales por Día de la Semana")

    # Crear columnas para mostrar las métricas
    # Usamos 7 columnas, una para cada día
    cols = st.columns(7)
    
    for i, row in df_weekday_sales.iterrows():
        with cols[i]:
            # st.metric muestra un valor "KPI"
            st.metric(
                label=row['Weekday'], 
                value=f"${row['money']:,.2f}"
            )

    # --- FIN DEL RESUMEN SUPERIOR ---

    st.divider() # Añade una línea divisoria

    # --- INICIO DE LOS GRÁFICOS PRINCIPALES ---
    
    st.header("Análisis Detallado de Ventas")

    # 5. Procesamiento y Creación de Gráficos
    
    # Preparar datos para los gráficos
    df_time_of_day = df.groupby('Time_of_Day')['money'].sum().reset_index()
    df_month = df.groupby(['Month_name', 'Monthsort'])['money'].sum().reset_index().sort_values('Monthsort')
    df_hour = df.groupby('hour_of_day')['money'].sum().reset_index()
    df_coffee = df.groupby('coffee_name')['money'].sum().reset_index().sort_values('money', ascending=False)

    # Definir el layout de 2x2 para los gráficos
    col1, col2 = st.columns(2)

    with col1:
        # 🥧 Gráfico de Pastel (Pie Chart): Time_of_Day vs money
        st.subheader("Ventas por Momento del Día")
        fig_pie = px.pie(
            df_time_of_day,
            names='Time_of_Day',
            values='money',
            title='Distribución de Ventas por Momento del Día',
            hole=0.3 # Opcional: crea un gráfico de "dona"
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)

        # 📊 Gráfico de Barras Horizontal: hour_of_day vs money
        st.subheader("Ventas por Hora del Día")
        fig_bar_h = px.bar(
            df_hour,
            x='money',
            y='hour_of_day',
            orientation='h', # 'h' para horizontal
            title='Ventas Totales por Hora',
            labels={'money': 'Ventas Totales ($)', 'hour_of_day': 'Hora del Día'}
        )
        # Asegurarse de que el eje Y se trate como categoría
        fig_bar_h.update_layout(yaxis={'type': 'category'}) 
        st.plotly_chart(fig_bar_h, use_container_width=True)

    with col2:
        # 📈 Gráfico de Líneas (Line Chart): Month_name vs money
        st.subheader("Tendencia de Ventas por Mes")
        fig_line = px.line(
            df_month,
            x='Month_name',
            y='money',
            title='Ventas Totales por Mes',
            labels={'money': 'Ventas Totales ($)', 'Month_name': 'Mes'},
            markers=True # Añade marcadores a los puntos de datos
        )
        st.plotly_chart(fig_line, use_container_width=True)

        # 📉 Gráfico de Barras Vertical: coffee_name vs money
        st.subheader("Ventas por Tipo de Café")
        fig_bar_v = px.bar(
            df_coffee,
            x='coffee_name',
            y='money',
            title='Ventas Totales por Tipo de Café',
            labels={'money': 'Ventas Totales ($)', 'coffee_name': 'Tipo de Café'}
        )
        st.plotly_chart(fig_bar_v, use_container_width=True)

else:
    st.warning("No se pudieron cargar los datos. Asegúrate de que 'Coffe_sales.csv' esté en la misma carpeta.")