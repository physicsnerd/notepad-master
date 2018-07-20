in_string = 'remindme 3d24h5m'
words = in_string.split()
print(words)
if len(words) != 2:
    print('problem')
else:
    ref = words[1]
    if 'd' in ref:
        days = ref[:ref.index('d')]
        print(days)
    if 'h' in ref:
        hours = ref[:ref.index('h')]
        print(hours)
    if 'm' in ref:
        minutes = ref[:ref.index('m')]
        print(minutes)
    #deal with time stuff
