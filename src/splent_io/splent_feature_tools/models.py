from splent_framework.db import db


class Tool(db.Model):
    """A research/SPL tool produced or maintained by the lab."""

    __tablename__ = "tool"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True, index=True)
    summary = db.Column(db.Text, default="")
    description = db.Column(db.Text, default="")  # rich text / HTML
    logo = db.Column(db.String(512), default="")
    github = db.Column(db.String(512), default="")
    website = db.Column(db.String(512), default="")
    status = db.Column(db.String(32), default="active")  # active|prototype|other
    order = db.Column(db.Integer, default=0)
    published = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"Tool<{self.slug}>"
