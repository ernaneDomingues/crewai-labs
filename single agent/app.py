import streamlit as st
from main import run_investiment_assistent

st.title('Investiment Assistent')
st.write('Pergunte sobre investimento')

with st.sidebar:
    st.header('Selecione a tarefa')
    tipo_tarefa = 'Responder sobre investimento'

    pergunta = st.text_area('Digite a pergunta:')

if st.button('Executar tarefa'):
    if not pergunta.strip():
        st.warning('Digite uma pergunta')
    else:
        st.write('Processando...')
        result = run_investiment_assistent(pergunta)
        st.subheader('Resultado:')
        st.write(result)