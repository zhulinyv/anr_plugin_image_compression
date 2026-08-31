# 🗜️ 图片压缩整理插件 (anr_plugin_image_compression)

[Auto-NovelAI-Refactor](https://github.com/zhulinyv/Auto-NovelAI-Refactor) 的图片压缩整理插件, 使用 opencv 与 pillow 对图片进行批量压缩, 并支持将图片整理为带完整生成参数的 Excel 表格。

## ✨ 功能特性

- 🗜️ **批量压缩**: 支持 jpg / png / webp 三种输出格式, 智能处理透明通道
- 📂 **Excel 整理**: 将图片连同正面提示词、负面提示词、分辨率、采样步数、相关性、调度器、采样器、sm/sm_dyn、随机种子等元数据整理成表格
- 🖼️ **单张与批量**: 支持单张图片或整个目录批量处理
- 🔄 **三种操作模式**:
  - **仅压缩**: 只压缩图片, 前端直接展示结果
  - **仅整理**: 只生成 Excel 表格, 不改变原图
  - **压缩并整理**: 先压缩再整理, 表格内插入压缩后的图片

## 📦 依赖

- openpyxl
- opencv-python (cv2)
- pillow

## 🚀 使用方法

1. 在 [Auto-NovelAI-Refactor](https://github.com/zhulinyv/Auto-NovelAI-Refactor) 的插件商店中安装本插件
2. 打开「压缩整理」面板
3. 选择「图片目录」或「单张图片」
4. 选择输出格式 (大小: png > jpg > webp, 质量: webp > png > jpg)
5. 点击对应按钮执行操作

## 🗂️ Excel 表格列说明

| 列 | 说明 |
| --- | --- |
| 图片 | 插入的图片预览 |
| 正面/负面提示词 | 生成时的提示词 (从图片元数据读取) |
| 分辨率 / 采样步数 / 提示词相关性 | 生成参数 |
| 调度器 / 采样器 | 生成参数 |
| sm / sm_dyn / variety / decrisp | 模型增强选项 |
| 随机种子 | 生成种子 |
