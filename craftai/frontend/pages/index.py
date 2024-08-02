"""The dashboard page."""

import reflex as rx

from craftai.frontend.templates.main import template


@template(route="/", title="Overview")
def index() -> rx.Component:
    """The overview page."""
    return rx.vstack(
        rx.heading("Overview", size="5"),
        spacing="8",
        width="100%",
    )
