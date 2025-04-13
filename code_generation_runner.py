from chat.code_generation_integration import CodeGenerationIntegration, PossibleModels

print("Enter message for code model!")

while(True):
    msg = input(">") 
    if msg == "/exit":
        print("Goodbye")
        break

    integration = CodeGenerationIntegration()

    answer = integration.get_response(PossibleModels.CODELLAMA.value["name"], msg)
    
    print(answer)