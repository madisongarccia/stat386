import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Popular Name Trends')

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

name = st.text_input(label ='Enter a name', value = 'John')
name_df = df[df['name'] == name]

tab1, tab2 = st.tabs(['Female', 'Male'])


with tab1:
    st.header(f'{name} Over Time')
    plot_df = name_df[name_df['sex'] =='F']
    fig_f = px.line(plot_df, x='year', y='n')
    st.plotly_chart(fig_f)

with tab2:
    st.header(f'{name} Over Time')
    plot_df = name_df[name_df['sex'] =='M']
    fig_m = px.line(plot_df, x='year', y='n')
    st.plotly_chart(fig_m)


with st.sidebar:
    year = st.slider('Choose a year', 1910, 2021)
    st.header(f'Top Names in {year}')
    year_df = df[df['year'] == year]
    girls_names = year_df[year_df.sex=='F'].sort_values('n', ascending=False).head(5)['name']
    boys_names = year_df[year_df.sex=='M'].sort_values('n', ascending=False).head(5)['name']

    top_names = pd.concat([girls_names.reset_index(drop=True), boys_names.reset_index(drop=True)], ignore_index=True, axis=1)
    top_names.columns = ['Girls','Boys']
    top_names.index = [1,2,3,4,5]
    st.dataframe(top_names)
#name_df = name_df.groupby('year')['n'].sum().reset_index()

#fig = px.line(name_df, x='year', y='n')

#st.plotly_chart(fig)

