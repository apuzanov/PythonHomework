def invert_quotation_mark(inp: str) -> str:
    return inp.translate({ord('"'): "'", ord("'"): '"'})
