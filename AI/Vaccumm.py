i=input('State where vacuum (A or B):').lower()
a=input('Enter initial condition of Room A:').lower()
b=input('Enter initial condition of Room B:').lower()
c=0
if i=='a':
    if a=='dirty':
        print('Suck')
        print('Move to right')
        c+=1
        if b=='dirty':
            print('Suck')
            c+=1
        elif b=='clean':
            print('No cleaning')
    elif a=='clean':
        print('No cleaning')
        print('Move to right')
        if b=='dirty':
            print('Suck')
            c+=1
        elif b=='clean':
            print('No cleaning')
elif i=='b':
    if b=='dirty':
        print('Suck')
        print('Move to left')
        c+=1
        if a=='dirty':
            print('Suck')
            c+=1
        elif a=='clean':
            print('No cleaning')
    elif b=='clean':
        print('No cleaning')
        print('Move to left')
        if a=='dirty':
            print('Suck')
            c+=1
        elif a=='clean':
            print('No cleaning ')
print('All states are cleaned')
print(f'Path cost is: {c}')