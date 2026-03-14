# here also, first it is necessary that we must have an 'OPENAI_API_KEY'

from langchain_openai import ChatOpenAI    # note that here it's "ChatOpenAI" we used 
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0.5, max_completion_tokens=10)

# temperature -> is a hyperparameter that controls the randomness, creativity, and "flair" of the generated text 

# max_completion_tokens -> a parameter in OpenAI's API that limits the maximum number of tokens generated in the completion, including reasoning tokens
 
# result = model.invoke("what is the capital of India")


result = model.invoke("write a poem on the sun")


print(result.content)    # note here in "ChatModel" we use print(result.content) to print the 'result_text' 