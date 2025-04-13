from chat.requirements_integration import RequirementsIntegration, PossibleModels

print("Enter message for requirements model!")

while(True):
    msg = input(">") 
    if msg == "/exit":
        print("Goodbye")
        break

    integration = RequirementsIntegration()

    answer = integration.get_response(PossibleModels.LLAMA3.value["name"], msg)
    
    print(answer)