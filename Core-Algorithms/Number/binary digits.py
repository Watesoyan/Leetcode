def bits(x):
    bits = []
    while True:
        if x > 1:
            q = x >> 1
            r = x - (q << 1)
            x = q
            bits.append(r)
        else:
            bits.append(x)
            bits.reverse()
            return bits
