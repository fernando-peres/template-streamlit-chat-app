"""
Home Page - UI
"""

import streamlit as st

from ui.sidebar import Sidebar


class HomePage:
    """Class for the Home Page UI."""

    def __init__(self) -> None:
        self.title = "Welcome to the Home Page"
        self.description = "This is the home page of our Streamlit application."

    def render(self) -> None:
        st.title(self.title)
        st.write(self.description)

        sidebar = Sidebar()
        sidebar.render()


if __name__ == "__main__":
    home_page = HomePage()
    home_page.render()
