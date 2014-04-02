import string
import sys
import os
import math
import cProfile
import re
class Words:
  textWords = []
  wordCount = []
  def checkWord(self, s):
    for i in range(len(self.textWords)):
      if s == self.textWords[i]:
        self.wordCount[i] += 1
        return
    self.textWords.append(s)
    self.wordCount.append(1)
    self.reorder()
  def getText(self):
    lines = []
    self.reorder()
    for i in range(len(self.textWords)):
      new_text = "%s %s\n" % (self.textWords[i], str(self.wordCount[i]))
      lines.append(new_text)
    return lines
  def reorder(self):
    self.wordCount, self.textWords = (list(x) for x in zip(*sorted(zip(self.wordCount, self.textWords), key=lambda pair: pair[0], reverse = True)))
def main():
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  textFile = open(os.path.join(__location__, 'words.txt'), "r")
  text = textFile.read()
  textFile.close()
  text = re.sub('[\t]', ' ', text)
  text = re.sub('[\n]', ' ', text)
  text = re.sub('[\W_]+', ' ', text)
  text = re.split(' ', text)
  wordObj = Words()
  for word in text:
    wordObj.checkWord(word)
  for i in range(len(wordObj.textWords)):
    print("%s %s\n" % (wordObj.textWords[i], str(wordObj.wordCount[i])))
if __name__ == '__main__': 
  cProfile.run('main()')
