"""A Gradio Blocks interface with custom CSS, tabs, rows, columns, and various interactive components."""

import gradio as gr
from gradio.media import get_image, get_video

with open("style.css", "r", encoding="utf-8") as f:
    css_text = f.read()

gallery_items = [
        ("https://upload.wikimedia.org/wikipedia/commons/0/09/TheCheethcat.jpg", "cheetah1"),
        ("https://nationalzoo.si.edu/sites/default/files/animals/cheetah-003.jpg", "cheetah2"),
        ("https://videos.pexels.com/video-files/3209828/3209828-uhd_2560_1440_25fps.mp4", "world"),
        (get_image("cheetah.jpg"), "cheetah3"),
        (get_video("world.mp4"), "world2")
    ]

with gr.Blocks(css=css_text) as demo:
    with gr.Tab(label="txt2img"):
        with gr.Row():
            with gr.Column(scale=15):
                textbox1 = gr.Textbox(lines=2, label="")
                textbox2 = gr.Textbox(lines=2, label="")
            with gr.Column(scale=1, min_width=1):
                button1 = gr.Button(value="1", elem_classes=["four_btn_high"])
                button2 = gr.Button(value="2", elem_classes=["four_btn_high"])
                button3 = gr.Button(value="3", elem_classes=["four_btn_high"])
                button4 = gr.Button(value="4", elem_classes=["four_btn_high"])
            with gr.Column(scale=1):
                with gr.Row():
                    button5 = gr.Button(value="Generate", variant="primary", scale=2, elem_classes=["generate_btn_high"])
                with gr.Row():
                    dropdown1 = gr.Dropdown(choices=["a", "b", "c"], label="Style 1", min_width=1, interactive=True)
                    dropdown2 = gr.Dropdown(choices=["x", "y", "z"], label="Style 2", min_width=1, interactive=True)
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    dropdown3 = gr.Dropdown(choices=["option1", "option2"], label="Sampling method", min_width=1, interactive=True)
                    slider1 = gr.Slider(minimum=1, maximum=100, step=1, label="Sampling steps", value=20, interactive=True)
                checkboxgrp = gr.CheckboxGroup(choices=["Restore faces", "Tilling", "Hires.fix"], label="", interactive=True)
                with gr.Row():
                    slider2 = gr.Slider(minimum=256, maximum=2048, step=64, label="Width", value=512, interactive=True)
                    slider3 = gr.Slider(minimum=256, maximum=2048, step=64, label="Batch count", value=4, interactive=True)
                with gr.Row():
                    slider4 = gr.Slider(minimum=256, maximum=2048, step=64, label="Height", value=512, interactive=True)
                    slider5 = gr.Slider(minimum=1, maximum=16, step=1, label="Batch size", value=12, interactive=True)
                slider6 = gr.Slider(minimum=1.0, maximum=20.0, step=0.1, label="CFG Scale", value=7.0, interactive=True)
                with gr.Row():
                    numberbox1 = gr.Number(label="Seed", interactive=True, scale=7, elem_classes=["seed_input"])
                    button_reset_seed = gr.Button(value="Reset", min_width=1, scale=1, elem_classes=["reset_btn"])
                    button_copy_seed = gr.Button(value="Copy", min_width=1, scale=1, elem_classes=["copy_btn"])
                    checkbox = gr.Checkbox(label="Extra", value=False, interactive=True, min_width=1, scale=1, elem_classes=["extra_checkbox"])
                dropdown4 = gr.Dropdown(choices=["Model 1", "Model 2"], label="Script", min_width=1, interactive=True)
            with gr.Column():
                gallery = gr.Gallery(value=gallery_items, label="")
                with gr.Row():
                    button6 = gr.Button(value="File", min_width=1, elem_classes=["six_btn_high"])
                    button7 = gr.Button(value="Save", min_width=1, elem_classes=["six_btn_high"])
                    button8 = gr.Button(value="Zip", min_width=1, elem_classes=["six_btn_high"])
                    button9 = gr.Button(value="Send to img2img", min_width=1, elem_classes=["six_btn_high"])
                    button10 = gr.Button(value="Send to inpaint", min_width=1, elem_classes=["six_btn_high"])
                    button11 = gr.Button(value="Send to extras", min_width=1, elem_classes=["six_btn_high"])
                textbox3 = gr.Textbox(lines=4, label="")
    with gr.Tab(label="img2img"):
        pass
demo.launch()