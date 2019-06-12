INFY-35 ROMAN TO NUM
class roman_to_int:
    def roman(self, str):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(str)):
            if i > 0 and rom_val[str[i]] > rom_val[str[i - 1]]:
                int_val += rom_val[str[i]] - 2 * rom_val[str[i - 1]]
            else:
                int_val += rom_val[str[i]]
        return int_val
s=str(input(""))
print(roman_to_int().roman(s))

CIRCULAR ARRAY ROTATION
n, k, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range (q):
    num = int(input())
    i = (num - k) % n
    print(a[i])
