print("**********Welcome to my Chatbot!*********")

while True:
  user= input("Enter your prompt: ")

  if user== "hello" or user=="hi" or user=="hey":
    print("Hello! How can I help you today?")
  elif user== "how are you":
    print("I'm doing well, thanks for asking!,what about you?")
  elif user=="i'm doing good too":
    print("good to know")
  elif user == "what can you do":
    print("I can answer all your basic questions and hold simple conversations.")
  elif user=="what's the year?":
   print("the current year is 2024")
  elif user=="thanks":
   print("you are welcome!")
  elif user== "bye" or user== "exit":
    print("Goodbye! Have a nice day.")
    break
  else:
    print("Sorry, I can't understand please try to use correct grammar and spelling or try asking a different question,thankyou!")