import numpy as np

def is_valid_cell(x, y, dist, len_mtx):
    if dist[y][x] == 0 and 0 <= x < len_mtx and 0 <= y < len_mtx: return True
    return False

def bfs(y_start, x_start, y_end, x_end, len_mtx=64):
    q = [(x_start, y_start)]
    dist = [[0]*len_mtx for _ in range(len_mtx)]
    dist[y_start][x_start] = 0

    while q:
        x_cur, y_cur = q.pop(0)

        if x_cur == x_end and y_cur == y_end:
            return dist[y_cur][x_cur]

        for i in ([(x_cur+1, y_cur), (x_cur-1, y_cur), (x_cur, y_cur+1), (x_cur, y_cur-1)]):
            x, y = i
            if is_valid_cell(x, y, dist, len_mtx):
                q.append((x, y))
                dist[y][x] = dist[y_cur][x_cur] + 1
    return -1

def find_al_vertex(img):
    r = []
    for mtx in img:
        res = np.array([np.array([0]*64) for _ in range(64)])
        for i in range(len((mtx))):
            for j in range(len(mtx[0])):
                if 1 <= i <= 62 and 1 <= j <= 62:
                    if all([
                        mtx[i][j] >= mtx[i+1][j],
                        mtx[i][j] >= mtx[i][j+1],
                        mtx[i][j] >= mtx[i-1][j],
                        mtx[i][j] >= mtx[i][j-1],
                        mtx[i][j] >= mtx[i+1][j+1],
                        mtx[i][j] >= mtx[i-1][j+1],
                        mtx[i][j] >= mtx[i-1][j-1],
                        mtx[i][j] >= mtx[i+1][j-1],
                            ]):
                        res[i][j] = mtx[i][j]
                elif i == 0 and j == 0:
                    if all([
                        mtx[i][j] >= mtx[i+1][j],
                        mtx[i][j] >= mtx[i][j+1]
                            ]):
                        res[i][j] = mtx[i][j]
                elif i == 0 and j == 63:
                    if all([
                        mtx[i][j] >= mtx[i+1][j],
                        mtx[i][j] >= mtx[i][j-1]
                            ]):
                        res[i][j] = mtx[i][j]
                elif i == 63 and j == 63:
                    if all([
                        mtx[i][j] >= mtx[i-1][j],
                        mtx[i][j] >= mtx[i][j-1]
                            ]):
                        res[i][j] = mtx[i][j]
                elif i == 63 and j == 0:
                    if all([
                        mtx[i][j] >= mtx[i-1][j],
                        mtx[i][j] >= mtx[i][j+1]
                            ]):
                        res[i][j] = mtx[i][j]
                elif i == 0 and 1 <= j <= 62:
                    if all([
                        mtx[i][j] >= mtx[i+1][j],
                        mtx[i][j] >= mtx[i][j+1],
                        mtx[i][j] >= mtx[i][j-1],
                            ]):
                        res[i][j] = mtx[i][j]
                elif 1 <= i <= 62 and j == 63:
                    if all([
                        mtx[i][j] >= mtx[i+1][j],
                        mtx[i][j] >= mtx[i-1][j],
                        mtx[i][j] >= mtx[i][j-1],
                            ]):
                        res[i][j] = mtx[i][j]
                elif i == 63 and 1 <= j <= 62:
                    if all([
                        mtx[i][j] >= mtx[i-11][j],
                        mtx[i][j] >= mtx[i][j+1],
                        mtx[i][j] >= mtx[i][j-1],
                            ]):
                        res[i][j] = mtx[i][j]
                elif 1 <= i <= 62 and j == 0:
                    if all([
                        mtx[i][j] >= mtx[i+1][j],
                        mtx[i][j] >= mtx[i-1][j],
                        mtx[i][j] >= mtx[i][j+1],
                            ]):
                        res[i][j] = mtx[i][j]
        r.append(res)
    return np.array(r)