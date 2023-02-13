import streamlit as st
import functions as fn
import datetime

todos = fn.get_todos()

st.set_page_config(layout="wide")


def add_todo():
    my_todo = f"{st.session_state['new_todo']}\n"
    todos.append(my_todo)
    fn.write_todos(todos)


st.title("My Todo App")
st.date_input("Current Date:")
st.write("Whatcha need to do homie? <b>Type it down</b>...", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(f"{todo}", key=f"{todo}")
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add todo",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")
