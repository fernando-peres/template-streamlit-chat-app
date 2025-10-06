"""
Sidebar - UI
"""

import streamlit as st


class Sidebar:
    """Class for the Sidebar UI."""

    def __init__(self) -> None:
        self.title = "Sidebar"
        self.options = ["Home", "About", "Contact"]

    def render(self) -> None:
        st.sidebar.title(self.title)
        self.selected_option = st.sidebar.radio("Navigate to:", self.options)
