import sys

def count_words(input_file):
    word_counts = {}
    try:
        with open(input_file, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower() 
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return word_counts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_script.py <filename>")
        sys.exit(1)

    input_file = sys.argv[1]
    num_of_words = count_words(input_file)
    for word, count in num_of_words.items():
        print(f"word: {word} and its count: [{count}]")
