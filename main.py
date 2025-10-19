import os
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
        
        # Check if the query starts with a preprompt keyword
        query_parts = query.split(maxsplit=1)
        preprompt_keyword = query_parts[0] if query_parts else ""
        user_query = query_parts[1] if len(query_parts) > 1 else ""
        
        # Get the path to preprompts folder from preferences
        preprompts_dir = extension.preferences.get('preprompts_location')
        
        # Fallback to default location if not set
        if not preprompts_dir:
            extension_dir = os.path.dirname(os.path.abspath(__file__))
            preprompts_dir = os.path.join(extension_dir, 'prepromts')
        
        preprompt_file = os.path.join(preprompts_dir, preprompt_keyword)
        
        # Check if preprompt file exists
        if os.path.isfile(preprompt_file):
            try:
                with open(preprompt_file, 'r') as f:
                    preprompt_text = f.read().strip()
                
                # Combine preprompt with user query
                combined_query = preprompt_text + " " + user_query if user_query else preprompt_text
                
                search_url = f"https://www.perplexity.ai/search?s=o&q={combined_query}"
                items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name=f'Search with "{preprompt_keyword}" preprompt',
                    description=f'Query: {user_query if user_query else "(no additional query)"}',
                    on_enter=OpenUrlAction(search_url)
                ))
            except Exception as e:
                items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name='Error reading preprompt',
                    description=str(e),
                    on_enter=OpenUrlAction("https://www.perplexity.ai/")
                ))
        else:
            # No preprompt found, use query as-is
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
