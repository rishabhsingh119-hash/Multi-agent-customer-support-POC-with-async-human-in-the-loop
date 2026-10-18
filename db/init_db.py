"""Builds (or rebuilds) the database from schema.sql + seed_data.sql.

Run it whenever you want a clean dataset:
    uv run python -m db.init_db
"""
from pathlib import Path

from config import DB_PATH
from db.connection import get_admin_connection



_DB_DIR = Path(__file__).parent
_SCHEMA_PATH = _DB_DIR / "schema.sql"
_SEED_DATA_PATH = _DB_DIR / "seed_data.sql"


def build_database() -> None:
    schema_sql = _SCHEMA_PATH.read_text()
    seed_sql = _SEED_DATA_PATH.read_text()

    conn = get_admin_connection()
    try:
        conn.executescript(schema_sql)
        conn.executescript(seed_sql)
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    build_database()
    print(f"Database built and seeded at {Path(DB_PATH).resolve()}")