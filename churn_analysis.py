
import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('/content/Churn_Modelling.csv')

st.title('Churn Analysis')

tab1 , tab2 = st.tabs(['Descriptive statistics', 'Charts'])

num = df.describe()
cat = df.describe(include='O')

with tab1:
  col1, col2, col3 = st.columns(3)
  with col1:
    st.subheader('Numerical descriptive Data')
    st.dataframe(num)
  with col3:
    st.subheader('Categorical descriptive Data')
    st.dataframe(cat)

with tab2:
  col1, col2, col3 = st.columns(3)
  with col1:
    filter = st.sidebar.selectbox('Select country', df['Geography'].unique())
    filtered_data = df[df['Geography']==filter]

    st.header('pie chart')
    fig = px.pie(filtered_data,names='Exited')
    st.plotly_chart(fig,use_container_width=True)
    
    st.header('bar chart')
    fig = filtered_data.groupby(['Geography','Gender'])['Exited'].sum().reset_index()
    fig = px.bar(fig,x='Geography',y='Exited',color='Gender',barmode='group')
    st.plotly_chart(fig,use_container_width=True)
  with col3:
    st.header('scatter chart')
    fig = px.scatter(filtered_data,x='Age',y='Balance',color='Exited')
    st.plotly_chart(fig,use_container_width=True)

    st.header('heatmap chart')
    fig = px.imshow(filtered_data.select_dtypes(exclude='O').corr().round(2), aspect= 'auto',text_auto=True)
    st.plotly_chart(fig,use_container_width=True)

