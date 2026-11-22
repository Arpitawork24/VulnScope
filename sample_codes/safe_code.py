"""Safe example: use a parameterized database query."""

import sqlite3


def find_user(user_id: int) -> tuple[str, ...]:
    with sqlite3.connect(":memory:") as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)"
        )
        rows = connection.execute(
            "SELECT name FROM users WHERE id = ?",
            (user_id,),
        ).fetchall()
    return tuple(row[0] for row in rows)
