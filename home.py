from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import (MDTabsItemIcon, MDTabsItem)

class HomePage(MDScreen):
    def on_enter(self):
        tabs = self.ids.primary_tabs
        content_container = (
            self.ids.primary_related_content_container
        )
        item = MDTabsItem
        
        for tab_icon, tab_name in {
            "home": "Flights",
            "bell": "Trips",
            "account": "Explore",
            "compass" : "Explore",
            "menu" : "menu"
        }.items():
            tabs.add_widget(
                item(
                    MDTabsItemIcon(
                        icon=tab_icon,
                    )
                )
            )
            content_container.add_widget(
                MDLabel(
                    text=tab_name,
                    halign="center",
                    valign="center",
                )
            )