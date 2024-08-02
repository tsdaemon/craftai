"""The connectors list page."""

import reflex as rx

from craftai.entities.connector import Connector
from craftai.frontend.templates.main import template


@template(route="/connectors", title="Connectors")
def list_route() -> rx.Component:
    """The connectors page."""
    return rx.vstack(
        rx.heading("Connectors", size="5"),
        spacing="8",
        width="100%",
    )


class TableState(rx.State):
    """The state class."""

    items: list[Connector] = []

    search_value: str = ""
    sort_value: str = ""
    sort_reverse: bool = False

    total_items: int = 0
    offset: int = 0
    limit: int = 12  # Number of rows per page

    @rx.var(cache=True)
    def filtered_sorted_items(self) -> list[Connector]:
        items = self.items

        # Filter items based on selected item
        if self.sort_value:
            items = sorted(
                items,
                key=lambda item: str(getattr(item, self.sort_value)).lower(),
                reverse=self.sort_reverse,
            )

        # Filter items based on search value
        if self.search_value:
            search_value = self.search_value.lower()
            items = [item for item in items if item.check_search_string(search_value)]

        return items

    @rx.var(cache=True)
    def page_number(self) -> int:
        return (self.offset // self.limit) + 1

    @rx.var(cache=True)
    def total_pages(self) -> int:
        return (self.total_items // self.limit) + (1 if self.total_items % self.limit else 0)

    @rx.var(cache=True, initial_value=[])
    def get_current_page(self) -> list[Connector]:
        start_index = self.offset
        end_index = start_index + self.limit
        return self.filtered_sorted_items[start_index:end_index]

    def prev_page(self) -> None:
        if self.page_number > 1:
            self.offset -= self.limit

    def next_page(self) -> None:
        if self.page_number < self.total_pages:
            self.offset += self.limit

    def first_page(self) -> None:
        self.offset = 0

    def last_page(self) -> None:
        self.offset = (self.total_pages - 1) * self.limit

    def load_items(self) -> None:
        pass

    def toggle_sort(self) -> None:
        self.sort_reverse = not self.sort_reverse
        self.load_items()
