#By Hossein Kamkar

from ntpath import join


question = input()

if '+' in question:
    question = question.replace('+','')
    
sortedQuestion = sorted(question)
question = ''.join(sortedQuestion)

i = 1
while i < len(question):
    question = question[:i] + '+' + question[i:]
    i += 2

print(question)