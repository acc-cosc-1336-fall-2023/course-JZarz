import decisions

result = decisions.overtime(45)

if result == False:
    print('30 is not overtime')

if result:
    print('is overtime')
else:
    print('not overtime')
