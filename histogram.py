import time
import sys

def create_file(name, histogram):
    f = open(name, 'w')
    for word in histogram:
        f.write(str(word) + ' ' + str(histogram[word]) + '\n')
    f.close()
    return f

def get_frequency(word, histogram):
    frequency = histogram[word]
    return frequency

def get_unique_words(histogram):
    unique_words = {}
    for word in histogram:
        if histogram[word] == 1:
            unique_words[word] = histogram[word]
    return len(unique_words)

def create_histogram(words_list):
    histogram = {}
    for word in words_list:
        if word in histogram:
            count = histogram[word]
            histogram[word] = count + 1
        else:
            histogram[word] = 1
    return histogram

def remove_punctuation(word_string):
    punctuations = '!()-[]{};:"\,<>./?@#$%^&*_~\x80\x98\x99\x94'
    no_punctuation = ''
    for character in word_string:
        if character not in punctuations:
            no_punctuation += character
    return no_punctuation

def get_words_list(file_name, number_of_words):
  f= open(file_name)
  lines = f.readlines()
  word_string = ' '.join(lines)
  no_punctuation = remove_punctuation(word_string)
  words_list = no_punctuation.split()

  #the benchmark list is created with this loop
  benchmark_list = []
  for index in range(0, number_of_words):
      benchmark_list.append(words_list[index])
  return benchmark_list

def my_app():
    words_list = get_words_list('tf.txt')
    histogram = create_histogram(words_list)
    unique_words = get_unique_words(histogram)
    frequency = get_frequency('to', histogram)
    text_file = create_file('histogram.txt', histogram)




if __name__ == '__main__':
    t0 = time.time()
    my_app()
    t1 = time.time()
    print(t1- t0)
