import re

from flask import (
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required

from splent_io.splent_feature_tools import tools_bp
from splent_io.splent_feature_tools.models import Tool
from splent_framework.db import db
from splent_framework.services.service_locator import service_proxy

tools_service = service_proxy("ToolsService")


# =====================================================================
# PUBLIC
# =====================================================================
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


# =====================================================================
# ADMIN — domain-specific management (the "plugin" screen)
# =====================================================================
# Status values that always lead the group select, in this order. Any other
# distinct status present in the DB is appended after these.
KNOWN_STATUSES = ["active", "prototype", "other"]


def _slugify(value):
    base = re.sub(r"[^a-z0-9]+", "-", (value or "").lower()).strip("-")
    return base or "tool"


def _unique_slug(name, exclude_id=None):
    base = _slugify(name)
    slug, i = base, 2
    while True:
        q = Tool.query.filter_by(slug=slug)
        if exclude_id:
            q = q.filter(Tool.id != exclude_id)
        if not q.first():
            return slug
        slug, i = f"{base}-{i}", i + 1


def _ordered_groups():
    """All tools (incl. drafts) grouped by status; KNOWN_STATUSES first, extras after."""
    grouped = {}
    for t in Tool.query.order_by(Tool.order.asc(), Tool.name.asc()).all():
        grouped.setdefault(t.status or "other", []).append(t)
    ordered = {g: grouped.pop(g) for g in KNOWN_STATUSES if g in grouped}
    ordered.update(grouped)
    return ordered


def _known_groups():
    existing = [s[0] for s in db.session.query(Tool.status).distinct().all() if s[0]]
    seen, out = set(), []
    for g in KNOWN_STATUSES + existing:
        if g and g not in seen:
            seen.add(g)
            out.append(g)
    return out


def _form_to_data(form):
    return {
        "name": (form.get("name") or "").strip(),
        "summary": (form.get("summary") or "").strip(),
        "description": (form.get("description") or "").strip(),
        "logo": (form.get("logo") or "").strip(),
        "github": (form.get("github") or "").strip(),
        "website": (form.get("website") or "").strip(),
        "status": (form.get("status") or "other").strip() or "other",
        "order": int(form.get("order") or 0),
        "published": bool(form.get("published")),
    }


@tools_bp.route("/admin/tools", methods=["GET"])
@login_required
def admin_index():
    return render_template(
        "tools/admin/list.html",
        groups=_ordered_groups(),
        known_groups=_known_groups(),
    )


@tools_bp.route("/admin/tools/new", methods=["GET", "POST"])
@login_required
def admin_new():
    if request.method == "POST":
        data = _form_to_data(request.form)
        if not data["name"]:
            flash("Name is required.", "danger")
            return redirect(url_for("tools.admin_new"))
        data["slug"] = _unique_slug(data["name"])
        db.session.add(Tool(**data))
        db.session.commit()
        flash(f"Added {data['name']}.", "success")
        return redirect(url_for("tools.admin_index"))
    return render_template(
        "tools/admin/form.html", tool=None, known_groups=_known_groups()
    )


@tools_bp.route("/admin/tools/<int:tool_id>/edit", methods=["GET", "POST"])
@login_required
def admin_edit(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    if request.method == "POST":
        data = _form_to_data(request.form)
        if not data["name"]:
            flash("Name is required.", "danger")
            return redirect(url_for("tools.admin_edit", tool_id=tool_id))
        if data["name"] != tool.name:
            data["slug"] = _unique_slug(data["name"], exclude_id=tool.id)
        for key, value in data.items():
            setattr(tool, key, value)
        db.session.commit()
        flash(f"Updated {tool.name}.", "success")
        return redirect(url_for("tools.admin_index"))
    return render_template(
        "tools/admin/form.html", tool=tool, known_groups=_known_groups()
    )


@tools_bp.route("/admin/tools/<int:tool_id>/move", methods=["POST"])
@login_required
def admin_move(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    new_group = (request.form.get("group") or "").strip()
    if new_group and new_group != tool.status:
        tool.status = new_group
        db.session.commit()
        flash(f"Moved {tool.name} to {new_group}.", "success")
    return redirect(url_for("tools.admin_index"))


@tools_bp.route("/admin/tools/<int:tool_id>/delete", methods=["POST"])
@login_required
def admin_delete(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    name = tool.name
    db.session.delete(tool)
    db.session.commit()
    flash(f"Removed {name}.", "success")
    return redirect(url_for("tools.admin_index"))
