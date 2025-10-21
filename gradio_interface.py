"""
This script creates a Gradio interface showcasing various input and output components.
Each input component is paired with a corresponding output component."""

import gradio as gr
from PIL import Image

input_list = [
    gr.Audio(sources=["microphone", "upload"], type="filepath", label="Record your voice"),
    gr.Checkbox(label="Checkbox"),
    gr.Dropdown(choices=["Option 1", "Option 2", "Option 3", "Option 4"], label="Select an option"),
    gr.Image(sources=["upload", "webcam", "clipboard"], type="filepath", label="Upload an image"),
    gr.Slider(minimum=0, maximum=100, step=1, label="Select a value"),
    gr.File(label="Upload a file", type="filepath"),
    gr.Number(label="Enter a number"),
    gr.Radio(choices=["Choice A", "Choice B", "Choice C"], label="Choose one"),
    gr.Textbox(type="text", placeholder="Enter some text", label="Text Input"),
    gr.TextArea(placeholder="Enter multiple lines of text", label="Text Area", lines=4),
    gr.Dataframe(headers=["Column 1", "Column 2"], label="Data Frame Input"),
    gr.Markdown(value="**This is a markdown component.**", label="Markdown Display")
]

output_list = [
    gr.Textbox(label="Audio Output"),
    gr.Textbox(label="Checkbox Output"),
    gr.Textbox(label="Dropdown Output"),
    gr.Image(label="Image Output"),
    gr.Textbox(label="Slider Output"),
    gr.Textbox(label="File Output"),
    gr.Textbox(label="Number Output"),
    gr.Textbox(label="Radio Output"),
    gr.Textbox(label="Text Output"),
    gr.Textbox(label="Text Area Output"),
    gr.Textbox(label="Data Frame Output"),
    gr.Markdown(value="**This is an output markdown component.**", label="Markdown Output")
]

def input_to_output(audio, checkbox, dropdown, image, slider, file, number, radio, text, text_area, dataframe, markdown):

    # print(image)
    image = Image.open(image).convert("L") if image else None

    return audio, str(checkbox), dropdown, image, str(slider), file, str(number), radio, text, text_area, dataframe, markdown

demo = gr.Interface(
    fn=input_to_output, 
    inputs=input_list, 
    outputs=output_list,    
    title="Gradio Input and Output Components Showcase",
    description="This interface demonstrates a variety of input and output components available in Gradio.",
    live=True
    )

demo.launch()