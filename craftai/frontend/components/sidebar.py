"""Sidebar component for the app."""

import reflex as rx

from .. import styles


def sidebar_header() -> rx.Component:
    """Sidebar header.

    Returns:
        The sidebar header component.
    """
    return rx.hstack(
        # The logo.
        rx.image(src="/logo.png", height="1.5em"),
        rx.spacer(),
        align="center",
        width="100%",
        padding="0.35em",
        margin_bottom="1em",
    )


def sidebar_item_icon(icon: str) -> rx.Component:
    return rx.icon(icon, size=18)


def sidebar_footer() -> rx.Component:
    """Sidebar footer.

    Returns:
        The sidebar footer component.
    """
    return rx.hstack(
        rx.link(sidebar_item_icon("settings"), href="/settings"),
        rx.spacer(),
        rx.color_mode.button(style={"opacity": "0.8", "scale": "0.95"}),
        justify="start",
        align="center",
        width="100%",
        padding="0.35em",
    )


def sidebar_item(text: str, url: str, icon: str = "layout-dashboard") -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # Whether the item is active.
    active = (rx.State.router.page.path == url.lower()) | ((rx.State.router.page.path == "/") & text == "Overview")

    return rx.link(
        rx.hstack(
            sidebar_item_icon(icon),
            rx.text(text, size="3", weight="regular"),
            color=rx.cond(
                active,
                styles.accent_text_color,
                styles.text_color,
            ),
            style={
                "_hover": {
                    "background_color": rx.cond(
                        active,
                        styles.accent_bg_color,
                        styles.gray_bg_color,
                    ),
                    "color": rx.cond(
                        active,
                        styles.accent_text_color,
                        styles.text_color,
                    ),
                    "opacity": "1",
                },
                "opacity": rx.cond(
                    active,
                    "1",
                    "0.95",
                ),
            },
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            spacing="2",
            padding="0.35em",
        ),
        underline="none",
        href=url,
        width="100%",
    )


def sidebar() -> rx.Component:
    """The sidebar.

    Returns:
        The sidebar component.
    """
    sidebar_nav = [
        ("/", "Overview", "layout-dashboard"),
        ("/chatbots", "Chat-bots", "bot-message-square"),
        ("/agents", "Agents", "pocket-knife"),
        ("/tasks", "Tasks", "briefcase-business"),
    ]
    sidebar_secondary_nav = [
        ("/connectors", "Connectors", "cable"),
    ]
    return rx.flex(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
                *[sidebar_item(text=title, url=url, icon=icon) for url, title, icon in sidebar_nav]
                + [rx.separator()]
                + [sidebar_item(text=title, url=url, icon=icon) for url, title, icon in sidebar_secondary_nav],
                spacing="1",
                width="100%",
            ),
            rx.spacer(),
            sidebar_footer(),
            justify="end",
            align="end",
            width=styles.sidebar_content_width,
            height="100dvh",
            padding="1em",
        ),
        display=["none", "none", "none", "none", "none", "flex"],
        max_width=styles.sidebar_width,
        width="auto",
        height="100%",
        position="sticky",
        justify="end",
        top="0px",
        left="0px",
        flex="1",
        bg=rx.color("gray", 2),
    )
