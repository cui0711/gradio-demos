from torchvision import transforms
from ultralytics import YOLO
import gradio as gr
from PIL import Image
import torch
import os

# 模型定义
model_seg = YOLO('yolov8n-seg.pt')
model_detect = YOLO('yolov8s-oiv7.pt')
model_cls = torch.hub.load(repo_or_dir='pytorch/vision:v0.6.0', model='resnet18', pretrained=True).eval()

# 标签定义
file_path = 'labels.txt'
with open(file_path, 'r') as file:
    labels = file.readlines()
labels = [label.strip() for label in labels]


def seg(image):
    results = model_seg([image])
    for r in results:
        im_array = r.plot()
        img = Image.fromarray(im_array[..., ::-1])  # BGR to RGB
    
    return img

def det(image):
    results = model_detect([image])
    for r in results:
        im_array = r.plot()
        img = Image.fromarray(im_array[..., ::-1])  # BGR to RGB
    
    return img

def cls(image):
    image = transforms.ToTensor()(image).unsqueeze(0)
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model_cls(image)[0], dim=0)
        confidences = {labels[i]: float(prediction[i]) for i in range(len(labels))}

    return confidences

current_dir = os.path.dirname(__file__)
with gr.Blocks() as demo:
    with gr.Tab("图像分类"):
        gr.Markdown("# 图像分类演示")
        with gr.Row():
            input_img = gr.Image(sources=["upload"], label="输入图像", type="pil")
            output_label = gr.Label(num_top_classes=10)
            
        # 我用autodl远程编写代码，似乎因为Gradio的安全策略导致路径被限制，无法使用本地图片作为Examples。
        # 我没有尝试在本地运行代码。
        # gr.Examples(examples=[[os.path.join(current_dir, "cat.jpg")], [os.path.join(current_dir, "dog.jpeg")]], inputs=[input_img])
        button = gr.Button(value="分类", variant="primary")
        button.click(fn=cls, inputs=input_img, outputs=output_label)
    with gr.Tab("语义分割"):
        gr.Markdown("# 语义分割演示")
        with gr.Row():
            input_img2 = gr.Image(sources=["upload"], label="输入图像", type="pil")
            output_img2 = gr.Image(type="pil")
        # gr.Examples(examples=[['./dog.jpeg'], ['./cat.jpg']], inputs=[input_img2])
        button2 = gr.Button(value="分割", variant="primary")
        button2.click(fn=seg, inputs=input_img2, outputs=output_img2)
    with gr.Tab("目标检测"):
        gr.Markdown("# 目标检测演示")
        with gr.Row():
            input_img3 = gr.Image(sources=["upload"], label="输入图像", type="pil")
            output_img3 = gr.Image(type="pil")
        # gr.Examples(examples=[['./dog.jpeg'], ['./cat.jpg']], inputs=[input_img3])
        button3 = gr.Button(value="检测", variant="primary")
        button3.click(fn=det, inputs=input_img3, outputs=output_img3)

demo.launch()