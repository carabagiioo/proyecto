# Análisis de Vehículos Usados (Proyecto Sprint 7)

## Descripción del Proyecto
Este proyecto es una aplicación web interactiva desarrollada en Python utilizando **Streamlit** y **Plotly**. Su objetivo principal es realizar y mostrar un Análisis Exploratorio de Datos (EDA) sobre un conjunto de datos de vehículos usados en venta en los Estados Unidos (`vehicles_us.csv`).

## ¿Para qué sirve la aplicación?
La aplicación sirve como un panel de control (dashboard) dinámico que permite a cualquier usuario visualizar rápidamente el estado del mercado de vehículos de segunda mano. Proporciona herramientas visuales intuitivas para entender cómo se distribuyen variables clave como el precio, el kilometraje, el año de los modelos, y el estado de los vehículos.

## Funcionalidades
La aplicación proporciona varios controles interactivos (botones y casillas de verificación) que generan gráficos de Plotly bajo demanda, optimizando así el rendimiento. Entre sus funcionalidades se incluyen:

- **Histograma de Odómetro**: Permite visualizar la distribución del kilometraje de los vehículos publicados.
- **Distribución por Año**: Muestra cuántos coches hay por cada año de fabricación.
- **Distribución de Precios**: Analiza los rangos de precios más comunes de los vehículos.
- **Transmisión y Tracción 4WD**: Gráficos para entender la proporción de vehículos manuales/automáticos y los que cuentan con tracción 4x4.
- **Condición del Vehículo**: Un análisis de las condiciones (excelente, buena, regular, etc.) en las que se venden los autos.
- **Relación Condición vs. Año**: Un diagrama de cajas (boxplot) que relaciona de forma interactiva el año de fabricación con la condición actual del vehículo.

## Tecnologías Utilizadas
- **Python**: Lenguaje principal de desarrollo.
- **Pandas**: Para la manipulación y lectura de los datos en formato CSV.
- **Plotly (Express y Graph Objects)**: Para la creación de gráficos dinámicos e interactivos.
- **Streamlit**: Para el despliegue rápido de la interfaz web.
