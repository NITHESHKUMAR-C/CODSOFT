def chatbot():
    print("hi i'm chatbot.type 'exit' to end the chat. ")
    while True:
        user=input("You: ").lower()
        if user == "exit":
            print("Chatbot:Goodboy have a nice day!")
            break
        elif "hello" in user or "hi" in user:
            print("chatbot:Hello how can i help you today?")
        elif "who are you" in user or "what are you" in user:
            print("chatbot:i am chatbot for basic conversation")
        elif "weather" in user:
            print("i am not connected to internet,check at weather.com")
        elif "time" in user:
            from datetime import datetime
            now=datetime.now()
            print(f"ChatBot: The current time is {now.strftime('%H:%M:%S')}.")
        elif "thank you" in user or "thanks" in user:
            print("chatbot:you are welcome")
        else:
            print("chatbot:can you ask something else")
chatbot()