# Paper-to-Course

> 将研究论文转换成可交互的浏览器学习课程。  
> Turn research papers into interactive browser-based learning courses.

## 致谢与来源 / Acknowledgement

这个项目的交互课程形式、前端视觉风格和部分交互组件，参考并改编自 Zara Zhang 的 **Codebase-to-Course**：

https://github.com/zarazhangrui/codebase-to-course

Codebase-to-Course 原本是把代码库转换成互动课程。我在这个优秀形式的基础上，探索了一个新的方向：**Paper-to-Course**，也就是把论文阅读流程转换成互动课程。

需要明确区分：

- 交互课程形式、滚动导航、进度条、translation block、quiz、tooltip、flow animation 等前端课程体验，参考 / 改编自 Zara Zhang 的 Codebase-to-Course。
- 论文阅读流程、TimeGrad 课程内容、中文解释、公式解读、图表阅读、实验审计、复现清单，是这个 paper-to-course 方向中新写的内容。

English:

This project is inspired by and adapts the interactive-course format of Zara Zhang's **Codebase-to-Course**:

https://github.com/zarazhangrui/codebase-to-course

Codebase-to-Course turns codebases into interactive courses. This project explores a related but different direction: turning research papers into interactive paper-reading courses.

The front-end course style and interaction patterns are adapted from Codebase-to-Course. The paper-reading workflow, TimeGrad teaching content, Chinese explanations, paper-specific quizzes, experiment audit, and reproducibility framing are newly created for this Paper-to-Course direction.

## 项目简介 / Overview

Paper-to-Course 是一个实验性 Codex skill / workflow，用来把研究论文 PDF 转换成浏览器里的互动学习课程。

它不是简单总结论文，而是按照读论文的真实路径拆解：

- 论文解决什么问题
- Gap 在哪里
- 核心方法是什么
- 公式和算法怎么理解
- 图表到底在证明什么
- 实验结果是否支撑论文主张
- 复现和迁移时需要注意什么

English:

Paper-to-Course is an experimental Codex skill / workflow for converting academic papers into browser-based study guides.

Instead of summarizing a paper, it teaches the paper as a reasoning path:

- problem
- Gap
- method
- equations and algorithms
- figures and tables
- experiments
- limitations
- reproducibility

## Demo

当前 demo 使用 TimeGrad 论文：

> Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting

打开本地双语 demo：

```bash
open docs/index.html
```

或者启动本地服务：

```bash
cd docs
python3 -m http.server 8768
```

然后访问：

```text
http://127.0.0.1:8768/index.html
```

课程直达：

```text
docs/zh/index.html    # 中文版本
docs/en/index.html    # English version
```

## GitHub Pages

如果发布到 GitHub Pages，设置：

```text
Branch: main
Folder: /docs
```

Pages 根地址会打开语言选择页：

```text
docs/index.html
```

然后可以进入：

```text
/zh/    中文课程
/en/    English course
```

## 项目结构 / Repository Structure

```text
.
├── docs/                     # GitHub Pages demo root
│   ├── index.html             # language selector / 语言选择页
│   ├── zh/                    # Chinese TimeGrad course / 中文课程
│   └── en/                    # English TimeGrad course / 英文课程
├── skills/
│   └── paper-to-course/       # Codex skill prototype
├── ACKNOWLEDGEMENTS.md
├── NOTICE.md
├── POSTING_COPY.md
├── UPLOAD_GUIDE.md
├── UPLOAD_GUIDE.zh-CN.md
└── UPLOAD_GUIDE.en.md
```

## 本项目新增了什么 / What This Project Adds

相比 Codebase-to-Course 面向代码库的课程生成，这个项目新增的是面向论文阅读的 workflow：

- 识别论文的 problem 和 Gap
- 把公式和算法翻译成 plain language
- 把图表当作证据来阅读
- 审计实验设置、baseline、metric 和 ablation
- 区分论文 claim 和实验真正证明的内容
- 生成复现清单和迁移判断清单

English:

Compared with codebase-oriented course generation, this project adds a paper-reading workflow:

- identify the paper's problem and Gap
- translate equations and algorithms into plain language
- read figures and tables as evidence
- audit experiments, baselines, metrics, and ablations
- separate paper claims from what the experiments actually prove
- build reproducibility and transfer checklists

## 安装 Skill / Install The Skill Locally

复制 skill 到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R skills/paper-to-course ~/.codex/skills/paper-to-course
```

然后重启 Codex 或重新加载 skills。

English:

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/paper-to-course ~/.codex/skills/paper-to-course
```

Then restart Codex or reload skills.

## 重新构建 Demo / Rebuild The Demo Courses

```bash
cd docs/zh
bash build.sh

cd ../en
bash build.sh
```

构建方式：

```text
_base.html + modules/*.html + _footer.html -> index.html
```

## 版权与使用说明 / License And Notice

这个仓库目前是 prototype / learning project，不是成熟库。

请在复用或发布 derivative work 前阅读：

- [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md)
- [NOTICE.md](NOTICE.md)

当前仓库整体暂未授予开源许可证。也就是说，在没有进一步明确 license 前，请不要把它当作可自由商用或可任意再授权的模板使用。

English:

This repository is a prototype / learning project, not a polished library.

Before reusing or publishing derivative work, please read:

- [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md)
- [NOTICE.md](NOTICE.md)

No open-source license is currently granted for this repository as a whole. Without a license, do not treat it as a freely reusable commercial or relicensable template.
