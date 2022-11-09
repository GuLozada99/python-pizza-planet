from typing import Optional

from app.plugins import db


class BaseManager:
    session: Optional[db.Session] = db.session
