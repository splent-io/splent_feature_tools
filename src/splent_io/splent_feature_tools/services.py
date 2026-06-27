from splent_io.splent_feature_tools.repositories import ToolsRepository
from splent_framework.services.BaseService import BaseService


class ToolsService(BaseService):
    def __init__(self):
        super().__init__(ToolsRepository())

    def list_published(self):
        return self.repository.list_published()

    def get_by_slug(self, slug: str):
        return self.repository.get_by_slug(slug)

    def grouped_by_status(self):
        return self.repository.grouped_by_status()
