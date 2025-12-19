import os
import re

def sort_key(filename):
    # Extract the number from 'chapter-N.txt'
    match = re.search(r'chapter-(\d+)\.txt', filename)
    if match:
        return int(match.group(1))
    return 0

def process_text(text):
    # Pre-processing
    text = text.replace('—', ' -- ')

    # Regex Replacements

    # 1. Handle Paired Magnitude |...|
    # This regex looks for | followed by non-| characters, followed by |.
    # We replace it with "the magnitude of [content]"
    # We run this loop until no more changes to handle potentially nested ones (though simple regex doesn't do nesting well,
    # the physics text seems simple: |v| or |Psi|).
    # NOTE: Special care for spacing.

    # Simple replacement for |X| -> magnitude of X
    text = re.sub(r'\|([^|]+)\|', r' the magnitude of \1 ', text)

    # If any stray | remain (unpaired or complex), map them to ' vertical bar ' just in case,
    # but based on grep they seem paired.
    text = text.replace('|', ' vertical bar ')

    replacements = [
        (r'\+/-', ' plus or minus '),
        (r'\^', ' to the power of '),
        (r'\*', ' times '),
        (r'/', ' divided by '),
        (r'=', ' equals '),
        (r'<', ' is less than '),
        (r'>', ' is greater than '),
        (r'~', ' approximately '),
        (r'%', ' percent '),
        (r'&', ' and '),
        (r'\+', ' plus '),
        (r'_', ' subscript '),
        (r'\[', ' open bracket '),
        (r'\]', ' close bracket '),
        (r'\(', ' open parenthesis '),
        (r'\)', ' close parenthesis '),
    ]

    for pattern, replacement in replacements:
        text = re.sub(pattern, replacement, text)

    return text

def main():
    files = [f for f in os.listdir('.') if f.startswith('chapter-') and f.endswith('.txt')]
    files.sort(key=sort_key)

    output_content = []

    for filename in files:
        chapter_num = sort_key(filename)
        print(f"Processing {filename}...")

        with open(filename, 'r') as f:
            content = f.read()

        # Process the content
        processed_content = process_text(content)

        # Build the chapter block
        chapter_block = f"Start of Chapter {chapter_num}\n\n"
        chapter_block += processed_content
        chapter_block += f"\n\nEnd of Chapter {chapter_num}\n\n"

        output_content.append(chapter_block)

    with open('audiobook.txt', 'w') as f:
        f.write("".join(output_content))

    print("audiobook.txt created successfully.")

if __name__ == '__main__':
    main()
