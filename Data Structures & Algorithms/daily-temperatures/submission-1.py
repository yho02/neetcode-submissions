class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = 0
        res = []
        higher_found = False 
        for i in range(len(temperatures)):
            count = 0
            for next_day in range(i+1, len(temperatures)):
                if temperatures[i] >= temperatures[next_day]:
                    count+= 1
                elif temperatures[i] < temperatures[next_day]:
                    # print (temperatures[i], temperatures[next_day])
                    higher_found = True
                    count += 1
                    break
                higher_found = False
            print (temperatures[i], temperatures[next_day])
            print (count)
            if higher_found:
                res.append(count)
            else:
                res.append(0)
        return res