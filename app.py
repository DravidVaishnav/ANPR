'''
file for streamlit, can be run with
streamlit run app.py
'''



import streamlit as st
import os
import shutil
# import predict


st.title('Number Plate Recognition')
st.divider()

with st.sidebar:
    st.header('upload your image, video of vehicle and get the output with recognized numberplate')
    st.divider()
    option = st.selectbox(
        'select type of file',
        ('Image', 'Video')
    )
    st.divider()
    uploaded_file = st.file_uploader('Upload')

cur_dir = os.getcwd()
obj_dir_path = 'runs/detect/train'
fin_det_path = os.path.join(cur_dir, obj_dir_path)

# try:
if uploaded_file is not None:
    path = fin_det_path + '/' + uploaded_file.name
    try:
        shutil.rmtree(fin_det_path)
    except:
        pass
    if option == 'Image':
        img = uploaded_file
        st.subheader('Original Image')
        st.image(img)
        st.text(type(img))
        st.divider()
        # predict.predict({"source":img})
        st.subheader('Output Image')
        st.image(path)


    else:
        st.text(type(uploaded_file))
        video_bytes = uploaded_file.read()
        st.subheader('Original Video')
        st.video(video_bytes)
        st.divider()
        # predict.predict({"source":uploaded_file})
        st.subheader('Output Video')
        fin_vid = open(path,'rb')
        fin_video_bytes = fin_vid.read()
        st.video(fin_video_bytes)



