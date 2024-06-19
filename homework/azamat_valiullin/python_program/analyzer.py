import argparse
import os


def search_in_file(file_path, search_text):
    results = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            if search_text in line:
                snippet = extract_snippet(line, search_text)
                results.append((file_path, line_number, snippet))
    return results


def extract_snippet(line, search_text, word_count=5):
    words = line.split()
    if search_text not in words:
        return line.strip()
    index = words.index(search_text)
    start = max(index - word_count, 0)
    end = index + word_count + 1
    snippet = ' '.join(words[start:end])
    return snippet


def search_in_directory(directory, search_text):
    results = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.log'):
                file_path = os.path.join(root, file)
                results.extend(search_in_file(file_path, search_text))
    return results


def main():
    parser = argparse.ArgumentParser(description="Log file analyzer.")
    parser.add_argument('log_dir', help='The full path to the folder where the log files are located')
    parser.add_argument('--text', required=True, help='The text to find in the files')
    parser.add_argument('--first', action='store_true', help='Display only the first found line')

    args = parser.parse_args()

    log_dir = args.log_dir
    search_text = args.text
    display_first = args.first

    if not os.path.isdir(log_dir):
        print(f"Error: {log_dir} is not a valid directory.")
        return

    results = search_in_directory(log_dir, search_text)
    if display_first and results:
        results = [results[0]]

    for file_path, line_number, snippet in results:
        print(f"File: {file_path}, Line: {line_number}, Snippet: {snippet}")


if __name__ == "__main__":
    main()

# Commands for running the program
"""
python homework\\azamat_valiullin\\python_program\\analyzer.py C:\\Users\\User\\workspace_python\\Azamat_V\\homework
\\eugene_okulik\\data\\logs --text WARN --first
python homework\\azamat_valiullin\\python_program\\analyzer.py C:\\Users\\User\\workspace_python\\Azamat_V\\homework
\\eugene_okulik\\data\\logs --text WARN
python homework\\azamat_valiullin\\python_program\\analyzer.py C:\\Users\\User\\workspace_python\\Azamat_V\\homework
\\eugene_okulik\\data\\logs --text ERROR --first
python homework\\azamat_valiullin\\python_program\\analyzer.py C:\\Users\\User\\workspace_python\\Azamat_V\\homework
\\eugene_okulik\\data\\logs --text ERROR
"""
