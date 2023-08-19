import streamlit as st
import pandas as pd
import numpy as np
import time


st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


@st.cache_data
def num_pickups_by_hour(df):
    time.sleep(5)
    st.subheader('Number of pickups by hour')
    hist_values = np.histogram(
        data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
    st.bar_chart(hist_values)


def add_map(data, hour_to_filter):
    st.subheader('Map of all pickups')
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
    st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    st.map(filtered_data)


def add_slider_widget():
    st.write("Widget:")
    hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
    return hour_to_filter


if __name__ == '__main__':
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(10001)
    # Notify the reader that the data was successfully loaded.
    data_load_state.text("Done! (using st.cache_data)")
    st.subheader('Raw data')

    st.write(data)

    num_pickups_by_hour(data)

    hour_to_filter = add_slider_widget()

    add_map(data, hour_to_filter)






