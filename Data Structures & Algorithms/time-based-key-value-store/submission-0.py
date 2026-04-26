class TimeMap:

    def __init__(self):
        self.map: dict[str, dict[int, str]] = {}
        self.cache_last_timestamps: dict[str, int] = {}  # Cache for last timestamp that was set

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key][timestamp] = value        
        else:
            self.map[key] = {timestamp: value}
        
        self.cache_last_timestamps[key] = timestamp


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        key_dict= self.map[key]  # Get dict of {timestamp: value} pairs for this key
        if timestamp in key_dict:  # Fast lookup O(1) in dict for exact timestamp key if exists
            return key_dict[timestamp]

        last_ts_set = self.cache_last_timestamps[key]
        if last_ts_set <= timestamp: # Valid since "All the timestamps are increasing" per description
            return self.map[key][last_ts_set]

        # Case where the timestamp does not match a key. Have to search for closest
        timestamps = list(self.map.get(key, {}).keys())
        ordered_timestamps = sorted(timestamps)  # Could use OrderedDict() but prefered a portable solution
        
        if timestamp < ordered_timestamps[0]:  # Smallest timestamp > queried timestamp
            return ""

        # Binary search for the largest timestamp which is <= than queried timestamp
        left, right = 0, len(ordered_timestamps) - 1
        while left<=right:
            mid = (left + right) // 2
            if ordered_timestamps[mid] <= timestamp:
                left = mid + 1
                val = self.map[key][ordered_timestamps[mid]]
            else:
                right = mid - 1

        return val
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)