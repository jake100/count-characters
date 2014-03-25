import string
import sys
import os
import math
import cProfile
class Word:
  def __init__(self):
    self.s = ""
    self.count = 1
  def __str__(self):
    return self.s + " " + str(self.count) + "\n"
class Words:
  textWords = []
  def checkWord(self, s):
    canAdd = True
    for i, word in enumerate(self.textWords):
      if s == self.textWords[i].s:
        canAdd = False
        self.textWords[i].count += 1
        break
    if canAdd:
      wordObj = Word()
      wordObj.s = s
      self.textWords += [wordObj]
  def getLines(self):
    lines = []
    for textWord in self.textWords:
      lines.extend(str(textWord))
    return lines
def main():
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  textFile = open(os.path.join(__location__, 'dictionary.txt'), "r")
  lines = textFile.readlines()
  textFile.close()
  wordObj = Words()
  for line in lines:
    for c in line:
      wordObj.checkWord(c)
  resultFile = open(os.path.join(__location__, 'letter count.txt'), "w")
  resultFile.writelines(wordObj.getLines())
  resultFile.close();
if __name__ == '__main__':
  cProfile.run('main()')
