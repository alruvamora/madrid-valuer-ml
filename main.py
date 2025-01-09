import streamlit as st
import numpy as np
import pandas as pd
import pickle

# CSS para personalizar los títulos
st.markdown("""
    <style>
    .main-title {
        text-align: center; /* Center the text */
        font-size: 50px; /* Large font size for the first title */
        font-weight: bold; /* Bold font */
        color: white; /* Text color */
        margin-bottom: 20px; /* Bottom spacing */
    }
    .sub-title {
        text-align: center; /* Center the text */
        font-size: 20px; /* Small font size for the second title */
        font-weight: normal; /* Normal font weight */
        color: gray; /* Gray color */
        margin-top: -10px; /* Top spacing */
    }
    </style>
""", unsafe_allow_html=True)

# Títulos con estilos personalizados
st.markdown('<div class="main-title">Madrid Valuer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Machine Learning Prediction Model for Floor Price in Madrid</div>', unsafe_allow_html=True)

# Load the image
st.image("Madrid.png", use_column_width=True)

# Load the model from the file
with open('madrid_valuer_model.pkl', 'rb') as f:
    etr = pickle.load(f)

columnas = [
    "CONSTRUCTEDAREA",
    "ROOMNUMBER",
    "BATHNUMBER",
    "HASTERRACE",
    "HASLIFT",
    "HASAIRCONDITIONING",
    "HASPARKINGSPACE",
    "ISPARKINGSPACEINCLUDEDINPRICE",
    "HASNORTHORIENTATION",
    "HASSOUTHORIENTATION",
    "HASEASTORIENTATION",
    "HASWESTORIENTATION",
    "HASBOXROOM",
    "HASWARDROBE",
    "HASSWIMMINGPOOL",
    "HASDOORMAN",
    "HASGARDEN",
    "ISDUPLEX",
    "ISSTUDIO",
    "ISINTOPFLOOR",
    "CONSTRUCTIONYEAR",
    "DISTANCE_TO_CITY_CENTER",
    "DISTANCE_TO_METRO",
    "DISTANCE_TO_CASTELLANA"
]

# st.title("Data Input")



def new_analysis():
    # Crear un formulario para ingresar los datos
    with st.form("data_form"):
        
        # Numeric data inputs
        constructed_area = st.number_input("Constructed Area (in m²)", min_value=0, step=1)
        room_number = st.number_input("Number of Rooms", min_value=0, step=1)
        bath_number = st.number_input("Number of Bathrooms", min_value=0, step=1)
        construction_year = st.number_input("Year of Construction", min_value=0, step=1)
        distance_to_metro = st.number_input("Distance to the Nearest Metro (in meters)", min_value=0.0, step=0.01)
        distance_to_city_center = st.number_input("Distance to City Center (in km)", min_value=0.0, step=0.01)
        distance_to_castellana = st.number_input("Distance to Castellana (in km)", min_value=0.0, step=0.01)
    
        # Boolean data inputs (True/False)
    
        # Checkbox
        has_terrace = st.checkbox("Terrace", value=False)
        has_lift = st.checkbox("Elevator", value=False)
        has_air_conditioning = st.checkbox("Air Conditioning", value=False)
        has_parking_space = st.checkbox("Parking", value=False)
        is_parking_space_included_in_price = st.checkbox("Parking Space Included", value=False)
        has_box_room = st.checkbox("Storage Room", value=False)
        has_wardrobe = st.checkbox("Built-in Wardrobes", value=False)
        has_swimming_pool = st.checkbox("Swimming Pool", value=False)
        has_doorman = st.checkbox("Doorman", value=False)
        has_garden = st.checkbox("Garden", value=False)
    
        #Toggle
        is_duplex = st.toggle("Duplex", value=False)
        is_studio = st.toggle("Studio", value=False)
        is_in_top_floor = st.toggle("Top Floor", value=False)
    
        # Use st.multiselect to select multiple orientations
        orientations = st.multiselect(
        "Orientation:",
        options=["North", "South", "East", "West"],  # Options to select
        default=[]  # By default, none are selected
        )
        
        # Convert the selected orientations into boolean values
        has_north_orientation = "North" in orientations
        has_south_orientation = "South" in orientations
        has_east_orientation = "East" in orientations
        has_west_orientation = "West" in orientations
    
        
        st.markdown("""
        <style>
        .css-1q8dd3e {  
        border-radius: 10px !important; /* Bordes redondeados */
        display: flex; 
        justify-content: center;
        align-items: center;
        }
        .stButton { 
            text-align: center; /* Centrar el botón */
        }
        </style>
        """, unsafe_allow_html=True)
    
        # Botón estilizado y funcional
        submit_button = st.form_submit_button("Get Price")
    
    # Guardar los datos ingresados en variables al enviar el formulario
    if submit_button:
        vector = [
            constructed_area, room_number, bath_number, has_terrace, has_lift, has_air_conditioning,
            has_parking_space, is_parking_space_included_in_price, has_north_orientation, 
            has_south_orientation,
            has_east_orientation, has_west_orientation, has_box_room, has_wardrobe, has_swimming_pool,
            has_doorman, has_garden, is_duplex, is_studio, is_in_top_floor, construction_year,
            distance_to_city_center, distance_to_metro/1000, distance_to_castellana
        ]
        
        # Crear un DataFrame para la muestra
        sample = pd.DataFrame(columns=columnas)
        sample.loc[0] = vector  # Agregar la fila de entrada
        
        # Convertir a un array bidimensional
        sample_array = sample.values.reshape(1, -1)
        
        # Predecir usando el modelo `etr`
        s_pred_etr = etr.predict(sample_array)
    
        st.markdown("<h3 style='font-size: 25px;'>Estimated Price: </h3>", unsafe_allow_html=True)
        st.markdown(
        """
        <h1 style='text-align: center;'>{:,} €</h1>
        """.format(int(s_pred_etr)).replace(',', '.'), unsafe_allow_html=True
        )
        st.markdown("<h3 style='font-size: 25px;'>Estimated Range: </h3>", unsafe_allow_html=True)
        st.markdown(
        """
        <h1 style='text-align: center;'>{:,} € - {:,} €</h1>
        """.format(int(s_pred_etr * (1 - 0.07)), int(s_pred_etr * (1 + 0.07))).replace(',', '.'),
        unsafe_allow_html=True
        )

