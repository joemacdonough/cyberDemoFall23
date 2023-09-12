import sys
def xor(vals, key):
        b = bytearray(vals)
        for i in range(len(b)):
            b[i] ^= key
        return b

def separate(string):
    vals = string.split(' ')
    for i in range(len(vals)):
        vals[i] = int(vals[i],16)
    return vals

try:
    input = sys.argv[1]
    key = sys.argv[2]
    nums = separate(input)
    final = xor(nums, int(key, 16))
    print(final.decode())

except Exception as e:
    print("Error occured! Make sure you are using the script in the format:")
    print('>python encoder.py "INPUT STRING" DECODE KEY')
    print('EXAMPLE:>python encoder.py "00 01 02 03" 04')
