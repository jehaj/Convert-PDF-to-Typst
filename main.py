import contextlib
from pix2text import Pix2Text
import os


def main():
    pdf_folder_path = "test"
    from tqdm.auto import tqdm

    # p2t = initialize_pix2text()
    # doc = p2t.recognize_pdf(
    #     "/home/nikolaj/Desktop/An Introduction to Cryptography by Ivan Damgård.pdf"
    # )
    # doc.to_markdown("output_md/entire")

    # return

    for file in tqdm(os.listdir(pdf_folder_path), unit="Chapter"):
        if not file.endswith(".pdf"):
            continue
        pdf_file_path = os.path.join(pdf_folder_path, file)
        convert_pdf_to_md(file, pdf_file_path)


def convert_pdf_to_md(file, pdf_file_path):
    """
    Convert a PDF file to Markdown format using Pix2Text.

    :param file: The name of the PDF file.
    :param pdf_file_path: The full path to the PDF file.
    """

    f = open(os.devnull, "w")
    with contextlib.redirect_stdout(f):
        p2t = initialize_pix2text()
        doc = p2t.recognize_pdf(pdf_file_path)
        output_md_path = os.path.join("output_md", f"{os.path.splitext(file)[0]}.md")
        doc.to_markdown(output_md_path)


def initialize_pix2text():
    text_formula_config = dict(
        languages=("en",),
        # text=dict(
        #     rec_model_name="en_PP-OCRv3",
        #     rec_model_backend="onnx",
        #     cand_alphabet=None,  # NOTE: must add this line
        # ),
    )
    total_config = {
        "layout": {"scores_thresh": 0.45},
        "text_formula": text_formula_config,
    }
    p2t = Pix2Text.from_config(total_configs=total_config, enable_table=False)
    return p2t


if __name__ == "__main__":
    import time

    t_start = time.time()
    main()
    t_end = time.time()
    print("Total time:")
    minutes, seconds = divmod(t_end - t_start, 60)
    print(f"{int(minutes)} minutes and {int(seconds)} seconds")
