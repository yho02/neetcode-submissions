class TimeMap:

    def __init__(self):
        self.timemap = {}
        self.time = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[(key,timestamp)] = value
        self.time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time[key]
        if not arr or timestamp < arr[0]:
            return ""
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + (r-l) // 2 
            if arr[mid] == timestamp:
                return self.timemap[(key,timestamp)]
            elif arr[mid] < timestamp:
                l = mid + 1
            elif timestamp < arr[mid]:
                r = mid - 1
        # print(arr)
        # print(l,mid,r)
        print(arr[mid])
        print(timestamp)
        if arr[mid] < timestamp:
            return self.timemap[(key, arr[mid])]
        else: 
            print('here')
            return self.timemap[(key, arr[mid-1])]

            
        
