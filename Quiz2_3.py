from Quiz2_1 import ngram_probs
from Quiz2_2 import prob3

import tool


def predict_max(starting, cnt2, cnt3):
  list_of_words = []
  prob = prob3(starting, cnt2=cnt2, cnt3=cnt3)


  return list_of_words


def main():
  cnt2, cnt3 = ngram_probs()
  sent = predict_max(('we', 'are'), cnt2=cnt2, cnt3=cnt3)
  assert sent[-1] == '.' or len(sent) <= 15
  print(' '.join(sent))

if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    print(tool.exception_parser())
