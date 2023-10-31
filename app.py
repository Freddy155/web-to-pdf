import pdfkit
import argparse

options = {
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'encoding': 'UTF-8',
}

def convert_webpage_to_pdf(url, output_filename):
    try:
        pdfkit.from_url(url, output_filename, options=options)
        print(f'PDF saved as {output_filename}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def main():
    parser = argparse.ArgumentParser(description='Webpage to PDF Converter')
    parser.add_argument('url', help='URL of the webpage to convert')
    parser.add_argument('output', help='Output PDF filename')
    args = parser.parse_args()

    convert_webpage_to_pdf(args.url, args.output)

if __name__ == "__main__":
    main()
