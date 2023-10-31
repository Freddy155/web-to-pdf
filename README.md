# Web to PDF Converter

## Table of Contents

1. [Introduction](#introduction)

2. [Features](#features)

3. [Requirements](#requirements)

4. [Installation](#installation)

5. [Usage](#usage)

6. [Command-Line Arguments](#command-line-arguments)

7. [Examples](#examples)

8. [Contributing](#contributing)

9. [License](#license)

## Introduction

The "Web to PDF Converter" is a Python application that allows you to convert web pages into PDF documents. This tool is built using the `pdfkit` library, which is a wrapper for the `wkhtmltopdf` command-line tool. With this application, you can convert web content into a more shareable and printable format.

## Features

- Convert web pages to PDF documents.

- Customize PDF output with options like page size and margins.

- Cross-platform support for Windows, Linux, and macOS.

- Easy-to-use command-line interface.

## Requirements

- Python 3.x

- `pdfkit` library

- `wkhtmltopdf` command-line tool

## Installation

1. **Python Installation**: Make sure you have Python 3.x installed on your system.

2. **Install Dependencies**: You need to install the `pdfkit` library. You can do this with pip:

```bash
pip install pdfkit
```

3. **Install `wkhtmltopdf`**:

- On Debian/Ubuntu, you can use `apt-get` to install it:

```bash
sudo apt-get install wkhtmltopdf
```

- On other systems, please refer to the [official website](https://wkhtmltopdf.org/) for installation instructions.

4. **Clone the Repository**:
```bash
git clone https://github.com/Freddy155/web-to-pdf.git
```

5. **Navigate to the app's directory**:
```bash
cd web-to-pdf
```

## Usage

The "Web to PDF Converter" is used via the command line. Here's how to use it:

```bash
python app.py <URL> <output_filename>
```

## Command-Line Arguments

- `<URL>`: The URL of the webpage you want to convert to a PDF.

- `<output_filename>`: The name of the PDF file where the converted content will be saved.

## Examples

Here are some example usages:

```bash
python app.py 'https://example.com' 'example.pdf'
```

This command will convert the webpage at 'https://example.com' into a PDF file named 'example.pdf'.

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these guidelines:

- Fork the repository.

- Create a new branch for your feature or bug fix.

- Make your changes and test them.

- Submit a pull request with a clear description of your changes.
