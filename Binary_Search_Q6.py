

def minMaxDelta(delta, t):
    n = len(delta)
    prev = []
    cur = [0]
    for tt in range(t + 1):
        prev.append(delta[0] / (tt + 1))
    for nn in range(1, n):
        cur.append(delta[nn])
        for tt in range(1, tt + 1):
            l = 0
            r = tt - 1
            while l < r - 1:
                m = l + int((r - l) / 2)
                i = int(delta[nn] / (t - m + 1))
                if 
