import streamlit as st
from tensorflow.keras.applications import ResNet50, InceptionV3, Xception, VGG16, VGG19
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import pandas as pd
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title="Image Classification App",
    page_icon="CMPT756",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Image Classification")
st.sidebar.subheader("Input")
models_list = ["VGG16", "VGG19", "Inception", "Xception", "ResNet"]
network = st.sidebar.selectbox("Select the Model", models_list)

# a dict for models and class name mapping
MODELS = {
    "VGG16": VGG16,
    "VGG19": VGG19,
    "Inception": InceptionV3,
    "Xception": Xception,  
    "ResNet": ResNet50,
}

# Component to upload images
uploaded_file = st.sidebar.file_uploader(
    "Choose an image to classify", type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    bytes_data = uploaded_file.read()

    # initialize the input image shape (224x224 pixels) and pre-processing function
    inputShape = (224, 224)
    preprocess = imagenet_utils.preprocess_input

    # change input shape and pre-processing function if InceptionV3 or Xception
    if network in ("Inception", "Xception"):
        inputShape = (299, 299)
        preprocess = preprocess_input

    Network = MODELS[network]
    model = Network(weights="imagenet")

    # load input image using PIL image utilities and resize
    image = Image.open(BytesIO(bytes_data))
    image = image.convert("RGB")
    image = image.resize(inputShape)
    image = img_to_array(image)

    # expand the dimension for passing it through the network
    image = np.expand_dims(image, axis=0)

    # pre-process the image
    image = preprocess(image)

    preds = model.predict(image)
    predictions = imagenet_utils.decode_predictions(preds)
    _, label, prob = predictions[0][0]

    st.image(bytes_data, caption=[f"{label} {prob*100:.2f}"])
    st.subheader(f"Top Predictions from {network}")

    # create a dataframe without the "Network" column
    df_predictions = pd.DataFrame(predictions[0], columns=["Network", "Classification", "Confidence"])
    df_predictions.drop(columns=["Network"], inplace=True)  # Remove the "Network" column

    # display the dataframe
    st.dataframe(df_predictions)  
