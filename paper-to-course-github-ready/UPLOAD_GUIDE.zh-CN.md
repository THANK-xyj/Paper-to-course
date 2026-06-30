# GitHub 上传指南（中文）

这是给第一次上传 GitHub 的简单流程。

## 方式 A：用 GitHub 网页上传

1. 打开 https://github.com/new
2. 仓库名建议：

```text
paper-to-course
```

3. 选择 `Public` 或 `Private`。
4. 不要勾选添加 README、license 或 `.gitignore`，因为这个文件夹里已经有这些说明文件。
5. 点击 `Create repository`。
6. 进入新仓库后，选择 `uploading an existing file`。
7. 把这个文件夹里的所有文件拖进去：

```text
/Users/xieyujie/Documents/Red book/paper-to-course-github-ready
```

8. 点击提交上传。

## 方式 B：用 Git 命令上传

先在 GitHub 上创建一个空仓库，然后在终端运行：

```bash
cd "/Users/xieyujie/Documents/Red book/paper-to-course-github-ready"
git init
git add .
git commit -m "Initial paper-to-course prototype"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/paper-to-course.git
git push -u origin main
```

把 `YOUR_USERNAME` 换成你的 GitHub 用户名。

## 开启 GitHub Pages

1. 打开你的 GitHub 仓库页面。
2. 进入 `Settings -> Pages`。
3. 在 `Build and deployment` 里选择：

```text
Source: Deploy from a branch
Branch: main
Folder: /docs
```

4. 点击保存。
5. GitHub 构建完成后会给你一个网站地址。
6. 根地址会打开语言选择页。两个课程直达地址通常是：

```text
https://YOUR_USERNAME.github.io/paper-to-course/zh/
https://YOUR_USERNAME.github.io/paper-to-course/en/
```

## 推荐仓库简介

```text
Turn research papers into interactive browser-based courses.
```

## 推荐 README 标语

```text
An experimental paper-reading workflow inspired by Codebase-to-Course.
```

## 上传前检查

确认这些文件存在：

```text
README.md
ACKNOWLEDGEMENTS.md
NOTICE.md
docs/index.html
docs/zh/index.html
docs/en/index.html
skills/paper-to-course/SKILL.md
```

## 小提醒

这个项目里包含从 TimeGrad 论文中截取的图表，适合作为教育 demo。如果你之后想做更正式的公开项目，可以考虑把论文图表替换成自己重绘的示意图。
