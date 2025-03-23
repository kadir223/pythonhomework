Sample="sample.txt"
if not Sample:
    with open(Sample,"w") as file:
        text=input("Enter a paragraph:")
        file.write(text)
with open(Sample,"r") as file:
    words=file.read().split().lowercase()


