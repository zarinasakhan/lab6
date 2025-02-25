string="HelloWorld"
uppers=sum(map(str.isupper, string))
lowers=sum(map(str.islower, string))
print(f"the sum of uppers: {uppers}")
print(f"the sum of lowers: {lowers}")