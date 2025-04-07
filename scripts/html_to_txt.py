from bs4 import BeautifulSoup

def html_to_text(input_html_path, output_txt_path):
    # Read the HTML file
    with open(input_html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse HTML and extract text
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)

    # Write to a text file
    with open(output_txt_path, 'w', encoding='utf-8') as out_file:
        out_file.write(text)

    print(f"Text extracted and saved to {output_txt_path}")

# Example usage
if __name__ == "__main__":
    html_file = 'html_cache/latest_chalmers_page.html'      # Change this to your local HTML file
    output_file = 'html_cache/latest_chalmers_page.txt'      # Desired output file
    html_to_text(html_file, output_file)
