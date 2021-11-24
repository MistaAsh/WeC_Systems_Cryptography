square = ['ABCDE', 'FGHIK', 'LMNOP', 'QRSTU', 'VWXYZ']

msg = 'STBASHTWOUPSRGBURYNISPBTAEILQSYDSIUBBZOYNSAFPQABTUYMSIPTQCOCILQSKSOCUBEBOCOHPCUDCPCLEAAFPQABUCPAZASC'
n = len(msg)

coord = {}
for i in range(5):
    for j in range(5):
        coord[square[i][j]] = [i, j]

ans = ''

i = 0
while i < n:
    r1 = coord[msg[i]][0]
    c1 = coord[msg[i]][1]

    r2 = coord[msg[i+1]][0]
    c2 = coord[msg[i+1]][1]

    if r1 == r2:
        ans += square[r1][(c1 + 4) % 5]
        ans += square[r2][(c2 + 4) % 5]

    elif c1 == c2:
        ans += square[(r1 + 4) % 5][c1]
        ans += square[(r2 + 4) % 5][c2]

    else:
        ans += square[r1][c2]
        ans += square[r2][c1]

    i += 2

print(ans)