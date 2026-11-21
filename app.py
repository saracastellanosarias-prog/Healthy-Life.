import pandas as pd
import streamlit as st 
import plotly.express as px
import numpy as np

st.set_page_config(
    page_title="Healthy Life",
    page_icon="💜",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #FAF8FC !important;
    color: #30263B !important;
}

h1, h2, h3, p {
    color: #76529B !important;
}

section[data-testid="stSidebar"] {
    background-color: #F0E8F8 !important;
}
</style>
""", unsafe_allow_html=True)
datos = pd.read_csv(
    "Sleep_health_and_lifestyle_dataset.csv"
)

import streamlit as st
import pandas as pd
import os

@st.cache_data
def cargar_datos():
    datos = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
    return datos

datos = cargar_datos()

st.title("Healthy Life")


st.write("Cantidad de filas y columnas:", datos.shape)

st.subheader("Primeros registros del dataset")
st.dataframe(datos.head(10))


import streamlit as st
import pandas as pd

# Función para cargar los datos
@st.cache_data
def cargar_datos():
    datos = pd.read_csv(
        "Sleep_health_and_lifestyle_dataset.csv"
    )
    return datos

# Cargar los datos
datos = cargar_datos()

st.write("Cantidad de registros:", len(datos))
st.write("Cantidad de variables:", len(datos.columns))

st.subheader("Nombres de las columnas")
st.write(datos.columns.tolist())

st.subheader("Información del dataset")
st.dataframe(datos)

opcion = st.sidebar.radio(
    "Menú principal",
    ["Inicio", "Explorar datos", "Conclusiones"]
)
if opcion == "Inicio":

    st.title("Bienvenido a Healthy Life")
    st.write("Conoce tus hábitos y descubre patrones relacionados con el bienestar.")

elif opcion == "Explorar datos":

    st.title("Exploración de datos")

    st.metric("Total de registros", len(datos))
    st.metric("Total de variables", len(datos.columns))

    st.subheader("Filtrar información")

    edades = sorted(datos["Age"].dropna().unique())

    edad = st.selectbox(
        "Selecciona una edad:",
        ["Todas"] + edades
    )

    if edad == "Todas":
        datos_filtrados = datos
    else:
        datos_filtrados = datos[datos["Age"] == edad]

    st.subheader("Resultados")
    st.dataframe(datos_filtrados)
    st.subheader("Calidad del sueño")

    calidad_sueno = (
        datos_filtrados["Quality of Sleep"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    calidad_sueno.columns = ["Calidad del sueño", "Cantidad de personas"]

    fig = px.bar(
        calidad_sueno,
        x="Calidad del sueño",
        y="Cantidad de personas",
        title="Distribución de la calidad del sueño",
        color_discrete_sequence=["#A78BCA"],
        text="Cantidad de personas"
    )

    fig.update_layout(
        plot_bgcolor="#FAF8FC",
        paper_bgcolor="#FAF8FC",
        font=dict(
            color="#49365E",
            size=13
        ),
        title_x=0.5,
        xaxis_title="Nivel de calidad del sueño",
        yaxis_title="Número de personas",
        xaxis=dict(
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        ),
        yaxis=dict(
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        )
    )

    fig.update_traces(
        textfont=dict(color="#49365E"),
        textposition="outside",
        marker_line_width=0
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Duración del sueño")

    fig2 = px.histogram(
        datos_filtrados,
        x="Sleep Duration",
        nbins=10,
        title="Distribución de las horas de sueño",
        color_discrete_sequence=["#B99AD9"],
        labels={
            "Sleep Duration": "Horas de sueño",
            "count": "Cantidad de personas"
        }
    )

    fig2.update_layout(
        plot_bgcolor="#FAF8FC",
        paper_bgcolor="#FAF8FC",
        font=dict(
            color="#49365E",
            size=13
        ),
        title_x=0.5,
        xaxis_title="Horas de sueño",
        yaxis_title="Cantidad de personas",
        xaxis=dict(
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        ),
        yaxis=dict(
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        )
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Actividad física")

    fig3 = px.histogram(
        datos_filtrados,
        x="Daily Steps",
        nbins=10,
        title="Distribución de los pasos diarios",
        color_discrete_sequence=["#A78BCA"],
        labels={
            "Daily Steps": "Pasos diarios",
            "count": "Cantidad de personas"
        }
    )

    fig3.update_layout(
        plot_bgcolor="#FAF8FC",
        paper_bgcolor="#FAF8FC",
        font=dict(color="#49365E", size=13),
        title_x=0.5,
        xaxis=dict(
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        ),
        yaxis=dict(
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        )
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Actividad física y calidad del sueño")

    fig4 = px.scatter(
        datos_filtrados,
        x="Daily Steps",
        y="Quality of Sleep",
        title="Relación entre pasos diarios y calidad del sueño",
        color_discrete_sequence=["#9370B8"],
        labels={
            "Daily Steps": "Pasos diarios",
            "Quality of Sleep": "Calidad del sueño"
        }
    )

    fig4.update_layout(
        plot_bgcolor="#FAF8FC",
        paper_bgcolor="#FAF8FC",
        font=dict(color="#49365E", size=13),
        title_x=0.5,
        xaxis=dict(
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        ),
        yaxis=dict(
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        )
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.subheader("Estrés y bienestar")

    estres = (
        datos_filtrados["Stress Level"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    estres.columns = ["Nivel de estrés", "Cantidad de personas"]

    fig5 = px.bar(
        estres,
        x="Nivel de estrés",
        y="Cantidad de personas",
        title="Distribución de los niveles de estrés",
        color_discrete_sequence=["#B99AD9"],
        text="Cantidad de personas"
    )

    fig5.update_layout(
        plot_bgcolor="#FAF8FC",
        paper_bgcolor="#FAF8FC",
        font=dict(color="#49365E", size=13),
        title_x=0.5,

        xaxis=dict(
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        ),

        yaxis=dict(
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        )
    )

    fig5.update_traces(
        textposition="outside",
        textfont=dict(color="#49365E")
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("Relación entre estrés y duración del sueño")

    fig6 = px.scatter(
        datos_filtrados,
        x="Stress Level",
        y="Sleep Duration",
        title="Relación entre el estrés y las horas de sueño",
        color="Stress Level",
        color_continuous_scale="Purples",
        labels={
            "Stress Level": "Nivel de estrés",
            "Sleep Duration": "Horas de sueño"
        },
        opacity=0.7
    )

    fig6.update_layout(
        plot_bgcolor="#FAF8FC",
        paper_bgcolor="#FAF8FC",
        font=dict(color="#49365E", size=13),
        title_x=0.5,

        xaxis=dict(
            title="Nivel de estrés",
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        ),

        yaxis=dict(
            title="Horas de sueño",
            color="#49365E",
            linecolor="#76529B",
            tickfont=dict(color="#49365E"),
            title_font=dict(color="#76529B")
        ),

        coloraxis_colorbar=dict(
            title="Estrés",
            tickfont=dict(color="#49365E")
        )
    )

    st.plotly_chart(fig6, use_container_width=True)

      
    # ANÁLISIS ESTADÍSTICO DE HEALTHY LIFE
    
    
    st.markdown("---")
    
    st.header("Análisis estadístico de Healthy Life")
    
    st.write(
        "En esta sección podrás consultar las "
        "estadísticas del sueño y la actividad física."
    )
    
    # Crear las pestañas ANTES de utilizarlas
    tab1, tab2, tab3 = st.tabs([
        "Sueño y descanso",
        "Actividad física",
        "Estrés y bienestar"
    ])
    
    
   
    # PRIMERA PESTAÑA: SUEÑO
    
    
    with tab1:
    
        st.subheader("Estadísticas del sueño")
    
        st.write(
            "Resultados estadísticos de las horas "
            "de sueño registradas en el dataset."
        )
    
        horas_sueno = datos["Sleep Duration"].dropna()
    
        if not horas_sueno.empty:
    
            tabla_sueno = pd.DataFrame({
                "Estadística": [
                    "Promedio",
                    "Mediana",
                    "Máximo",
                    "Mínimo",
                    "Desviación estándar"
                ],
                "Resultado": [
                    f"{np.mean(horas_sueno):.2f} horas",
                    f"{np.median(horas_sueno):.2f} horas",
                    f"{np.max(horas_sueno):.2f} horas",
                    f"{np.min(horas_sueno):.2f} horas",
                    f"{np.std(horas_sueno):.2f} horas"
                ]
            })
    
            st.table(tabla_sueno.set_index("Estadística"))

            st.markdown("### Interpretación de los resultados")

            promedio_sueno = np.mean(horas_sueno)
            desviacion_sueno = np.std(horas_sueno)

            st.write(
                f"Las personas del conjunto de datos duermen "
                f"en promedio {promedio_sueno:.2f} horas diarias. "
                f"La desviación estándar es de "
                f"{desviacion_sueno:.2f} horas, lo que permite "
                f"conocer cuánto varía la duración del sueño "
                f"entre los registros."
            )

            st.info(
                "Estas estadísticas permiten conocer "
                "el comportamiento de las horas de sueño."
            )

        else:
            st.warning("No hay datos disponibles de sueño.")
    
    
    
    # SEGUNDA PESTAÑA: ACTIVIDAD FÍSICA
    
    
    with tab2:
    
        st.subheader(" Estadísticas de actividad física")
    
        st.write(
            "Resultados estadísticos de la cantidad "
            "de pasos diarios registrados."
        )
    
        pasos = datos["Daily Steps"].dropna()
    
        if not pasos.empty:
    
            tabla_actividad = pd.DataFrame({
                "Estadística": [
                    "Promedio",
                    "Mediana",
                    "Máximo",
                    "Mínimo",
                    "Desviación estándar"
                ],
                "Resultado": [
                    f"{np.mean(pasos):,.0f} pasos",
                    f"{np.median(pasos):,.0f} pasos",
                    f"{np.max(pasos):,.0f} pasos",
                    f"{np.min(pasos):,.0f} pasos",
                    f"{np.std(pasos):,.2f} pasos"
                ]
            })
    
            st.table(tabla_actividad.set_index("Estadística"))

            st.markdown("### Interpretación de los resultados")

            promedio_pasos = np.mean(pasos)
            desviacion_pasos = np.std(pasos)

            st.write(
                f"Las personas registran un promedio de "
                f"{promedio_pasos:,.0f} pasos diarios. "
                f"La desviación estándar es de "
                f"{desviacion_pasos:,.2f} pasos, "
                f"lo que permite analizar las diferencias "
                f"en actividad física entre los registros."
            )

            st.info(
                "Estas estadísticas permiten conocer "
                "el comportamiento de la actividad física."
            )

        else:
            st.warning("No hay datos disponibles de actividad física.")


    # TERCERA PESTAÑA: ESTRÉS

    with tab3:

        st.subheader("Análisis estadístico del estrés")

        st.write(
            "En esta sección se analizan los niveles "
            "de estrés registrados en el dataset."
        )

        estres = datos["Stress Level"].dropna()

        if not estres.empty:

            tabla_estres = pd.DataFrame({
                "Estadística": [
                    "Promedio",
                    "Mediana",
                    "Máximo",
                    "Mínimo",
                    "Desviación estándar"
                ],
                "Resultado": [
                    f"{np.mean(estres):.2f}",
                    f"{np.median(estres):.2f}",
                    f"{np.max(estres):.2f}",
                    f"{np.min(estres):.2f}",
                    f"{np.std(estres):.2f}"
                ]
            })

            st.table(
                tabla_estres.set_index("Estadística")
            )


            st.markdown("### Interpretación de los resultados")

            promedio_estres = np.mean(estres)
            desviacion_estres = np.std(estres)

            st.write(
                f"El nivel promedio de estrés registrado "
                f"es de {promedio_estres:.2f} puntos. "
                f"La desviación estándar es de "
                f"{desviacion_estres:.2f} puntos, "
                f"lo que permite observar cuánto varían "
                f"los niveles de estrés entre las personas."
            )

            st.info(
                "Estas estadísticas permiten conocer "
                "cómo se distribuyen los niveles de estrés."
            )

        else:
            st.warning(
                "No hay datos disponibles sobre estrés."
            )
    
    

# CONCLUSIONES 


elif opcion == "Conclusiones":

    st.title("💜 Conclusiones de Healthy Life")

    st.write(
        "A partir del análisis de los datos, "
        "podemos explorar patrones relacionados "
        "con el sueño, la actividad física y el estrés."
    )

    st.markdown("---")

    # PREGUNTA GUÍA
    st.subheader("Nuestra pregunta guía")

    st.info(
        "¿Cómo podemos ayudar a las personas "
        "a identificar si están teniendo hábitos "
        "saludables en su vida diaria?"
    )

    # CONCLUSIONES POR DIMENSIÓN
    tab_sueno, tab_actividad, tab_estres = st.tabs([
        "Sueño",
        "Actividad física",
        "Estrés"
    ])

    with tab_sueno:

        st.subheader("Conclusiones sobre el sueño")

        horas = datos["Sleep Duration"].dropna()

        if not horas.empty:

            promedio = np.mean(horas)
            mediana = np.median(horas)

            st.write(
                f"El promedio de duración del sueño "
                f"es de {promedio:.2f} horas, mientras "
                f"que la mediana es de {mediana:.2f} horas."
            )

            st.write(
                "Estos resultados permiten describir "
                "los patrones de descanso registrados "
                "en el conjunto de datos."
            )

    with tab_actividad:

        st.subheader("Conclusiones sobre actividad física")

        pasos = datos["Daily Steps"].dropna()

        if not pasos.empty:

            promedio_pasos = np.mean(pasos)

            st.write(
                f"El promedio de pasos diarios "
                f"registrados es de "
                f"{promedio_pasos:,.0f} pasos."
            )

            st.write(
                "Este indicador permite observar "
                "los niveles de movimiento registrados "
                "y comparar diferencias entre personas."
            )

    with tab_estres:

        st.subheader("Conclusiones sobre el estrés")

        estres = datos["Stress Level"].dropna()

        if not estres.empty:

            promedio_estres = np.mean(estres)

            st.write(
                f"El nivel promedio de estrés "
                f"registrado es de "
                f"{promedio_estres:.2f} puntos."
            )

            st.write(
                "El análisis permite explorar "
                "cómo varían los niveles de estrés "
                "y su posible relación con el descanso."
            )

    # REFLEXIÓN FINAL
    st.markdown("---")

    st.subheader(" Reflexión final")

    st.success(
        "Healthy Life demuestra cómo el análisis "
        "y la visualización de datos pueden facilitar "
        "la comprensión de hábitos relacionados "
        "con el bienestar."
    )

    st.write(
        "Al presentar información mediante gráficas, "
        "tablas e interpretaciones, ayudamos a las "
        "personas a reconocer patrones y reflexionar "
        "sobre sus hábitos diarios."
    )

    st.caption(
        "Los resultados son descriptivos y no "
        "permiten diagnosticar condiciones médicas "
        "ni establecer relaciones de causa y efecto."
    )

  


