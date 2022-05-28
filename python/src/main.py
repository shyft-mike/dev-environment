"""The main entry for the streamlit app"""

from pathlib import Path
import pandas as pd
import requests
import streamlit as st


def handle_log_click():
    # TODO: replace with a service call
    print("log")


def handle_load_click():
    with open("src/data/census_2019.csv", "wb") as data_file:
        content = requests.get(
            "https://chronicdata.cdc.gov/resource/k86t-wghb.csv", stream=True
        ).content

        data_file.write(content)


def render():
    st.write(
        """
        # Throw some buttons on here
        """
    )
    data = pd.DataFrame([[1, 2], [3, 4]], columns=["test1", "test2"])
    st.button("Log", on_click=handle_log_click)
    st.button("Load", on_click=handle_load_click)
    st.write(data)
    st.area_chart(data)

    if Path("src/data/census_2019.csv").is_file():
        health_df = pd.read_csv("src/data/census_2019.csv")
        st.write(health_df)


render()
