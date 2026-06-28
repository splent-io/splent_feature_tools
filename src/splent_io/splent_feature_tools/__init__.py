from splent_framework.blueprints.base_blueprint import create_blueprint
from splent_framework.services.service_locator import register_service

from splent_io.splent_feature_tools.services import ToolsService

tools_bp = create_blueprint(__name__)


def init_feature(app):
    # Tools is managed through its OWN custom admin screens (see routes.py and
    # hooks.py) — the WordPress-plugin pattern — instead of the generic admin
    # resource, so it does not call register_admin_resource.
    register_service(app, "ToolsService", ToolsService)


def inject_context_vars(app):
    return {}