def about():
    
    # Markdown content explaining the application
    markdown_content = """
    # Code Explanation
    
    This code implements a web application using **Streamlit** to predict floor prices in Madrid using a pre-trained Machine Learning model saved in a `.pkl` file. The model is pre-trained with a GitHub® data repository from idealista® (https://github.com/paezha/idealista18) that contains information on 94,815 apartments for sale in the city of Madrid. Here's a step-by-step explanation of its functionality:
    
    ---
    
    ## 1. **Imports and Setup**
    - **Imported Libraries**:
      - `streamlit` to create the web interface.
      - `numpy` and `pandas` to handle data.
      - `pickle` to load the pre-trained Machine Learning model.
    - **Custom CSS**:
      - CSS is defined using `st.markdown()` to customize the titles' style, changing their size, color, and alignment.
    
    ---
    
    ## 2. **Main Interface**
    - **Customized Titles**:
      - The main title **"Madrid Valuer"** appears centered, in white, and with a large font size.
      - The subtitle **"Machine Learning Prediction Model for Floor Price in Madrid"** appears centered, in gray, and with a smaller font size.
    - **Image Display**:
      - A background image of Madrid (`Madrid.png`) is displayed as part of the interface.
    - **Load the Model**:
      - A pre-trained Machine Learning model is loaded from `madrid_valuer_model.pkl` using `pickle`.
    
    ---
    
    ## 3. **Data Input: Interactive Form**
    In the **"Data Input"** tab, a form is displayed where the user can input property data. It includes:
    
    ### a) **Numeric Data**
    - Constructed area (in m²).
    - Number of rooms.
    - Number of bathrooms.
    - Year of construction.
    - Distances to key locations such as:
      - Nearest metro station (in meters).
      - City center (in kilometers).
      - Castellana (in kilometers).
    
    ### b) **Floor Features (Boolean)**
    Using checkboxes (`st.checkbox`) or toggle buttons (`st.toggle`), the user can specify:
    - Terrace, elevator, air conditioning.
    - Parking (and whether it's included in the price).
    - Orientations: North, South, East, and West.
    - Swimming pool, doorman, garden.
    - Whether the property is a duplex, studio, or on the top floor.
    
    ### c) **Submit Button**
    - After entering all the data, the user can click the **"Get Price"** button to submit the form.
    
    ---
    
    ## 4. **Data Processing and Prediction**
    When the form is submitted:
    - **Input Vector**:
      - The entered data is collected into a vector and structured as a `DataFrame` with the columns required by the model.
    - **Prediction**:
      - The data is transformed into a 2D array, and the loaded model (`etr`) predicts the floor price.
    - **Result Display**:
      - The estimated price (`s_pred_etr`) is displayed prominently, centered, and with a confidence range (±7% of the price).
    
    ---
    
    ## 5. **Tab Navigation**
    Two tabs are created to organize the interface:
    1. **"Data Input"**:
       - Contains the form for entering property details and getting the estimated price.
    2. **"About"**:
       - Contains information about the application.
    3. **"Contact"**:
       - Contains contact information and a brief creator's resume.
    
    ---
    
    ## **Summary of Functionality**
    This application:
    1. Provides a user-friendly interface with custom styling.
    2. Allows the user to input detailed information about a property.
    3. Uses a pre-trained Machine Learning model to predict the floor price.
    4. Displays the estimated price and a confidence range.
    5. Divides functionality into tabs for better organization.
    
    ---
    
    ## **Requirements**
    - A `madrid_valuer_model.pkl` file containing a pre-trained Machine Learning model.
    - A `Madrid.png` file for the background image.
    - Required Python packages installed:
      - `streamlit`, `numpy`, `pandas`, `pickle`.

      
    """
    
    # Display the markdown content in the Streamlit app
    st.markdown(markdown_content)

def contact():
    
    # Markdown content explaining the application
    markdown_content_info = """

    ## Contact info:
    - GitHub: https://github.com/alruvamora
    - Linkedin: https://www.linkedin.com/in/%C3%A1lvaro-ruedas-29379a180/
    - Mail: alruvamora@gmail.com


    ## About me: 
    Álvaro Ruedas Mora
    
    - Data Scientist from **Ironhack**
    - Industrial and Automation Electronics Engineer from **Polytechnic University of Madrid**
    - MBA from **EAE Business School**
      
    """
    
    # Display the markdown content in the Streamlit app
    st.markdown(markdown_content_info)


# tabs
tabs = st.tabs(["Data Input", "About", "Contact"])

with tabs[0]:
    new_analysis()
with tabs[1]:
    about()
with tabs[2]:
    contact()

