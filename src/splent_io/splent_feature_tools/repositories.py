from __future__ import annotations

from collections import OrderedDict

from splent_io.splent_feature_tools.models import Tool
from splent_framework.repositories.BaseRepository import BaseRepository


class ToolsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Tool)

    def list_published(self) -> list[Tool]:
        return (
            Tool.query.filter_by(published=True)
            .order_by(Tool.order.asc(), Tool.name.asc())
            .all()
        )

    def get_by_slug(self, slug: str) -> Tool | None:
        return Tool.query.filter_by(slug=slug).first()

    def grouped_by_status(self) -> "OrderedDict[str, list[Tool]]":
        groups: "OrderedDict[str, list[Tool]]" = OrderedDict()
        for tool in self.list_published():
            groups.setdefault(tool.status or "other", []).append(tool)
        return groups
