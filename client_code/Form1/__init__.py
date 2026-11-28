from ._anvil_designer import Form1Template
import anvil.js


class Form1(Form1Template):

    def __init__(self, **properties):
        super().__init__(**properties)

    def search_form_submit(self, event):
        event.preventDefault()

        query = self.dom_nodes["search_input"].value.strip()

        if query:
            self.display_search_results(query)

    def display_search_results(self, query):

        section = self.dom_nodes["results_section"]
        status = self.dom_nodes["search_status"]
        results_area = self.dom_nodes["search_results"]

        section.style.display = "block"
        status.innerText = "Searching JAC APP..."
        results_area.innerHTML = ""

        api_url = (
            "http://127.0.0.1:8000/search?q="
            + anvil.js.window.encodeURIComponent(query)
        )

        def process_response(response):

            if not response.ok:
                status.innerText = (
                    "Search error: " + str(response.status)
                )
                return

            def process_results(data):

                results = data.get("results", [])

                if not results:
                    status.innerText = "No results found for: " + query
                    return

                status.innerText = (
                    str(len(results)) + " results found for: " + query
                )

                document = anvil.js.window.document

                for result in results:

                    card = document.createElement("div")
                    card.className = "jac-result-card"

                    title = document.createElement("h3")
                    title.innerText = result.get("title", "Untitled")

                    description = document.createElement("p")
                    description.innerText = result.get("description", "")

                    card.appendChild(title)
                    card.appendChild(description)

                    url = result.get("url", "")

                    if url.startswith(("https://", "http://")):

                        link = document.createElement("a")
                        link.href = url
                        link.target = "_blank"
                        link.rel = "noopener noreferrer"
                        link.innerText = url

                        card.appendChild(link)

                    results_area.appendChild(card)

            return response.json().then(process_results)

        def handle_error(error):

            status.innerText = (
                "Search failed. Check the API connection."
            )
            print("JAC APP error:", error)

        try:

            anvil.js.window.fetch(api_url).then(
                process_response
            ).catch(handle_error)

        except Exception as error:

            status.innerText = "Could not start search."
            print("JAC APP error:", error)
