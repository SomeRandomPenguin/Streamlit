import todolist
import datetime as dt
import streamlit as st

@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def connect_db():
    db = todolist.todolist_pd()
    return db

db = connect_db()
st.title('Memothing - v0.1')

option = st.sidebar.selectbox('Menu',['Select one','New','Edit','Load','Delete','Save','Open'])

if option == 'Select one':
    st.write('Please choose one from the sidebar')
    
elif option == 'New':
    st.write('Create a New memo')
    topic = st.text_input("Topic",'Replace this message')
    body = st.text_input("Body",'Replace this message')
    date = st.date_input("Target date")
    newb = st.button("Done")
    if newb:
        db.create(topic,body,date)
    
elif option == 'Edit':
    st.write('Edit an existing memo')
    topic1 = st.text_input("Topic of memo you will edit",'Replace this message')
    body1 = st.text_input("New body message",'Replace this message')
    date1 = st.date_input("New target date")
    editb = st.button("Finish")
    if editb:
        db.edit(topic1,body1,date1)
    
elif option == 'Delete':
    st.write('Delete a memo')
    topic2 = st.text_input("Topic you will delete",'Replace this message')
    delb = st.button("Delete")
    if delb:
        db.delete(topic2)

elif option == 'Load':
    st.write("Load all memos")
    loadb = st.button("Load")
    if loadb:
        df = db.read()
        st.write(df)

elif option == 'Save':
    st.write("Save current memos")
    name1 = st.text_input("Name of file")
    saveb = st.button("Save")
    if saveb:
        db.save(name1)

elif option == 'Open':
    st.write("Open saved memo")
    name = st.text_input("Name of file")
    openb = st.button("Open")
    if openb:
        db.load(name)
        