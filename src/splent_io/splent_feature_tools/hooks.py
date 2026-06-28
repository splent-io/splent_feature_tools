from flask import request, url_for

from splent_framework.hooks.template_hooks import register_template_hook


def tools_admin_link():
    """Sidebar entry for the Tools management screen (the WP-plugin pattern)."""
    active = (
        "active"
        if request.endpoint and request.endpoint.startswith("tools.admin")
        else ""
    )
    return (
        f'<li class="sidebar-item {active}">'
        f'<a class="sidebar-link" href="{url_for("tools.admin_index")}">'
        '<i class="align-middle" data-feather="tool"></i> '
        '<span class="align-middle">Tools</span>'
        "</a>"
        "</li>"
    )


register_template_hook("layout.authenticated_sidebar", tools_admin_link)
