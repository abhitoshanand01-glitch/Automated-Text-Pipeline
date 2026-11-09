import os
from core_processor import parse_poetry_file

def generate_latex_book_page(metadata, poem_lines, output_folder="output_book"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    output_path = os.path.join(output_folder, "kavita_book_page.tex")
    
    # Title aur Author metadata se nikal rahe hain
    title = metadata.get("TITLE", "Kavita")
    author = metadata.get("AUTHOR", "Unknown")
    date = metadata.get("DATE", "\\today")
    
    # Kavita ki lines ko LaTeX format mein set karna (har line ke baad \\ lagana zaroori hai)
    formatted_poem = " \\\\\n".join(poem_lines)
    
    # Ye hamara master LaTeX template hai jo Hindi support karta hai
    latex_template = f"""\\documentclass[12pt, a4paper]{{article}}
\\usepackage{{fontspec}}
\\setmainfont{{Nirmala UI}} % Hindi support ke liye
\\usepackage[margin=1.5in]{{geometry}}
\\usepackage{{setspace}}

\\title{{\\Huge \\textbf{{{title}}}}}
\\author{{\\Large {author}}}
\\date{{\\textit{{{date}}}}}

\\begin{{document}}
\\maketitle
\\vspace{{1cm}}

\\begin{{center}}
\\Large
\\setstretch{{1.5}} % Lines ke beech gap badhane ke liye
{formatted_poem}
\\end{{center}}

\\end{{document}}
"""

    # Is template ko .tex file mein save kar rahe hain
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(latex_template)
        
    print(f"Success! LaTeX file yahan save ho gayi hai: {output_path}")
    print("Aap is file ka text Overleaf par paste karke PDF bana sakte hain!")

if __name__ == "__main__":
    target_file = 'poetry.txt'
    
    if os.path.exists(target_file):
        print("Kavita padh rahe hain...")
        meta, poem = parse_poetry_file(target_file)
        print("LaTeX Book Page bana rahe hain...")
        generate_latex_book_page(meta, poem)
    else:
        print("Error: poetry.txt nahi mili!")