import tool


def ngram_probs(filename='./raw_sentences.txt'):
  bigram_probs = {}
  trigram_probs = {}

  with open(filename, 'r')as f:
    lines = f.readlines()
    print(len(lines))
    print('\n')
    bicount = 0
    tricount = 0

    for i, line in enumerate(lines):
      print(i, end='\r')
      line = line.lower()
      line = line.split(' ')

      for i in range(len(line) - 1):
        bigraph = (line[i], line[i + 1])
        if bigraph not in bigram_probs:
          bigram_probs[bigraph] = 1
        else:
          bigram_probs[bigraph] += 1
        bicount += 1

      for i in range(len(line) - 2):
        trigraph = (line[i], line[i + 1], line[i + 2])
        if trigraph not in trigram_probs:
          trigram_probs[trigraph] = 1
        else:
          trigram_probs[trigraph] += 1
        tricount += 1

    for k in bigram_probs:
      bigram_probs[k] /= (bicount + 1e-5)
    for k in trigram_probs:
      trigram_probs[k] /= (tricount + 1e-5)

  return bigram_probs, trigram_probs


def main():
  cnt2, cnt3 = ngram_probs()
  print(cnt2[('we', 'are')])

if __name__ == '__main__':
  try:
    main()
  except Exception as e:
    print(tool.exception_parser())
