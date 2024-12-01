import unittest
from unittest.mock import MagicMock
import os
import sqlite3
from clipmon import (
    is_url,
    initialize_database,
    output_database_to_file,
    get_clipboard_content,
)

class TestClipboardCollector(unittest.TestCase):
    def setUp(self):
        """Set up a temporary database and test environment."""
        self.test_db = "test_clipboard.db"
        self.test_output_file = "test_output.txt"
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        if os.path.exists(self.test_output_file):
            os.remove(self.test_output_file)

    def tearDown(self):
        """Clean up the test environment."""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        if os.path.exists(self.test_output_file):
            os.remove(self.test_output_file)

    def test_is_url(self):
        """Test the URL validation function."""
        self.assertTrue(is_url("https://example.com"))
        self.assertTrue(is_url("http://example.com"))
        self.assertFalse(is_url("example.com"))
        self.assertFalse(is_url("not a url"))

    def test_initialize_database(self):
        """Test database initialization."""
        conn = initialize_database(self.test_db)
        cursor = conn.cursor()

        # Check if the table is created
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clipboard'")
        self.assertEqual(cursor.fetchone()[0], "clipboard")

        # Check if columns are present
        cursor.execute("PRAGMA table_info(clipboard)")
        columns = [info[1] for info in cursor.fetchall()]
        self.assertIn("content", columns)
        self.assertIn("created_at", columns)

        conn.close()

    def test_output_database_to_file(self):
        """Test exporting database content to a text file."""
        conn = initialize_database(self.test_db)
        cursor = conn.cursor()

        # Insert test data
        test_data = ["https://example1.com", "https://example2.com"]
        for data in test_data:
            cursor.execute("INSERT INTO clipboard (content) VALUES (?)", (data,))
        conn.commit()

        # Export to file
        output_database_to_file(self.test_db, self.test_output_file)

        # Verify file content
        with open(self.test_output_file, "r") as f:
            lines = f.read().strip().split("\n")
            self.assertEqual(lines, test_data)

        conn.close()

    def test_get_clipboard_content(self):
        """Test retrieving clipboard content."""
        # Create a mock pasteboard instance
        mock_pasteboard = MagicMock()
        mock_pasteboard.stringForType_.return_value = "https://example.com"

        # Test clipboard content retrieval
        content = get_clipboard_content(pasteboard=mock_pasteboard)
        self.assertEqual(content, "https://example.com")

        # Test with empty clipboard
        mock_pasteboard.stringForType_.return_value = None
        content = get_clipboard_content(pasteboard=mock_pasteboard)
        self.assertIsNone(content)

if __name__ == "__main__":
    unittest.main()
