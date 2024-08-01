"""The dashboard page."""

import reflex as rx

from craftai.templates.main import template


@template(route="/", title="Overview")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Overview", size="5"),
        spacing="8",
        width="100%",
    )
