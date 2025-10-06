"""
chat ui (page)
"""

import streamlit as st

from ui.sidebar import Sidebar


class ChatPage:
    """Class for the Chat Page UI."""

    def __init__(self) -> None:
        self.title = "Chat with AI"
        self.description = "This is the chat page where you can interact with the AI."

    def render(self) -> None:
        st.title(self.title)
        st.write(self.description)

        sidebar = Sidebar()
        sidebar.render()


chat_page = ChatPage()
chat_page.render()
