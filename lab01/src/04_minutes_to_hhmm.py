m= int(input('целые минуты '))
h=(m%(24*60))//60
m=m%60
print(f'{h}:{m}')