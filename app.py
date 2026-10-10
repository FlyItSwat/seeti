import streamlit as st
import time

st.set_page_config(page_title='Seeti', page_icon='🍲', layout='centered')
st.markdown('''<style> .block-container{max-width:520px;padding-top:2rem} .stButton>button{width:100%;min-height:62px;border-radius:16px;font-size:22px;font-weight:700} h1{text-align:center} .muted{text-align:center;color:#666} </style>''',unsafe_allow_html=True)
st.title('🍲 SEETI')
st.markdown('<p class="muted">Cook without counting whistles.</p>',unsafe_allow_html=True)
if 'started' not in st.session_state: st.session_state.started=False
if 'start' not in st.session_state: st.session_state.start=0
if not st.session_state.started:
    st.markdown('### What are you cooking?')
    foods=['Dal','Rice','Rajma','Chole','Potato','Other']
    cols=st.columns(2)
    for i,food in enumerate(foods):
        with cols[i%2]:
            if st.button(food,key=food):
                st.session_state.food=food
                st.session_state.started=True
                st.session_state.start=time.time()
                st.rerun()
else:
    st.markdown(f'### {st.session_state.food} is cooking')
    elapsed=int(time.time()-st.session_state.start)
    st.metric('Cooking time',f'{elapsed//60:02d}:{elapsed%60:02d}')
    st.info('Listening for whistles… Connect the Seeti sensor for automatic counting.')
    if 'whistles' not in st.session_state: st.session_state.whistles=0
    st.metric('Whistles detected',st.session_state.whistles)
    st.caption('Demo mode: Tap below to simulate a detected whistle. Cooking readiness is not inferred from whistle count alone.')
    if st.button('🔊 Simulate whistle'):
        st.session_state.whistles+=1
        st.rerun()
    if st.button('Finish cooking'):
        st.session_state.started=False
        st.session_state.whistles=0
        st.rerun()
st.divider()
st.caption('Seeti is a cooking assistant, not a safety monitor. Never leave a lit stove unattended. Follow your pressure cooker manufacturer’s instructions.')
