#storage into text file

file1=open("mytext.txt","w")

file1.writelines("Hello World. ")
file1.writelines(input("Enter your text here: "))
file1.writelines("Today is Monday. ")

file1.close()

file2=open("mytext.txt","r")

a_word=input("Enter your text here: ")
for line in file2:
    if a_word in line:
    print(line)

file2.close()
