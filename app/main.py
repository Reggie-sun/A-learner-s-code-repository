import pandas as pd
import streamlit as st
import pickle


st.set_page_config(
    page_title="Breast Cancer Predictor",
    page_icon=":shark:",
    layout="wide",
    initial_sidebar_state="expanded"
)


def get_clean_data():
    data = pd.read_csv(
        r"D:\vscode folder\Diagnosis of breast cancer\data\data.csv")
    data = data.drop(columns=['Unnamed: 32', 'id'])
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

    return data


def add_sidebar():
    st.sidebar.header("Cell Nuclei Measurements")

    data = get_clean_data()

    slider_labels = [
        ("Radius (mean)", "radius_mean"),
        ("Texture (mean)", "texture_mean"),
        ("Perimeter(mean)", "perimeter_mean"),
        ("Area(mean)", "area_mean"),
        ("Smoothness (mean)", "smoothness_mean"),
        ("Compactness(mean)", "compactness_mean"),
        ("Concavity (mean)", "concavity_mean"),
        ("Concave points (mean)", "concave points_mean"),
        ("Symmetry(mean)", "symmetry_mean"),
        ("Fractaldimension(mean)", "fractal_dimension_mean"),
        ("Radius (se)", "radius_se"),
        ("Texture (se)", "texture_se"),
        ("Perimeter (se)", "perimeter_se"),
        ("Area (se)", "area_se"),
        ("Smoothness (se)", "smoothness_se"),
        ("Compactness (se)", "compactness_se"),
        ("Concavity (se)", "concavity_se"),
        ("Concave points (se)", "concave points_se"),
        ("Symmetry (se)", "symmetry_se"),
        ("Fractal dimension (se)", "fractal_dimension_se"),
        ("Radius (worst)", "radius_worst"),
        ("Texture (worst)", "texture_worst"),
        ("Perimeter (worst)", "perimeter_worst"),
        ("Area (worst)", "area_worst"),
        ("Smoothness(worst)", "smoothness_worst"),
        ("Compactness(worst)", "compactness_worst"),
        ("Concavity (worst)", "concavity_worst"),
        ("Concave points (worst)", "concave points_worst"),
        ("Symmetry (worst)", "symmetry_worst"),
        ("Fractal dimension (worst)", "fractal_dimension_worst")
    ]

    input_dict = {}

    for laber, key in slider_labels:
        input_dict[key] = st.sidebar.slider(laber,
                                            min_value=float(0),
                                            max_value=float(data[key].max()),
                                            value=float(data[key].mean()),
                                            )
    return input_dict


def main():
    with st.container():
        st.title("Breast Cancer Predictor")
        st.write("""Please connect this app to your cytology lab to help diagnose breast cancer form your tissue sample: This app predicts using a machine learning model whether a breast mass is
             benign or malignant based on the measurements it receives from your cytosis lab.You can also update the measurements by hand using the slidersin the sidebar.""")

    input_data = add_sidebar()

    col1, col2 = st.columns([4, 1])

    with col1:
        st.write("this is column 1")
    with col2:
        st.write('this is column 2')

    input_data = add_sidebar()


if __name__ == '__main__':

    main()
