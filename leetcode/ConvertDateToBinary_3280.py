from builtins import str


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        t = ""
        result = ""
        for c in date:
            if c.isdigit():
                t += c
            else:
                if t:  # If t is not empty
                    result += bin(int(t))[2:]  # Convert the accumulated digits to binary
                result += c  # Add the non-digit character
                t = ""  # Reset the accumulated digits

        if len(t) > 0:  # Handle remaining digits at the end of the string
            result += bin(int(t))[2:]

        return result


# Example Usage
x = Solution()
date_str = "2080-02-29"
binary_date = x.convertDateToBinary(date_str)
print(binary_date)
