a = "AAAA"
b = "BB"
c = 1.122222233
# ou string = 'a={} b={} c={:.2f}'
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)