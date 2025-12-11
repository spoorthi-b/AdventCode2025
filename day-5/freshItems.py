class Solution:

    def parseItemsInput(self, inputFile):
        items = []
        with open(inputFile, 'r') as file:
            for line in file:
                items.append(int(line.strip()))
        return items
    
    def parseRangeInput(self, inputFile):
        ranges = []
        with open(inputFile, 'r') as file:
            for line in file:
                line = line.strip()
                start, end = map(int, line.split("-"))
                ranges.append((start, end))
        return ranges

    def mergeRanges(self, ranges):
        ranges.sort()
        merged = [ranges[0]]

        for start, end in ranges[1:]:
            last_start, last_end = merged[-1]
            if start <= last_end:  # overlap
                merged[-1] = (last_start, max(last_end, end))
            else:
                merged.append((start, end))

        return merged

    def findFreshItems(self, rangeFile, itemsFile):
        ranges = self.parseRangeInput(rangeFile)
        items = self.parseItemsInput(itemsFile)

        ranges = self.mergeRanges(ranges)

        fresh = 0
        for range in ranges:
            fresh += (range[1] - range[0] + 1)

        '''
        First part of the problem
        
        # Binary search helper
        import bisect
        starts = [r[0] for r in ranges]

        fresh = 0
        for x in items:
            idx = bisect.bisect_right(starts, x) - 1
            if idx >= 0:
                s, e = ranges[idx]
                if s <= x <= e:
                    fresh += 1
        '''
        return fresh


day5Solution = Solution()
print(day5Solution.findFreshItems("valid_item_ranges.txt", "items.txt"))