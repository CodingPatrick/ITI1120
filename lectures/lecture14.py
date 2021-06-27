import random

def raw_read_answer():
    ans = 0
    try:
        ans = int(input('Give me an integer in range (1,2,3,4): '))
    except:
        print('Your answer must be an integer')
    return ans

def read_answer():
    ans = raw_read_answer()
    while ans not in [1,2,3,4]:
        print('Answer out of range')
        ans = raw_read_answer()
    return ans

def ask_question(q):
    print(q[0])
    for i in range(1,5):
        print(i, q[p[i-1]])

# main
lines = open('quiz.csv', encoding='utf-8').read().splitlines()

questions = []
for items in lines:
    questions.append(item.split('\t'))

score = 0
lives = 5
while lives > 0 and len(questions) >= 1:
    q = random.choice(questions)
    questions.remove(q)

    p = [1,2,3,4]
    random.shuffle(p)
    
    ask_question(q)
    ans = read_answer()
    
    if p[ans-1] == 1:
        score = score + int(q[-1])
    else:
        print('The correct answer was:', q[1])
        lives = lives - 1
    print('Your score is', score, '# of lives is', lives)
