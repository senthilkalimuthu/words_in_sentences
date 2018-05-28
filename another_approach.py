import argparse

parser = argparse.ArgumentParser()

def parse_args():
    parser.add_argument("-f", "--file", help="path to text file")
    return parser.parse_args()


def main():
    # data = input()
    args = parse_args()
    sentence_terminators = ('.', '!', '?')
    with open(args.file) as f:
        data = f.readlines()

    abbreviations = ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Sr.', 'i.e.', 'e.g.']  # etc.,

    visited_words = {}
    sentence_number = 1

    for word in data.split(' '):
            if word in visited_words.keys():
                if sentence_number not in visited_words[word]:
                    visited_words[word].append(sentence_number)
            else:
                visited_words[word] = [sentence_number]

            if word.endswith(sentence_terminators) and word not in abbreviations:
                sentence_number += 1


    for word, sentence_number in visited_words.items():
        print("{}: {}".format(word, ','.join(str(i) for i in sentence_number) ))

if __name__ == '__main__':
    main()
