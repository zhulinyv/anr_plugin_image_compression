import gradio as gr

from plugins.anr_plugin_image_compression.utils import (
    image_compression,
    image_organization,
)


def plugin():
    with gr.Tab("压缩整理"):
        image_path = gr.Textbox("", label="图片目录")
        image_format = gr.Radio(
            ["jpg", "png", "webp"],
            value="png",
            label="大小: png>jpg>webp, 质量: webp>png>jpg, 数据: png>webp>jpg",
        )
        with gr.Row():
            compression_button = gr.Button("仅压缩")
            organization_button = gr.Button("仅整理")
            compression_and_organization_button = gr.Button("压缩并整理")
        output_info = gr.Textbox(label="输出信息")

        compression_button.click(
            image_compression, inputs=[image_format, image_path], outputs=output_info
        )
        organization_button.click(
            image_organization,
            inputs=[image_format, image_path, gr.Checkbox(False, visible=False)],
            outputs=output_info,
        )
        compression_and_organization_button.click(
            image_organization,
            inputs=[image_format, image_path, gr.Checkbox(True, visible=False)],
            outputs=output_info,
        )
