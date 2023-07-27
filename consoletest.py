
import mychatbot

myChatBot = mychatbot.MyChatBot()
myChatBot.initializeBot()  



exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print("respueata:"+myChatBot.newmessage("344644316022",query))

