import streamlit as sp
import google.generativeai as ai
ai.configure(api_key='AIzaSyBb78vgrSXypIr4YYjkoozC5DGAwwYU0TM')
sys_prompt = '''you are an python code reviewer only replay to python code related problems
create a bug report of given python code and generate correct code if there is an issue or room for improvement with headings as bug report,fixed code and summary
if there is no error in the code give what will be the output of the code or facts  
and lastly give summry or explanation
 '''
model = ai.GenerativeModel(system_instruction=sys_prompt)
sp.title('Python Code Reviewer')
user_prompt = sp.text_area('Enter your code here : ',placeholder = 'enter your query here:',height=200 )
button = sp.button('Review')

if button == True:
  if not user_prompt.strip():
    sp.error('Enter python code to reviewe')
  else:
    responce = model.generate_content(user_prompt)
    sp.write(responce.text)

