import re
import argparse

parser = argparse.ArgumentParser()

def parse_args():
    parser.add_argument("-f", "--file", help="path to text file")
    return parser.parse_args()

def remove_punctuation(word):
    salutation = re.match('((Mr|Mrs|Ms|Dr|Sr|[A-Z])\.|\w\.\w\.)', word)
    str_with_hyp = re.match('\w+(?:-\w+)+', word)
    str_with_amp = re.match('\w+(?:&\w+)+', word)
    str_with_single_quote = re.match('\w+\'[a-z]', word)

    if salutation is not None:
        return word
    elif str_with_hyp is not None:
        return word
    elif str_with_amp is not None:
        return word
    elif str_with_single_quote is not None:
        return word
    else:
        return (re.sub('[^A-Za-z0-9]+', '', word))

def find_words(word, sentences):
    line_numbers = []
    for i in range(len(sentences)):
        if word in sentences[i]:
            line_numbers.append(i+1)
    return line_numbers

def main():
    # data = input()
    args = parse_args()
    sentence_pattern = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\!|\?)\s')
    seen = {}
    sentences = []
    with open(args.file) as f:
        data = f.readlines()

    for sentence in re.split(sentence_pattern, str(data)):
        sentences.append(sentence)
        print("Sentence {} : {}".format(len(sentences),sentence))

    for word in re.split(r'\s', ' '.join(data)):
        stripped_word = remove_punctuation(word)
        if stripped_word not in seen:
            seen[stripped_word] = find_words(stripped_word, sentences)

    for key,value in seen.items():
        print("{}: {}".format(key, ','.join(str(i) for i in value) ))

if __name__ == '__main__':
    main()
