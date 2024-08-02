"""Welcome to Reflex!."""

# Import all the pages.

import reflex as rx

import craftai.frontend.pages as pages  # noqa: F401
from craftai.frontend import styles

# Create the app.
app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
)
