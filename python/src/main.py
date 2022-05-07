"""The main entry for the streamlit app"""

import streamlit as st


def handle_log_click():
    # TODO: replace with a service call
    print("Clicked!!!")


def render():
    st.write(
        """
        # Throw some buttons on here
        """
    )

    st.button("Log", on_click=handle_log_click)


render()
