class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:   
        if len(dislikes) == 0:
            return True
        lst = [None] * N
        lst[dislikes[0][0] - 1] = 1
        lst[dislikes[0][1] - 1] = 2
        ok = 1
        remaining = []
        while True:
            length = len(dislikes)
            for i in dislikes:
                if ok == 0:
                    if lst[i[0] - 1] is None:
                        if lst[i[1] - 1] is None:
                            remaining.append(i)

                        elif lst[i[1] - 1] == 1:
                            lst[i[0] - 1] = 2
                        else:
                            lst[i[0] - 1] = 1
                    elif lst[i[0] - 1] == 1:
                        if lst[i[1] - 1] is None:
                            lst[i[1] - 1] = 2
                        elif lst[i[1] - 1] == 1:
                            return False
                    else:
                        if lst[i[1] - 1] is None:
                            lst[i[1] - 1] = 1
                        elif lst[i[1] - 1] == 2:
                            return False
                else:
                    ok = 0
            if len(dislikes) == 0:
                break
            if length == len(remaining) and len(remaining) > 0:
                lst[remaining[0][0] - 1] = 1
                lst[remaining[0][1] - 1] = 2
                remaining.pop(0)
            dislikes = remaining
            remaining = []

        return True
