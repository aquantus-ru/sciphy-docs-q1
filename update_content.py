import glob
import re
import os

def extract_dictionary(input_files):
    dictionary_entries = []

    for filepath in input_files:
        print(f"Scanning {filepath} for dictionary terms...")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

            # Find the "Dictionary of Terms" section
            match = re.search(r'## Dictionary of Terms\n+(.*)', content, re.DOTALL)
            if match:
                section_content = match.group(1)
                # Parse list items: * **Term:** Definition
                # Regex looks for lines starting with * or - followed by bolded term
                items = re.findall(r'[\*\-]\s+\*\*(.*?)\*\*:?\s+(.*)', section_content)
                for term, definition in items:
                    dictionary_entries.append(f"{term}: {definition.strip()}")
            else:
                print(f"Warning: No dictionary found in {filepath}")

    # Sort alphabetically by term
    return sorted(dictionary_entries, key=lambda x: x.split(':')[0].lower())

def extract_laws(input_files):
    laws_entries = []

    for filepath in input_files:
        print(f"Scanning {filepath} for laws...")
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            for i, line in enumerate(lines):
                # Heuristic: Look for headers or bold text containing "Law"
                # Markdown headers ### 1. Newton's First Law (Inertia)
                # Markdown bold **Newton's Second Law**

                # Check headers
                header_match = re.match(r'#+\s+.*(Law|Principle|Theorem).*', line)
                if header_match:
                    law_name = header_match.group(0).lstrip('#').strip()
                    # Try to capture the definition in the following lines
                    definition = []
                    for j in range(i+1, min(i+10, len(lines))):
                        next_line = lines[j].strip()
                        if next_line.startswith('#'): # Stop at next header
                            break
                        if next_line:
                            definition.append(next_line)

                    if definition:
                        # Clean up definition (remove latex markers if possible, though strict conversion is hard here)
                        # Just take the first substantial paragraph
                        full_def = " ".join(definition)
                        laws_entries.append(f"{law_name}\n{full_def}\n")

    return laws_entries

def generate_index(input_files):
    index_entries = ["Table of Contents"]
    for filepath in sorted(input_files, key=lambda x: int(re.search(r'chapter-(\d+)', x).group(1))):
         with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            # Remove markdown header markers
            title = first_line.lstrip('#').strip()
            index_entries.append(title)
    return index_entries

def generate_theory_summary(input_files):
    summaries = []
    for filepath in sorted(input_files, key=lambda x: int(re.search(r'chapter-(\d+)', x).group(1))):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')

            # Title
            title = lines[0].lstrip('#').strip()
            summaries.append(f"THEORY OF {title.upper()}\n")

            # Extract text until the first subsection or a reasonable limit
            # We want "inner workings... rather than equations"
            # Strategy: Grab text paragraphs, ignore lines with $$ or latex math, ignore explicit "Example" sections

            current_text = []
            for line in lines[1:]:
                stripped = line.strip()
                if stripped.startswith('## Dictionary') or stripped.startswith('Dictionary of Terms'):
                    break

                # Skip headers for now, just flatten the prose?
                # Or maybe keep h2/h3 as text structure
                if stripped.startswith('#'):
                    # It's a header
                     current_text.append(f"\n{stripped.lstrip('#').strip()}:")
                     continue

                # Skip math blocks
                if '$$' in line:
                    continue
                if line.strip() == '':
                    continue

                # If it looks like a list item for a formula, maybe skip?
                # But keep bullet points of concepts

                current_text.append(stripped)

            # Join and clean up
            text_block = "\n".join(current_text)
            summaries.append(text_block)
            summaries.append("\n" + "="*30 + "\n")

    return "\n".join(summaries)


def main():
    # Use MD files for source of laws and dictionary as they have structure
    md_files = glob.glob('chapter-*.md')
    md_files.sort(key=lambda x: int(re.search(r'chapter-(\d+)', x).group(1)))

    # Generate Dictionary
    dictionary = extract_dictionary(md_files)
    with open('dictionary.txt', 'w', encoding='utf-8') as f:
        f.write("PHYSICS DICTIONARY\n\n")
        for entry in dictionary:
            f.write(entry + "\n\n")

    # Generate Laws
    laws = extract_laws(md_files)
    with open('laws.txt', 'w', encoding='utf-8') as f:
        f.write("FUNDAMENTAL PHYSICS LAWS\n\n")
        for law in laws:
             f.write(law + "\n" + "-"*20 + "\n")

    # Generate Index (TOC)
    index = generate_index(md_files)
    with open('index.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(index) + "\n\n" + "-"*40 + "\n\n")

    # Generate Physics Theory Audiobook
    # Ideally, we should use the .txt files for the content if they are cleaner for "audiobook" purposes (no latex)
    # But .md files have structure that helps us skip "Equations".
    # Let's stick to .txt files for the main text content to avoid Latex parsing issues,
    # BUT the user wants "theory... rather than equations".
    # The .txt files already have equations converted to ASCII (e.g. "sqrt(L/g)").
    # Maybe I can just read the .txt files and try to heuristically remove lines that look like math?
    # Or just use the .txt content as is, since "theory of how... work" might essentially be the text of the book without the specific worked examples?
    # Let's try to extract from .txt files, filtering out obvious math-heavy lines if possible, or just providing the text.
    # The prompt says: "covers theory of how chapters 1-15 work... rather than equations".
    # This implies a higher level summary.
    # Since I cannot write new content, I will aggregate the text portions of the chapters.

    txt_files = glob.glob('chapter-*.txt')
    txt_files.sort(key=lambda x: int(re.search(r'chapter-(\d+)', x).group(1)))

    theory_content = []
    for filepath in txt_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            chapter_title = lines[0].strip()
            theory_content.append(f"\n{chapter_title} - THEORETICAL OVERVIEW\n")

            for line in lines[1:]:
                # Filter out lines that look like pure math or short formulas
                # Heuristic: if line contains '=' or math symbols and is short
                if len(line.strip()) < 50 and ('=' in line or '*' in line):
                    continue
                # Filter out "Example:" lines?
                if "Example:" in line:
                    continue

                theory_content.append(line)
            theory_content.append("\n" + "="*30 + "\n")

    with open('physics_theory_audiobook.txt', 'w', encoding='utf-8') as f:
        f.write("PHYSICS THEORY AUDIOBOOK: CONCEPTS AND MECHANISMS\n\n")
        f.write("".join(theory_content))


    # Re-assemble audiobook.txt
    # Order: Index, Chapters, Laws, Dictionary

    # Read existing audiobook content (or regenerate from chapters to be safe/clean)
    # We should regenerate to include the index at the start.

    with open('audiobook.txt', 'w', encoding='utf-8') as outfile:
        # 1. Index
        with open('index.txt', 'r', encoding='utf-8') as f:
            outfile.write(f.read())

        # 2. Chapters (from txt files)
        for filepath in txt_files:
             with open(filepath, 'r', encoding='utf-8') as f:
                outfile.write(f.read())
                outfile.write('\n\n' + '-'*40 + '\n\n')

        # 3. Laws
        outfile.write("\n\nAPPENDIX A: LAWS OF PHYSICS\n\n")
        with open('laws.txt', 'r', encoding='utf-8') as f:
            outfile.write(f.read())

        # 4. Dictionary
        outfile.write("\n\nAPPENDIX B: DICTIONARY OF TERMS\n\n")
        with open('dictionary.txt', 'r', encoding='utf-8') as f:
            outfile.write(f.read())

    print("Files generated: dictionary.txt, laws.txt, index.txt, physics_theory_audiobook.txt, audiobook.txt")

if __name__ == "__main__":
    main()
