"""A simple Gradio interface that takes a name as input and returns a greeting message."""

import gradio as gr

def greet(name):
    return f"Hi, {name}!"

iface = gr.Interface(fn=greet, inputs=gr.Textbox(type="text", placeholder="Enter your name", label="Name", lines=5), outputs=gr.Textbox(label="Greeting"))

iface.launch()