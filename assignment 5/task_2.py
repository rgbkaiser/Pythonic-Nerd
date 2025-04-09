list = [i*1 for i in range(1,11)]
print(f"Original list: {list}")
extraction = list[0:5]
print(f"Extracted first five elements: {extraction}")
print(f"Reversed extracted elements: {extraction[::-1]}")