import numpy as np

import tool
from Quiz2_1 import ngram_probs


def prob3(bigram, cnt2, cnt3):
  p2 = np.log10(cnt2[bigram])
  prob = {}
  for key in cnt3:
    p3 = np.log10(cnt3[key])
    for i in key:
      if i not in bigram:
        prob[i] = p3 - p2

  return prob


def main():
  cnt2, cnt3 = ngram_probs()
  prob = prob3(('we', 'are'), cnt2=cnt2, cnt3=cnt3)
  print(prob['family'])

if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    print(tool.exception_parser())
