from splent_framework.admin import register_admin_resource
from splent_framework.blueprints.base_blueprint import create_blueprint
from splent_framework.services.service_locator import register_service

from splent_io.splent_feature_tools.models import Tool
from splent_io.splent_feature_tools.services import ToolsService

tools_bp = create_blueprint(__name__)


def init_feature(app):
    register_service(app, "ToolsService", ToolsService)

    # Surface Tool in the admin panel (the wp-admin-style back-office).
    register_admin_resource(
        Tool,
        name="tool",
        label="Tool",
        label_plural="Tools",
        icon="tool",
        group="Research",
        order=20,
        list_columns=["name", "status"],
        field_widgets={
            "description": "richtext",
            "logo": "image",
            "github": "url",
            "website": "url",
            "status": "select",
            "summary": "textarea",
            "slug": "slug",
        },
        feature="tools",
    )


def inject_context_vars(app):
    return {}
