import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = Ollama(model="mistral:latest",
             callback_manager=CallbackManager(
                 [StreamingStdOutCallbackHandler()]))

cmd = input("give me a command: ")

prompt = PromptTemplate(
    input_variables=["what"],
    template="You are a smart assistant .Take input {what} and give output in linux terminal commands in bash shell, give me only one command without any explanation or description in a single line")

# prompt = PromptTemplate(
#     input_variables=["command"],
#     template="You are a smart assistant .Take name of linux terminal {command} and give 5 examples on how to use it with different flags",
# )
chain = LLMChain(llm=llm, prompt=prompt)


output = (chain.run(cmd))
