# Day 5 — Fresh Ingredient Identification
## Intuition

An ingredient is fresh if it falls within any of the ID ranges.
However:
- Ranges may overlap
- They may appear unordered
- Some ranges may be fully contained inside others

### Approach for 1st problem - Merge ranges and Binary Search
Question: Given a list of IDs find the number of fresh IDs

#### Merge Ranges
Since the ranges may overlap, merge the ranges so that there
are no overlapping ranges present

#### Binary Search
Once merged, ranges are sorted and non-overlapping.For each ingredient ID x,
we determine which range it might fall inside. We do this by performing a
binary search on the start values of the range

For example:
```
    x = 11
    merged_sorted_ranges = [(3, 5), (10, 20)]
    starts = [3,10]  
```
We would need to find where can 11 be placed and explore the index right before
it. In this case it would be 10,20
```
    [3,10] --> [3,11,10]
```

We then check if x falls in this range
```
    start <= x <= end
    10 <= 11 <= 20
```
If this condition is true we update the number of fresh items

Time Complexity: O(IlogR)

### Approach for 2nd problem - Merge ranges
Question: Given just the range of IDs, find the total number of fresh items

If we solve the first problem, the second is simpler as we already merged
the ranges to have non-overlapping values. We need to just sum up all 
possible IDs in a range. It can be done easily with:
```
    total_fresh_ids += (end - start + 1)
```

Time Complexity: O(n)