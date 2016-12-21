import sys
import time
from histogram import get_words_list
from histogram import create_histogram

def performance(file_name):
    t0 = time.time()
    hundred_list = get_words_list(file_name, 100)
    hundred_hgram = create_histogram(hundred_list)
    t1 = time.time()
    t100 = t1-t0
    print t100

    t2 = time.time()
    ten_thousand_list = get_words_list(file_name, 100000)
    ten_thousand_hgram = create_histogram(ten_thousand_list)
    t3 = time.time()
    t10000 = t3-t2
    print t10000

if __name__ == '__main__':
    file_name = str(sys.argv[1])
    performance(file_name)
