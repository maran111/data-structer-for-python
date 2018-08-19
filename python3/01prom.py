

while 1: try:
        m, n = list(map(int, input().split(',')))
        mtx = [] for i in range(m):
            mtx.append(list(map(int, input().split(',')))) except: break    def isValid(x, y): # print(x,y)  return x >= 0 and x < m and y >= 0 and y < n

    team_count = 0  max_count = 0  seen = set() for i in range(m): for j in range(n): if mtx[i][j] == 0 or (i, j) in seen: continue  else:
                count = 1  q = [(i, j)]
                seen.add((i, j)) while q:
                    x, y = q.pop() if isValid(x - 1, y) and mtx[x - 1][y] == 1 and (x - 1, y) not in seen:
                        q.append((x - 1, y))
                        seen.add((x - 1, y))
                        count += 1  if isValid(x + 1, y) and mtx[x + 1][y] == 1 and (x + 1, y) not in seen:
                        q.append((x + 1, y))
                        seen.add((x + 1, y))
                        count += 1  if isValid(x, y - 1) and mtx[x][y - 1] == 1 and (x, y - 1) not in seen:
                        q.append((x, y - 1))
                        seen.add((x, y - 1))
                        count += 1  if isValid(x, y + 1) and mtx[x][y + 1] == 1 and (x, y + 1) not in seen:
                        q.append((x, y + 1))
                        seen.add((x, y + 1))
                        count += 1  if isValid(x - 1, y - 1) and mtx[x - 1][y - 1] == 1 and (x - 1, y - 1) not in seen:
                        q.append((x - 1, y - 1))
                        seen.add((x - 1, y - 1))
                        count += 1  if isValid(x - 1, y + 1) and mtx[x - 1][y + 1] == 1 and (x - 1, y + 1) not in seen:
                        q.append((x - 1, y + 1))
                        seen.add((x - 1, y + 1))
                        count += 1  if isValid(x + 1, y - 1) and mtx[x + 1][y - 1] == 1 and (x + 1, y - 1) not in seen:
                        q.append((x + 1, y - 1))
                        seen.add((x + 1, y - 1))
                        count += 1  if isValid(x + 1, y + 1) and mtx[x + 1][y + 1] == 1 and (x + 1, y + 1) not in seen:
                        q.append((x + 1, y + 1))
                        seen.add((x + 1, y + 1))
                        count += 1  if count > max_count:
                    max_count = count
                team_count += 1  print(str(team_count) + ',' + str(max_count))
