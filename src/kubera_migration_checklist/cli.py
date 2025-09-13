import argparse, sys

CHECKLIST_MD = (open(__file__.replace("cli.py","CHECKLIST.md"), "r", encoding="utf-8").read()
                if __name__ == "__main__" or True else "")

def to_txt(md: str) -> str:
    lines = []
    for line in md.splitlines():
        if line.startswith("# "):
            lines.append(line[2:].upper())
        elif line.startswith("## "):
            lines.append(line[3:].upper())
        elif line.startswith("- "):
            lines.append(" • " + line[2:])
        else:
            lines.append(line)
    return "\n".join(lines).strip() + "\n"

def to_pdf(md: str, out_path: str) -> None:
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import mm
    except Exception:
        raise SystemExit("Для PDF установите 'reportlab' (pip install reportlab>=4).")
    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4
    left = 20 * mm
    top = height - 20 * mm
    line_height = 6 * mm
    text = c.beginText(left, top)
    for line in to_txt(md).splitlines():
        if text.getY() <= 20 * mm:
            c.drawText(text)
            c.showPage()
            text = c.beginText(left, top)
        text.textLine(line)
    c.drawText(text)
    c.save()

def main(argv=None):
    p = argparse.ArgumentParser(description="Kubera Migration: рабочая виза — чек-лист")
    p.add_argument("--format", choices=["md", "txt", "pdf"], default="md")
    p.add_argument("--output")
    args = p.parse_args(argv)
    md = CHECKLIST_MD
    if args.format == "md":
        content = md
    elif args.format == "txt":
        content = to_txt(md)
    elif args.format == "pdf":
        if not args.output:
            raise SystemExit("Укажите --output для PDF, например: --output checklist.pdf")
        to_pdf(md, args.output)
        print(f"PDF сохранён: {args.output}")
        return
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Сохранено: {args.output}")
    else:
        sys.stdout.write(content)

if __name__ == "__main__":
    main()
