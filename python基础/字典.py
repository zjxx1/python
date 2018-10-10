d={"one":1,"two":2,"three":3}
dd={k:v for k,v in d.items()}
print(dd)
print("*" * 10)
cc={k:v for k,v in d.items() if v%2==0}
print(cc)
