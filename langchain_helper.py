from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_assembly_and_enhancers(gene):
    prompt_template_name = PromptTemplate(
        input_variables=['gene'],
        template="I want to know enhancers for {gene}. Give all the names."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="assembly")

    
    prompt_template_items = PromptTemplate(
        input_variables=['assembly'],
        template="""Give enhancers for {assembly}. Return it as a comma separated string"""
    )

    enhancer_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="enhancers")

    chain = SequentialChain(
        chains=[name_chain, enhancer_items_chain],
        input_variables=['gene'],
        output_variables=['assembly', "enhancers"]
    )

    response = chain({'gene': gene})

    return response

if __name__ == "__main__":
    print(generate_assembly_and_enhancers("nanog"))
