import streamlit as st

def main():
    st.title("ShineAI - A Car Care Assistant")

    if 'chat_history' not in st.session_state:  
        st.session_state['chat_history'] = []   

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Conversation History**")  
        if 'chat_history' in st.session_state:  
            chat_history = st.session_state['chat_history']
        else:
            chat_history = []  
        for message in chat_history:
            st.write(message) 

    with col2:
        user_input = st.text_input("You: ", key="user_input")  

    if user_input:
        st.session_state['chat_history'].append(user_input)  
        chatbot_response = process_message(user_input)
        st.session_state['chat_history'].append(chatbot_response) 

def process_message(message):
    return "Nothing So Far" 

if __name__ == "__main__":
    main()