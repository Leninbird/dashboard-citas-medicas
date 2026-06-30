import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de la página
st.set_page_config(page_title="Gestión de Citas Médicas", layout="wide")

# 2. Título principal del Dashboard
st.title('Dashboard de Gestión de Citas Médicas')
st.markdown("Análisis inteligente del comportamiento de citas, especialidades y demanda futura.")

# 3. Cargar el dataset generado en la Actividad 1
# Nota: El archivo 'citas_medicas.csv' debe estar en la misma carpeta que este script
df = pd.read_csv('citas_medicas.csv')

# Asegurar el formato de fecha para los gráficos temporales
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.month

# 4. DISPOSICIÓN EN COLUMNAS (Para una mejor organización visual)
col1, col2 = st.columns(2)

with col1:
    st.subheader('📊 Citas por Especialidad')
    # Conteo de frecuencia de especialidades
    citas_especialidad = df['especialidad'].value_counts().reset_index()
    citas_especialidad.columns = ['Especialidad', 'Cantidad']
    
    # Gráfico de barras interactivo con Plotly
    fig1 = px.bar(
        citas_especialidad, 
        x='Especialidad', 
        y='Cantidad',
        color='Especialidad',
        text_auto=True
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader('🍕 Estado de las Citas')
    # Gráfico de pastel interactivo
    fig2 = px.pie(
        df, 
        names='estado', 
        color='estado',
        color_discrete_map={'Atendida':'#2ca02c', 'Cancelada':'#d62728', 'No asistió':'#ff7f0e'}
    )
    st.plotly_chart(fig2, use_container_width=True)

# 5. Gráfico de línea en la parte inferior (Análisis mensual)
st.subheader('📈 Evolución Temporal de Citas por Mes')
citas_mes = df.groupby('mes').size().reset_index(name='cantidad')

fig3 = px.line(
    citas_mes,
    x='mes',
    y='cantidad',
    markers=True,
    labels={'mes': 'Número de Mes', 'cantidad': 'Total de Citas'}
)
# Ajustar el eje X para que muestre los meses correctamente del 1 al 12
fig3.update_layout(xaxis=dict(tickmode='linear', tick0=1, dtick=1))
st.plotly_chart(fig3, use_container_width=True)
