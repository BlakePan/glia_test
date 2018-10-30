from Quiz2_1 import ngram_probs
from Quiz2_2 import prob3

import tool


def predict_max(starting, cnt2, cnt3):
  list_of_words = []
  while True:
    prob = prob3(starting, cnt2=cnt2, cnt3=cnt3)
    max_prb = float('-inf')
    final_sent = '.'

    for k in sorted(cnt3):
      if starting == k[:2]:
        sent_cand = k[-1]
        # print(starting, sent_cand)

        if sent_cand in prob and prob[sent_cand] > max_prb:
          max_prb = prob[sent_cand]
          final_sent = sent_cand

    starting = (starting[1], final_sent)
    list_of_words.append(final_sent)
    # print(list_of_words)

    if final_sent == '.' or len(list_of_words) >= 15:
      break

  return list_of_words


def main():
  cnt2, cnt3 = ngram_probs()
  sent = predict_max(('we', 'are'), cnt2=cnt2, cnt3=cnt3)
  assert sent[-1] == '.' or len(sent) <= 15, '{}'.format(sent)
  print(' '.join(sent))

if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    print(tool.exception_parser())
