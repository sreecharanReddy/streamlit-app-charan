import streamlit as st
import numpy as np
import pandas as pd
import time

###################
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

###################
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

###################
st.write("Here's our first attempt at styler:")

dataframe = pd.DataFrame(
    np.random.randn(30, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

###################
st.write("Line chart:")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
###################
st.write("Using checkbox to show Map:")

if st.checkbox('Show Map'):
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)


###################
st.text_input("Your name", key="name", placeholder='number', value='charan')

###################
st.write("Widget:")
x = st.slider(st.session_state.name, min_value=10, max_value=500)  # 👈 this is a widget
st.write(x, 'squared is', x * x)


###################
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

################### Progress Bar

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.2)

'...and now we\'re done!'