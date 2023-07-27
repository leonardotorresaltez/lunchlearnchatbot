
import os
from dotenv import load_dotenv, find_dotenv
from langchain.agents import  ConversationalChatAgent
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents.agent import AgentExecutor




from langchain.chat_models import ChatOpenAI

class MyChatBot:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def initializeBot(self):
        if  self.ready:
            return
        tools = []
        _ = load_dotenv(find_dotenv()) #read local .env file
        llm=ChatOpenAI(
            openai_api_key=os.getenv('OPENAI_API_KEY'),
            temperature=0
        )
        system_message = "Ten una conversacion en lenguaje español con un humano, respondiendo las preguntas tan bien como puedas"
        memory = ConversationBufferWindowMemory(
            memory_key="chat_history",  
            k=5,
            return_messages=True
        )
        custom_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools, system_message=system_message)
        agent_executor = AgentExecutor.from_agent_and_tools(agent=custom_agent, tools=tools, memory=memory)
        agent_executor.verbose = True
        self.agent_executor = agent_executor
        print(
            agent_executor.agent.llm_chain.prompt
        )
        self.ready= True
    
    def __init__(self):
        self.ready = False



    def newmessage(self,telefonoCliente,humanmessage) ->str:
        return self.agent_executor.run(input=humanmessage)

