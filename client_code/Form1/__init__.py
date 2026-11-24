from ._anvil_designer import Form1Template
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js
from anvil.js.window import URL, open as open_window


class Form1(Form1Template):
    def __init__(self, **properties):
        super().__init__(**properties)

    def search_form_submit(self, event):
        event.preventDefault()
        self.open_search(self.dom_nodes["search_input"].value)

    def quick_search_click(self, event):
        query = event.currentTarget.getAttribute("data-query")
        self.dom_nodes["search_input"].value = query
        self.open_search(query)

    def open_search(self, query):
        query = query.strip()
        if not query:
            return

        engine = self.dom_nodes["engine"].value
        if engine == "google":
            base_url = "https://www.google.com/search"
        elif engine == "bing":
            base_url = "https://www.bing.com/search"
        else:
            base_url = "https://duckduckgo.com/"

        search_url = anvil.js.new(URL, base_url)
        search_url.searchParams.set("q", query)
        open_window(search_url.href, "_blank")
