try:
    print("Reading file content:")
    with open('sample.txt','r') as reader:
        c=0
        for line in reader:
            clean_line = line.rstrip()
            c = c+1
            print(f"Line {c}: {clean_line}")
    reader.close()
except:
    print("Error: The file 'sample.txt' was not found.")

input("\nPress Enter To Exit...")