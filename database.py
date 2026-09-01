import sqlite3


def get_connection():
    return sqlite3.connect(
        "study_planner.db",
        check_same_thread=False
    )


def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            assignment TEXT NOT NULL,
            due_date TEXT,
            priority TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_assignment(
    subject,
    assignment,
    due_date,
    priority,
    status
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO assignments
        (subject, assignment, due_date, priority, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        subject,
        assignment,
        due_date,
        priority,
        status
    ))

    conn.commit()
    conn.close()


def get_assignments():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM assignments"
    )

    data = cursor.fetchall()

    conn.close()

    return data


def update_status(
    assignment_id,
    status
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE assignments
        SET status = ?
        WHERE id = ?
    """, (
        status,
        assignment_id
    ))

    conn.commit()
    conn.close()


def delete_assignment(
    assignment_id
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM assignments WHERE id = ?",
        (assignment_id,)
    )

    conn.commit()
    conn.close()