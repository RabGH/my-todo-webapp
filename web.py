import streamlit as st
import functions as fn
import time

now = time.strftime("%b %d, %Y, %I:%M%p")

todos = fn.get_todos()


def add_todo():
    my_todo = f"{st.session_state['new_todo']}\n"
    todos.append(my_todo)
    fn.write_todos(todos)


st.title("My Todo App")
st.subheader(now)
st.write("Whatcha need to do homie? Type it down...")

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

# print("Hello")

# st.session_state