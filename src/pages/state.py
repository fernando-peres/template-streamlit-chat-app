"""
state management (page)
"""

import streamlit as st

from ui.sidebar import Sidebar


class StatePage:
    """Class for the State Management Page UI."""

    def __init__(self) -> None:
        self.title = "State Management"
        self.description = "This page demonstrates state management in Streamlit."

    def render(self) -> None:
        st.title(self.title)
        st.write(self.description)

        if "counter" not in st.session_state:
            st.session_state.counter = 0

        increment = st.button("Increment Counter")
        if increment:
            st.session_state.counter += 1

        st.write(f"Counter Value: {st.session_state.counter}")

        sidebar = Sidebar()
        sidebar.render()


state_page = StatePage()
state_page.render()
