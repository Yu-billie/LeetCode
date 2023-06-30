class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle special cases
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1

        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)

        # Convert both dividend and divisor to positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Initialize the quotient and current divisor
        quotient = 0
        current_divisor = divisor

        # Bitwise division algorithm
        while dividend >= divisor:
            current_divisor = divisor
            count = 1

            # Double the current divisor until it exceeds the remaining dividend
            while (current_divisor << 1) <= dividend:
                current_divisor <<= 1
                count <<= 1

            # Subtract the current divisor from the dividend and update the quotient
            dividend -= current_divisor
            quotient += count

        # Apply the sign to the quotient
        if negative:
            quotient = -quotient

        return quotient



s = Solution()
dividend = 7
divisor = -3
print(s.divide(dividend, divisor))