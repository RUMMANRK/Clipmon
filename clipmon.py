import AppKit
import time
import sqlite3
import sys
from urllib.parse import urlparse

def is_url(text):
    """Check if a string is a valid URL."""
    try:
        result = urlparse(text)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def get_clipboard_content(pasteboard=None):
    """Retrieve the current clipboard content."""
    if pasteboard is None:
        pasteboard = AppKit.NSPasteboard.generalPasteboard()
    content = pasteboard.stringForType_(AppKit.NSStringPboardType)
    if content:
        return content.strip()
    return None


def initialize_database(db_name):
    """Initialize the SQLite database."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clipboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn


def output_database_to_file(db_name, output_file):
    """Output all clipboard content from the database to a text file."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM clipboard")
    contents = cursor.fetchall()
    with open(output_file, "w") as file:
        for (content,) in contents:
            file.write(content + "\n")
    conn.close()
    print(f"Exported {len(contents)} entries to {output_file}")


def monitor_clipboard_with_db(db_name, check_urls=True):
    """Monitor clipboard and store content in the database."""
    conn = initialize_database(db_name)
    cursor = conn.cursor()
    print("Monitoring clipboard... Press Ctrl+C to stop.")
    seen_contents = set()

    while True:
        try:
            clipboard_content = get_clipboard_content()
            if clipboard_content and (not check_urls or is_url(clipboard_content)):
                if clipboard_content not in seen_contents:
                    seen_contents.add(clipboard_content)
                    try:
                        cursor.execute("INSERT INTO clipboard (content) VALUES (?)", (clipboard_content,))
                        conn.commit()
                        print(f"New content added: {clipboard_content}")
                    except sqlite3.IntegrityError:
                        pass  # Content already exists
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping clipboard monitoring.")
            break

    conn.close()


def monitor_clipboard_to_file(output_file, check_urls=True):
    """Monitor clipboard and store content in a text file."""
    seen_contents = set()
    print("Monitoring clipboard... Press Ctrl+C to stop.")

    while True:
        try:
            clipboard_content = get_clipboard_content()
            if clipboard_content and (not check_urls or is_url(clipboard_content)):
                if clipboard_content not in seen_contents:
                    seen_contents.add(clipboard_content)
                    with open(output_file, "a") as file:
                        file.write(clipboard_content + "\n")
                    print(f"New content: {clipboard_content}")
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping clipboard monitoring.")
            break


def main():
    args = sys.argv[1:]

    # Determine if URL checking is disabled
    check_urls = "-nourl" not in args

    if "-db" in args:
        try:
            db_name = args[args.index("-db") + 1]
            monitor_clipboard_with_db(db_name, check_urls=check_urls)
        except IndexError:
            print("Error: Missing database name after '-db' flag.")
    elif "-dboutput" in args:
        try:
            db_name = args[args.index("-dboutput") + 1]
            output_file = args[args.index("-dboutput") + 2]
            output_database_to_file(db_name, output_file)
        except IndexError:
            print("Error: Missing arguments for '-dboutput' flag.")
    else:
        output_file = "collected_clipboard.txt"
        monitor_clipboard_to_file(output_file, check_urls=check_urls)


if __name__ == "__main__":
    main()
