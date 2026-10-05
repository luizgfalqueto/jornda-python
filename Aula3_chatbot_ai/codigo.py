# titulo
# campo de mensagem (input)
# quando o usuario enviar uma mensagem
    # mostrar a mensagem na conversa
    # mandar mensagem para a ia responder
    # mostrar a resposta na conversa

import streamlit as st
from openai import OpenAI

model = OpenAI(api_key='', 
               base_url='https://generativelanguage.googleapis.com/v1beta/openai')

st.write('## ChatBot de IA')

if not 'message_list' in st.session_state:
    st.session_state['message_list'] = []

for message in st.session_state['message_list']:
    st.chat_message(message['role']).write(message['content'])

user_message = st.chat_input('Escreva sua mensagem aqui')

if user_message:
    # mostrar a mensagem na conversa
    st.chat_message('user').write(user_message)
    userMessage = {'role': 'user', 'content': user_message}
    st.session_state['message_list'].append(userMessage)

    # pegar a resposta da IA
    model_response = model.chat.completions.create(
        messages=st.session_state['message_list'],
        model='gemini-flash-lite-latest'
    )

    ia_response = model_response.choices[0].message.content

    # enviar a mensagem da ia no chat
    st.chat_message('assistant').write(ia_response)
    assistantMessage = {'role': 'assistant', 'content': ia_response}
    st.session_state['message_list'].append(assistantMessage)