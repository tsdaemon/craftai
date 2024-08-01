"""Welcome to Reflex!."""

# Import all the pages.
from typing import Callable
from reflex.app import ComponentCallable
from reflex.constants.route import DefaultPage
from reflex.event import EventSpec
from .pages import *
from . import styles

import reflex as rx

class CraftAiApp(rx.App):
    def add_page(
        self, component: rx.Component | Callable[[], rx.Component], 
        route: str | None = None, title: str | None = None, description: str | None = None, 
        image: str = "icon.png", 
        on_load: rx.EventHandler | EventSpec | list[rx.EventHandler | EventSpec] | None = None, 
        meta: list[dict[str, str]] = rx.constants.DefaultPage.META_LIST
    ):
        return super().add_page(component, route, title, description, image, on_load, meta)


# Create the app.
app = CraftAiApp(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
)
