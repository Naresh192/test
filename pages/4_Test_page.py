import streamlit as st
import pickle 
st.set_page_config(layout="wide") # for making UI wide

st.markdown('''<style>div[data-testid="stToolbar"] {
  visibility: hidden;
}</style>''',unsafe_allow_html=True)
try :
    video = open('video.pkl', 'rb')
except :
    video = open('video.pkl', 'wb')
    pickle.dump('None', video)
    video.close()
    video = open('video.pkl', 'rb')
try :
    chat = open('chat.pkl', 'rb')
except :
    chat = open('chat.pkl', 'wb')
    pickle.dump([], chat)
    chat.close()
    chat = open('chat.pkl', 'rb')
l=pickle.load(video)
video_url=st.text_input("URL",'None')
if video_url!='None':
    video_player = st.video(video_url,autoplay=True)
elif l!='None' :
    video_player = st.video(l)
elif video_url=='None' :
    video_player = st.video(l)
else :
    pass
chat=pickle.load(chat)
message=st.text_input('Text','')
c1,c2,c3=st.columns(3)
if c1.button("Send") :
    chat.append(message)
a=st.empty()
chats=''
for i in chat[::-1] :
    chats+='\n'+i
a.text(chats)
if c2.button("Refresh Chat") :
    a.empty()
    chats=''
    for i in chat[::-1] :
        chats+='\n'+i
    a.text(chats)

if c3.button("Clear Chat") :
    chat=[]
if video_url!='None' :
    video = open('video.pkl', 'wb')
    pickle.dump(video_url, video)
chat2 = open('chat.pkl', 'wb')
pickle.dump(chat, chat2)
