# 📋 ClipMon: The Ultimate Clipboard Monitor for macOS

*Effortlessly collect and manage your clipboard content like never before!*

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Command-Line Options](#command-line-options)
- [Tutorial](#tutorial)
- [Edge Cases](#edge-cases)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Ever found yourself juggling multiple pieces of text or URLs, wishing there was an easier way to keep track of everything you copy? Say hello to **ClipMon**, your new best friend for clipboard management on macOS!

ClipMon is a Python script that monitors your clipboard in real-time, capturing text and URLs and storing them in either a SQLite database or a simple text file. Whether you're researching, coding, or just surfing the web, ClipMon ensures you never lose a valuable snippet again.

---

## Features

- 📋 **Real-Time Monitoring**: Keep an eye on your clipboard 24/7.
- 🌐 **URL Detection**: Automatically filter and store valid URLs.
- 💾 **Flexible Storage**: Choose between SQLite database or plain text file.
- 🛠 **Easy Customization**: Simple command-line options to suit your needs.
- 🔄 **Export Functionality**: Easily export your collected data for later use.

---

## Installation

### Prerequisites

- **macOS**: This script is designed specifically for macOS.
- **Python 3**: Make sure you have Python 3 installed. You can check by running:

  ```bash
  python3 --version
  ```

- **Python Packages**: You'll need the following Python packages:
  - `AppKit`
  - `sqlite3`

### Steps

1. **Clone the Repository** (or download the script directly):

   ```bash
   git clone https://github.com/yourusername/clipmon.git
   ```

2. **Navigate to the Directory**:

   ```bash
   cd clipmon
   ```

3. **Install Required Packages**:

   - Install `pyobjc` to get access to `AppKit`:

     ```bash
     pip3 install pyobjc
     ```

---

## Usage

### Basic Usage

To start monitoring your clipboard and saving URLs to a text file:

```bash
python3 clipmon.py
```

### Command-Line Options

- **`-db <database_name>`**: Store clipboard content in a SQLite database.

  ```bash
  python3 clipmon.py -db my_clipboard.db
  ```

- **`-dboutput <database_name> <output_file>`**: Export database content to a text file.

  ```bash
  python3 clipmon.py -dboutput my_clipboard.db exported_clipboard.txt
  ```

- **`-nourl`**: Disable URL checking to capture all clipboard content.

  ```bash
  python3 clipmon.py -nourl
  ```

---

## Tutorial

Ready to become a ClipMon pro? Let's dive in!

### Step 1: Start Basic Monitoring

Open your terminal and run:

```bash
python3 clipmon.py
```

ClipMon will now monitor your clipboard and save any valid URLs to `collected_clipboard.txt`.

### Step 2: Copy Some URLs

- Open your web browser.
- Copy a few URLs.
- Watch as ClipMon detects and logs them!

### Step 3: Use the SQLite Database Option

Want to store your clipboard content in a database? Use the `-db` option:

```bash
python3 clipmon.py -db my_clipboard.db
```

### Step 4: Export Your Data

After collecting data, you might want to export it:

```bash
python3 clipmon.py -dboutput my_clipboard.db exported_clipboard.txt
```

### Step 5: Capture All Clipboard Content

Need more than just URLs? Disable URL checking:

```bash
python3 clipmon.py -nourl
```

Now, every piece of text you copy will be recorded.

### Step 6: Stop Monitoring

- Simply press `Ctrl+C` in the terminal.
- ClipMon will gracefully stop and save all your data.

---

## Edge Cases

While ClipMon is designed to be robust, here are some edge cases to be aware of:

- **Non-Text Clipboard Content**: ClipMon only captures text data. Images, files, or other non-text content will be ignored.
- **Rapid Copying**: Copying content extremely rapidly may cause some entries to be missed due to the 1-second sleep interval. Adjust the sleep time in the script if necessary.
- **Database Integrity**: If using the database option, ensure the script has permission to write to the directory to avoid database errors.
- **Unicode Characters**: Clipboard content with unusual Unicode characters may cause unexpected behavior.

---

## FAQ

### Q1: Can I use ClipMon on Windows or Linux?

**A**: Currently, ClipMon is designed specifically for macOS due to its reliance on the `AppKit` framework. However, with some modifications, it could be adapted for other operating systems.

### Q2: How do I change the output file name?

**A**: By default, the script writes to `collected_clipboard.txt`. You can modify the script or use the database option to specify an output file during export.

### Q3: Is there a way to adjust the clipboard check interval?

**A**: Yes! In the script, you can modify the `time.sleep(1)` line to change the interval (in seconds) between clipboard checks.

### Q4: I'm getting a permission error when writing to the database. What do I do?

**A**: Ensure that the directory you're running the script in is writable. You might need to adjust the directory permissions or run the script from a different location.

### Q5: How can I contribute to the project?

**A**: We'd love your help! See the [Contributing](#contributing) section below.

---

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue on GitHub. Whether it's a bug fix, feature request, or documentation improvement, we appreciate your input.

---

## License

This project is licensed under the MIT License.

---

*Happy clipping! If ClipMon has made your life easier, consider giving us a star on GitHub. ⭐*