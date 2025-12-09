'''
Intution: Identify numbers that are formed by repeating a
smaller number x at least n times, where n >= 2.

Valid Examples:
- 11111 --> x = 1, n = 5
- 121212 --> x = 12, n = 3
- 123123 --> x = 123, n = 2

To check this, convert the number to a string and see if
there exists a pattern such that:

pattern * n = number (n >= 2)

Lenght of pattern when n = 2:
- If the number has even length, len(pattern) = len(number) // 2
- If the number has odd length, len(pattern) = (len(number) // 2) + 1

The maximum length of pattern is (len(number) // 2) + 1
'''
class Solution:
    def findInvalidIds(self, input):
        res = 0
        # split the input by comma
        ranges = input.split(",")
        for ran in ranges:
            # split the range by hyphen like start - end
            start = int(ran.split("-")[0])
            end = int(ran.split("-")[1])
            res += self.findInvalidInRange(start,end)
        print('Final res:', res)
        return

    def findInvalidInRange(self, start, end) -> int:
        res = 0
        # iterate through all values from start to end to find pattern
        for i in range(start, end + 1):
            string_form = str(i)    # convert the number to string
            n = len(string_form)
            for window in range(1, n // 2 + 1): # pattern size ranges from 1 to (n/2 + 1)
                if n % window != 0:
                    continue 
                pattern = string_form[:window]
                repeats = n // window
                if repeats >= 2 and pattern * repeats == string_form:
                    res += i
                    break
        return res

input = "328412-412772,1610-2974,163-270,7693600637-7693779967,352-586,65728-111612,734895-926350,68-130,183511-264058,8181752851-8181892713,32291-63049,6658-12472,720-1326,21836182-21869091,983931-1016370,467936-607122,31-48,6549987-6603447,8282771161-8282886238,7659673-7828029,2-18,7549306131-7549468715,3177-5305,20522-31608,763697750-763835073,5252512393-5252544612,6622957-6731483,9786096-9876355,53488585-53570896"
day2Solution = Solution()
print(day2Solution.findInvalidInRange(input))