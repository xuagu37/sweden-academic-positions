import re
from pathlib import Path

def convert_md_headings_to_html(input_path: str, output_path: str, level: int = 2):
    """
    Converts Markdown headings (##, ###, etc.) to HTML <hN> tags in a Markdown file.

    Args:
        input_path (str): Path to the input .md file.
        output_path (str): Path to the output .md file.
        level (int): Minimum heading level to convert (default is 2).
    """
    input_path = Path(input_path)
    output_path = Path(output_path)

    text = input_path.read_text(encoding="utf-8")

    # Match headings like ## Heading or ### Heading
    pattern = re.compile(r"^(#{%d,}) (.+)$" % level, re.MULTILINE)

    def replacer(match):
        hashes, title = match.groups()
        heading_level = len(hashes)
        return f"<h{heading_level}>{title.strip()}</h{heading_level}>\n"

    converted = pattern.sub(replacer, text)

    output_path.write_text(converted, encoding="utf-8")
    print(f"✅ Converted headings from: {input_path.name} → {output_path.name}")

if __name__ == "__main__":
    # Example usage:
    convert_md_headings_to_html("html_cache/lund.md", "content/lund.md")
    convert_md_headings_to_html("html_cache/uppsala.md", "content/uppsala.md")
    convert_md_headings_to_html("html_cache/stockholm.md", "content/stockholm.md")
    convert_md_headings_to_html("html_cache/gothenburg.md", "content/gothenburg.md")
    convert_md_headings_to_html("html_cache/ki.md", "content/ki.md")
    convert_md_headings_to_html("html_cache/kth.md", "content/kth.md")
    convert_md_headings_to_html("html_cache/linkoping.md", "content/linkoping.md")
    convert_md_headings_to_html("html_cache/umea.md", "content/umea.md")
    convert_md_headings_to_html("html_cache/orebro.md", "content/orebro.md")
    convert_md_headings_to_html("html_cache/lulea.md", "content/lulea.md")
    convert_md_headings_to_html("html_cache/malmo.md", "content/malmo.md")
