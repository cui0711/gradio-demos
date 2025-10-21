import json

input_file = "imagenet-simple-labels.json"
output_file = "labels.txt"

with open(input_file, "r", encoding="utf-8") as f:
    labels = json.load(f)

with open(output_file, "w", encoding="utf-8") as f:
    for label in labels:
        f.write(f"{label}\n")

print(f"已生成 {output_file}，共 {len(labels)} 行。")