import random
right = False

user_num = int(input("Please enter a number ranging from 1 to 100:"))

ran_num = random.randint(0,100)

while right == False:
  if user_num != ran_num:
    print('Whoops wrong guess.')
    user_num = int(input("Please enter a number ranging from 1 to 100:"))
    right = False
  else:
    print('Wow that right!')
    print('Congratulation')
    right = True
