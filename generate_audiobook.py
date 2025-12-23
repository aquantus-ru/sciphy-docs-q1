import glob
import re

def get_chapter_number(filename):
    match = re.search(r'chapter-(\d+)\.txt', filename)
    if match:
        return int(match.group(1))
    return 0

def generate_audiobook():
    files = glob.glob('chapter-*.txt')
    # Sort files by chapter number
    sorted_files = sorted(files, key=get_chapter_number)

    with open('audiobook.txt', 'w', encoding='utf-8') as outfile:
        for i, filename in enumerate(sorted_files):
            print(f"Processing {filename}...")
            with open(filename, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                # Add spacing between chapters, but not after the last one
                if i < len(sorted_files) - 1:
                    outfile.write('\n\n' + '-'*40 + '\n\n')

    print("audiobook.txt generated successfully.")

if __name__ == "__main__":
    generate_audiobook()
