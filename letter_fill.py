letter='''
      Dear <|Name|>,
      \tYou are selected!
      <|Date|>
      '''
name=input("Enter your name: ")
date=int(input("Enter date: "))
month=int(input("Enter month: "))
year=int(input("Enter year: "))
print(letter.replace("<|Name|>",f"{name}").replace("<|Date|>",f"{date}-{month}-{year}"))