with open("sample.txt") as f:
     f.write("hello world\nhello again\n")

with open("sample.txt" , "r") as f:
      content = f.read()
      print(content)
