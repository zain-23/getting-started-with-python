def main():
 height = get_height()
 for i in range(height):
  print("#")

def get_height():
 while True:
   try:
      n = int(input("Height :"))
      if n > 0 :
        return n
   except ValueError:
     print("Invalid type")
  
main()