from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# Model Import
llm = Ollama(model="mistral:latest",
             callback_manager=CallbackManager(
                 [StreamingStdOutCallbackHandler()]))

# Choose how you want help
cmd = input(
    "HI! \n press 1 to get help performing a task  \n press 2 to get basic information about a command \n press 3 to get more advanded usage information with flags: ")

# Just give the command for Natural language request
if cmd == '1':
    cmd_1 = input("Tell me the task you want to perform: ")
    prompt = PromptTemplate(
        input_variables=["command_1"],
        template="You are a smart assistant .Take input {command_1} and give output in linux terminal commands in bash shell, give me only one command without any explanation or description in a single line")

    chain_1 = LLMChain(llm=llm, prompt=prompt)
    print(chain_1.run(cmd_1))

# Give more info about command with flags
elif cmd == '2':
    cmd_2 = input("Description of command: ")
    prompt = PromptTemplate(
        input_variables=["command_2"],
        template="You are a smart assistant .Take name of linux terminal {command_2} and give 5 examples on how to use it",
    )
    chain_2 = LLMChain(llm=llm, prompt=prompt)
    print(chain_2.run(cmd_2))

elif cmd == '3':
    cmd_3 = input("More information about the command: ")
    prompt = PromptTemplate(
        input_variables=["command_3"],
        template="You are a smart assistant .Take name of linux terminal {command_3} and give 10 examples on how to use it with different flags",
    )
    chain_3 = LLMChain(llm=llm, prompt=prompt)
    print(chain_3.run(cmd_3))
