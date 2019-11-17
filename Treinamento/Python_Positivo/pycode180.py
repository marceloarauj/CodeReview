def interval_scheduling(stimes, ftimes):
    """Return largest set of mutually compatible activities.
 
    This will return a maximum-set subset of activities (numbered from 0 to n -
    1) that are mutually compatible. Two activities are mutually compatible if
    the start time of one activity is not less then the finish time of the other.
 
    stimes[i] is the start time of activity i.
    ftimes[i] is the finish time of activity i.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(stimes)))
    # sort according to finish times
    index.sort(key=lambda i: ftimes[i])
 
    maximal_set = set()
    prev_finish_time = 0
    for i in index:
        if stimes[i] >= prev_finish_time:
            maximal_set.add(i)
            prev_finish_time = ftimes[i]
 
    return maximal_set
 
 
n = int(input('Enter number of activities: '))
stimes = input('Enter the start time of the {} activities in order: '
              .format(n)).split()
stimes = [int(st) for st in stimes]
ftimes = input('Enter the finish times of the {} activities in order: '
               .format(n)).split()
ftimes = [int(ft) for ft in ftimes]
 
ans = interval_scheduling(stimes, ftimes)
print('A maximum-size subset of activities that are mutually compatible is', ans)