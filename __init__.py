"""图片压缩整理插件。"""
from __future__ import annotations

from plugins.anr_plugin_image_compression.utils import image_compression, image_organization
from utils.plugins import Action, Field, Panel, Plugin


def register(plugin: Plugin):
    panel = Panel(
        id="compression",
        title="压缩整理",
        icon="🗜️",
        description="批量压缩 / 整理图片, 支持 jpg / png / webp 格式",
        fields=[
            Field(id="image_path", label="图片目录", type="path", folder=True, file=False),
            Field(id="image", label="或单张图片", type="image"),
            Field(
                id="image_format",
                label="输出格式 (大小: png>jpg>webp, 质量: webp>png>jpg)",
                type="radio",
                options=["jpg", "png", "webp"],
                default="png",
            ),
        ],
        actions=[
            Action(
                id="compress",
                label="🗜️ 仅压缩",
                uses_novelai=False,
                inputs=["image_format", "image_path", "image"],
                # 返回 {message, images}: 前端在输出区直接展示压缩后的图片
                handler=lambda v: image_compression(v.get("image_format", "png"), [v.get("image"), v.get("image_path")]),
            ),
            Action(
                id="organize",
                label="📂 仅整理",
                uses_novelai=False,
                inputs=["image_format", "image_path", "image"],
                # 返回 {message, dir}: 前端在输出区显示完成消息 + 打开保存目录按钮
                handler=lambda v: image_organization(v.get("image_format", "png"), [v.get("image"), v.get("image_path")], False),
            ),
            Action(
                id="compress_organize",
                label="🗜️📂 压缩并整理",
                uses_novelai=False,
                inputs=["image_format", "image_path", "image"],
                handler=lambda v: image_organization(v.get("image_format", "png"), [v.get("image"), v.get("image_path")], True),
            ),
        ],
    )
    plugin.title = "压缩整理"
    plugin.description = "批量压缩并整理图片元数据"
    plugin.icon = "🗜️"
    plugin.panels.append(panel)