from pix2text import Pix2Text


def main():
    print("Hello from convert-pdf-to-typst!")
    model = Pix2Text()
    pdf_file_path = "test.pdf"
    doc = model.recognize_pdf(pdf_file_path)
    print(f"Finished recognizing {pdf_file_path}. Saving to output_md...")
    doc.to_markdown("output_md")


if __name__ == "__main__":
    main()
