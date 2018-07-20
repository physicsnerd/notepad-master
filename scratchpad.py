in_string = 'remindme 3d'
words = in_string.split()
days = 0
hours = 0
minutes = 0
def findOccurences(s, ch):
    return len([i for i, letter in enumerate(s) if letter == ch])
if len(words) != 2:
    print('problem')
elif findOccurences(words[1], 'd') > 1 or findOccurences(words[1], 'h') > 1 or findOccurences(words[1], 'm') > 1:
    print('problem')
#elif d is after h/index are screwed up => problem
else:
    ref = words[1]
    if 'd' in ref:
        days = ref[:ref.index('d')]
        print(days)
    if 'h' in ref:
        if 'd' in ref:
            hours = ref[ref.index('d')+1:ref.index('h')]
        else:
            hours = ref[:ref.index('h')]
        print(hours)
    if 'm' in ref:
        if 'h' in ref:
            minutes = ref[ref.index('h')+1:ref.index('m')]
        else:
            if 'd' in ref:
                minutes = ref[ref.index('d'):ref.index('m')]
            else:
                minutes = ref[:ref.index('m')]
        print(minutes)
#deal with time stuff        
        
