import sys
from histogram import get_words_list
from histogram import create_histogram

def benchmark(file_name):
    hundred_list = get_words_list(file_name, 100)
    hundred_hgram = create_histogram(hundred_list)
    print hundred_hgram
    return hundred_hgram

if __name__ == '__main__':
    file_name = str(sys.argv[1])
    benchmark()
