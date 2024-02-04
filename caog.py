import streamlit as st
import numpy as np
import keras
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras.models import load_model
import cv2
import time
import warnings
warnings.filterwarnings("ignore")

model = load_model('model.h5')

def show_page():
    st.write("<h1 style='text-align: center; color: blue;'>مدل تشخیص سگ و گربه</h1>", unsafe_allow_html=True)
    st.write("<h2 style='text-align: center; color: gray;'>Convolutional Neural Network Model</h2>", unsafe_allow_html=True)
    st.write("<h4 style='text-align: center; color: gray;'>Robo-Ai.ir طراحی شده توسط</h4>", unsafe_allow_html=True)
    st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")

    image = st.file_uploader('آپلود تصویر', type=['jpg', 'jpeg'])        
    if image is not None:
        file_bytes = np.array(bytearray(image.read()), dtype= np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        st.image(img, channels= 'BGR', use_column_width= True)
        x = cv2.resize(img, (128, 128))
        x1 = img_to_array(x)
        x1 = x1.reshape((1,) + x1.shape)
        y_pred = model.predict(x1)
        if y_pred == 1:
            with st.chat_message("assistant"):
                with st.spinner('''در حال تحلیل'''):
                    time.sleep(3)
                    st.success(u'\u2713''تحلیل انجام شد')
                    st.write("<h4 style='text-align: right; color: gray;'>بر اساس تحلیل من، تصویر وارد شده سگ است</h4>", unsafe_allow_html=True)
        elif y_pred == 0:
            with st.chat_message("assistant"):
                with st.spinner('''در حال تحلیل'''):
                    time.sleep(3)
                    st.success(u'\u2713''تحلیل انجام شد')
                    st.write("<h4 style='text-align: right; color: gray;'>بر اساس تحلیل من، تصویر وارد شده گربه است</h4>", unsafe_allow_html=True)

show_page()
