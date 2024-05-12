# Importing the necessary libraries
import streamlit as st
import pandas as pd
import pickle


# Setting up the page configuration for Streamlit App
st.set_page_config(
    page_title=" :mushroom: Mushroom App",
    page_icon="🍄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Function for user input features
def user_input_features():
    # Creating sliders and select boxes for user input in the sidebar
    cap_diameter = st.sidebar.slider('Cap Diameter',
                            min_value=0.0,
                            max_value=2000.0,
                            value = 1000.0,
                            step=1.0,
    )
    cap_shape = st.sidebar.selectbox('Cap Shape',
                            options=('bell',
                                    'conical',
                                    'convex',
                                    'flat',
                                    'sunken',
                                    'spherical',
                                    'other',)
    )
    gill_attachment = st.sidebar.selectbox('Gill Attachment',
                            options=('adnate',
                                    'adnexed',
                                    'decurrent',
                                    'free',
                                    'sinuate',
                                    'pores',
                                    'none',)
    )
    gill_color = st.sidebar.selectbox('Gill Color',
                            options=('brown',
                                    'buff',
                                    'gray',
                                    'green',
                                    'pink',
                                    'purple',
                                    'red',
                                    'white',
                                    'yellow',
                                    'blue',
                                    'orange',
                                    'black',)
    )
    stem_height = st.sidebar.slider('Stem Height',
                            min_value=0.0,
                            max_value=4.0,
                            value=2.0,
                            step=0.1,
    )
    stem_width = st.sidebar.slider('Stem Width',
                            min_value=0.0,
                            max_value=4000.0,
                            value=2000.0,
                            step=1.0,
    )
    stem_color = st.sidebar.selectbox('Stem Color',
                            options=('brown',
                                    'buff',
                                    'gray',
                                    'green',
                                    'pink',
                                    'purple',
                                    'red',
                                    'white',
                                    'yellow',
                                    'blue',
                                    'orange',
                                    'black',)
    )
    season = st.sidebar.selectbox('Season',
                            options=('spring',
                                    'summer',
                                    'autumn',
                                    'winter',)
    )


    # Function to get the color code
    def get_color(color_name):
        color_dict = {
            'brown': 0,
            'buff': 1,
            'gray': 2,
            'green': 3,
            'pink': 4,
            'purple': 5,
            'red': 6,
            'white': 7,
            'yellow': 8,
            'blue': 9,
            'orange': 10,
            'black': 11,
        }
        return color_dict.get(color_name.lower(), "not found")


    # Function to get the cap shape code
    def get_cap_shape(cap_shape):
        shape_dict = {
            'bell': 0,
            'conical': 1,
            'convex': 2,
            'flat': 3,
            'sunken': 4,
            'spherical': 5,
            'other': 6,
        }
        return shape_dict.get(cap_shape.lower(), "not found")


    # Function to get gill attachment code
    def get_gill_attachment(gill_attachment):
        gill_attachment_dict = {
            'adnate': 0,
            'adnexed': 1,
            'decurrent': 2,
            'free': 3,
            'sinuate': 4,
            'pores': 5,
            'none': 6,
        }
        return gill_attachment_dict.get(gill_attachment.lower(), "not found")


    # Function to get season code
    def get_season(season):
        season_dict = {
            'spring': 0,
            'summer': 1,
            'autumn': 2,
            'winter': 3,
        }
        return season_dict.get(season.lower(), "not found")

    # Creating a data dictionary to store the user input data
    data = {'cap-diameter': cap_diameter,
            'cap-shape': get_cap_shape(cap_shape),
            'gill-attachment': get_gill_attachment(gill_attachment),
            'gill-color': get_color(gill_color),
            'stem-height': stem_height,
            'stem-width': stem_width,
            'stem-color': get_color(stem_color),
            'season': get_season(season),
    }

    # Creating a DataFrame from the data dictionary
    features = pd.DataFrame(data, index=[0])
    return features


# Function to load the prediction model
#@st.cache_data()
def get_model():
    model = pickle.load(open("models/rfc_model.pkl", "rb"))
    return model


# Function to make prediction using the model and input data
def make_prediction(data):
    model = get_model()
    return model.predict(data)


# Main function
def main():
    st.write("""# :mushroom: Mushroom App""")
    st.sidebar.image("img/dataset-cover.jpg")
    user_data = user_input_features()

    # Creating a session state button for prediction
    if 'btn_predict' not in st.session_state:
        st.session_state['btn_predict'] = False

    st.session_state['btn_predict'] = st.button("Predict")

    # Making prediction and showing result
    if st.session_state['btn_predict'] == True:
        if make_prediction(user_data) == 1:
            st.error("# Result: Poisonous :skull_and_crossbones: ")
        else:
            st.success("# Result: Edible :mushroom: ")


# Running the main function
if __name__ == "__main__":
    main()
