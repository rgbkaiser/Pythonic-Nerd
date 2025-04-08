inp = input("Enter text to write to the file: ")

with open('output.txt','w') as writer:
    writing = writer.write(inp)
writer.close()

print("Data successdully written to output.txt.\n")

inp2 = input("Enter additional text to append: ")

with open('output.txt','a') as appender:
    appending = appender.write('\n'+inp2)
appender.close()

print("Data successdully appended.\n")

print("Final content of output.txt:")
with open('output.txt','r') as reader:
    print(reader.read())
reader.close()