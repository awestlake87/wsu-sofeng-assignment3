#!/usr/bin/python3
# program that scans a file and counts the lines and words
# Andrew J Westlake k582r363

if __name__ == "__main__":
    file_name = input("Enter a file name: ")
    num_lines = 0
    num_words = 0
    num_chars = 0

    with open(file_name, 'r') as file:
        for line in file:
            num_lines += 1
            num_words += len(line.split())
            num_chars += len(line)


    print(
        "%s has %d lines %d words and %d chars" % (
            file_name, num_lines, num_words, num_chars
        )
    )
