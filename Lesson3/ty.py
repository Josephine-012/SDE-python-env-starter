family_gifts = ['Zephan', 'Mommy', 'Daddy', 'Joanne']
friend_gifts = ['Rylie', 'Nyla', 'Parker', 'Hanna']


def thank_you(name):
  print("thank you " + name)

def print_thank_you_card(list):
  for item in list:
    thank_you(item)
