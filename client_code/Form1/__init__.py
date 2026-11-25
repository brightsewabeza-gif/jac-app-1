
from ._anvil_designer import Form1Template
import anvil.js
from anvil.js.window import URL, open as open_window


class Form1(Form1Template):

    def __init__(self, **properties):
        super().__init__(**properties)

    def search_form_submit(self, event):
        event.preventDefault()

        query = self.dom_nodes["search_input"].value
        self.open_search(query)

    def quick_search_click(self, event):
        query = event.currentTarget.getAttribute("data-query")

        self.dom_nodes["search_input"].value = query
        self.open_search(query)

    def open_search(self, query):
        query = query.strip()

        if not query:
            return

        # JAC APP API address
        base_url = "http://127.0.0.1:8000"

        # Build JAC search URL
        search_url = anvil.js.new(
            URL,
            base_url + "/search"
        )

        search_url.searchParams.set("q", query)

        # Open JAC search results
        open_window(search_url.href, "_blank")
