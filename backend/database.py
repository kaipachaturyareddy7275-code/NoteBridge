
import sqlite3
from pathlib import Path
from datetime import datetime

DATABASE_PATH = Path(__file__).resolve().parent.parent / "notebridge.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            file_path TEXT NOT NULL,
            upload_date TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    
def insert_document(filename, file_path):
    conn = get_db_connection()

    conn.execute(
        """
        INSERT INTO documents (filename, file_path, upload_date)
        VALUES (?, ?, ?)
        """,
        (filename, file_path, datetime.now().isoformat())
    )

    conn.commit()
    conn.close()
    

def get_all_documents():
    conn = get_db_connection()

    documents = conn.execute(
        "SELECT * FROM documents"
    ).fetchall()

    conn.close()

    return [dict(document) for document in documents]

def get_document_by_id(document_id):
    conn = get_db_connection()

    document = conn.execute(
        "SELECT * FROM documents WHERE id = ?",
        (document_id,)
    ).fetchone()

    conn.close()

    return dict(document) if document else None


def update_document(document_id, new_filename, new_file_path):
    conn = get_db_connection()

    cursor = conn.execute(
        """
        UPDATE documents
        SET filename = ?, file_path = ?
        WHERE id = ?
        """,
        (new_filename, new_file_path, document_id)
    )

    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()

    return updated


def delete_document(document_id):
    conn = get_db_connection()

    cursor = conn.execute(
        "DELETE FROM documents WHERE id = ?",
        (document_id,)
    )

    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()

    return deleted


