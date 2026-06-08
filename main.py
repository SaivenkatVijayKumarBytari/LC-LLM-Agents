import os
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

dotenv.load_dotenv()

llm_agent = ChatGoogleGenerativeAI(model = "gemini-3-flash-preview")

#llm_agent = ChatOllama(model="gemma3:1b")

summary = """It is named after the engineer Gustave Eiffel, whose company designed and built the tower from 1887 to 1889.
            Locally nicknamed "La dame de fer" (French for "Iron Lady") for its use of wrought iron, 
            it was constructed as the centrepiece of the 1889 World's Fair, and to crown the centennial
            anniversary of the French Revolution. Although initially criticised by some of France's leading 
            artists and intellectuals for its design, it has since become a global cultural icon of France 
            and one of the most recognisable structures in the world.[5] The tower received 5,889,000 visitors
            in 2022.[6] The Eiffel Tower is the most visited monument with an entrance fee in the world:[7] 
            6.91 million people ascended it in 2015. It was designated a monument historique in 1964, and was 
            named part of a UNESCO World Heritage Site ("Paris, Banks of the Seine") in 1991.[8]"""
llm_template = """Providing summary about a monument: {summary}, I want you to create
                  A short summary about the monument in 1-2 sentences, and a list of 3 interesting facts about the monument.
"""
summary_prompt_template = PromptTemplate(
    input_variables=["summary"],
    template=llm_template
)

chain =  summary_prompt_template | llm_agent

def main():
    print("Hello from lc-llm-agents!")
    response = chain.invoke({
        "summary": summary
    })

    print(response)

if __name__ == "__main__":
    main()
