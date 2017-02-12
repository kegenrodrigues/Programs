# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#
def convert_seconds(n):
    seconds=0
    minutes=0
    hours=0
    i=1
    while i<=n:
        seconds+=1
        if i%60==0:
            seconds=0
            minutes=minutes+1
        if i%3600==0:
            seconds=0
            minutes=0
            hours=hours+1
        
        i+=1
    seconds=seconds+(n%10)-(int(n)%10)     
    if hours==1:
        hours=str(hours)+' hour'
    else:
        hours=str(hours)+' hours'
    if minutes==1:
        minutes=', '+str(minutes)+' minute'
    else:
        minutes=', '+str(minutes)+' minutes'
    if seconds==1:
        seconds=', '+str(seconds)+' second'
    else:
        seconds=', '+str(seconds)+' seconds'
    time=[hours,minutes,seconds]
    string=''
    for e in time:
        string=string+e
    return string


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second
print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds
print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds
