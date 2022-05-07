"""The main entry for the streamlit app"""

import pandas as pd
import streamlit as st


def handle_log_click():
    # TODO: replace with a service call
    print("log")


def render():
    st.write(
        """
        # Throw some buttons on here
        """
    )
    data = pd.DataFrame([[1, 2], [3, 4]], columns=["test1", "test2"])
    st.button("Log", on_click=handle_log_click)
    st.write(data)
    st.bar_chart(data)


render()
