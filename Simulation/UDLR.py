size = int(input())
direction = input().split()
move_types = ['R','D','L','U']
dx = [0,1,0,-1]
dy = [1,0,-1,0]

x,y = 1,1

for d in direction:
    '''
    if d == 'U': i = 3
    if d == 'R': i = 0
    if d == 'D': i = 1
    if d == 'L': i = 2
    '''
    for i in range(len(move_types)):
        if d == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > size or ny < 1 or ny > size:
        continue
    x = nx
    y = ny

print(x,y)

