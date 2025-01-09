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
Three tabs are created to organize the interface:
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

---

## **Contact Info**
- **GitHub**: [https://github.com/alruvamora](https://github.com/alruvamora)
- **LinkedIn**: [Álvaro Ruedas Mora](https://www.linkedin.com/in/%C3%A1lvaro-ruedas-29379a180/)
- **Email**: alruvamora@gmail.com

---

## **About Me**
**Álvaro Ruedas Mora**
- Data Scientist from **Ironhack**
- Industrial and Automation Electronics Engineer from **Polytechnic University of Madrid**
- MBA from **EAE Business School**
