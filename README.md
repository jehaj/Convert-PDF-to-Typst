# Convert-PDF-to-Typst
Convert any PDF to Typst (perhaps through a local LLM such as Gemma).

It is very much in development.

How can it be done?

- `pdftotext`---sucks at handling formulas.
- [`typress`](https://github.com/ParaN3xus/typress)---however, it does not seem
  to be finished. Only supports formulas.
- [`Pix2Text`](https://github.com/breezedeus/Pix2Text)---converts to Markdown.
  - `pandoc` to convert to Typst.
  - a local LLM such as Gemma.
    - Can learn to use [`theorion`](https://typst.app/universe/package/theorion)
      and perhaps fix other formatting issues e.g. $$ \text{Byte}(...) \quad \text{instead of} \quad Byte(...) $$ 
      which occurs frequently in many math books and drives me crazy.
    - Perhaps fix grammar, but then the scope increases. I would also like for
      grammar fixing to be another pass entirely. We can also split this into
      normal grammar and formula grammar.
      - [`typst-languagetool`](https://github.com/antonWetzel/typst-languagetool)
        is also an option.

Pix2Text is killed when running on PDF with 162 pages (size 1.1MB) on my 16GB
RAM machine. I will try again running on chunks of pages i.e. chapters.

Requires PDF to be image-based. Convert text-based PDF to image-based PDF with
`magick`:
```shell
magick -density 150 input.pdf output.pdf
```

Or apparently not necessary, IDK. The documentation is not the greatest.

## Pix2Text

Using the English model has issues pertaining `font_path`. Adding

`"font_path": None,` to `.venv/lib/python3.12/site-packages/cnocr/ppocr/rapid_recognizer.py`
line 26 and forwards such that it becomes

```python
class Config(dict):
    DEFAULT_CFG = {
        "font_path": None,
        "engine_type": EngineType.ONNXRUNTIME,
```

fixes the issue. Mentioned at [Issue 364 at CnOCR](https://github.com/breezedeus/CnOCR/issues/364#issuecomment-3205088342).

Took 33 minutes and 17 seconds to run.
