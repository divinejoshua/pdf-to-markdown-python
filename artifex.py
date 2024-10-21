import pymupdf4llm
md_text = pymupdf4llm.to_markdown("Aliko_Dangote.pdf")

import pathlib
pathlib.Path("output_artifex.md").write_bytes(md_text.encode())