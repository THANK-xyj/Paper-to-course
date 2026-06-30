# GitHub Upload Guide (English)

This is a simple upload path if you have never published a GitHub repository before.

## Option A: Upload Through The GitHub Website

1. Go to https://github.com/new
2. Suggested repository name:

```text
paper-to-course
```

3. Choose `Public` or `Private`.
4. Do not add a README, license, or `.gitignore` on GitHub, because this folder already includes the relevant files.
5. Click `Create repository`.
6. On the new repository page, choose `uploading an existing file`.
7. Drag all files from this folder into GitHub:

```text
/Users/xieyujie/Documents/Red book/paper-to-course-github-ready
```

8. Commit the upload.

## Option B: Upload With Git

Create a new empty GitHub repository first, then run:

```bash
cd "/Users/xieyujie/Documents/Red book/paper-to-course-github-ready"
git init
git add .
git commit -m "Initial paper-to-course prototype"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/paper-to-course.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Enable GitHub Pages

1. Open your GitHub repository.
2. Go to `Settings -> Pages`.
3. Under `Build and deployment`, choose:

```text
Source: Deploy from a branch
Branch: main
Folder: /docs
```

4. Save the setting.
5. GitHub will provide a website URL after the build finishes.
6. The root Pages URL opens a language selector. The direct course URLs are usually:

```text
https://YOUR_USERNAME.github.io/paper-to-course/zh/
https://YOUR_USERNAME.github.io/paper-to-course/en/
```

## Suggested Repository Description

```text
Turn research papers into interactive browser-based courses.
```

## Suggested README Tagline

```text
An experimental paper-reading workflow inspired by Codebase-to-Course.
```

## Pre-Upload Checklist

Make sure these files exist:

```text
README.md
ACKNOWLEDGEMENTS.md
NOTICE.md
docs/index.html
docs/zh/index.html
docs/en/index.html
skills/paper-to-course/SKILL.md
```

## Note

This project includes figures extracted from the TimeGrad paper for educational demonstration. For a more formal public release, consider replacing paper figures with your own redrawn diagrams.
