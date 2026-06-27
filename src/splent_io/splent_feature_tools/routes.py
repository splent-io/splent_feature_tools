from flask import abort, render_template

from splent_io.splent_feature_tools import tools_bp
from splent_framework.services.service_locator import service_proxy

tools_service = service_proxy("ToolsService")


@tools_bp.route("/tools", methods=["GET"])
def index():
    groups = tools_service.grouped_by_status()
    return render_template("tools/list.html", groups=groups)


@tools_bp.route("/tools/<slug>", methods=["GET"])
def detail(slug):
    tool = tools_service.get_by_slug(slug)
    if tool is None:
        abort(404)
    return render_template("tools/detail.html", tool=tool)
