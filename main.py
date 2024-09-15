import requests
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

class PerplexitySearchExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument()
        if query is None:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='Search Perplexity AI',
                    description='Type your query after the keyword',
                    on_enter=OpenUrlAction("https://www.perplexity.ai/")
                )
            ])

        items = []
        search_url = f"https://www.perplexity.ai/search?s=o&q={query}"
        items.append(ExtensionResultItem(
            icon='images/icon.png',
            name=f'Search Perplexity AI for "{query}"',
            description='Click to open search results',
            on_enter=OpenUrlAction(search_url)
        ))

        return RenderResultListAction(items)

if __name__ == '__main__':
    PerplexitySearchExtension().run()
