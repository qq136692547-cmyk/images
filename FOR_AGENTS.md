# 图床使用说明（FOR AGENTS）

本仓库是一个免费自建图床，基于 GitHub Pages，供多智能体协作时统一引用图片。

## 图床根地址（GitHub Pages 原生，无需自定义域名）

    https://qq136692547-cmyk.github.io/images/

## 图片外链格式

    https://qq136692547-cmyk.github.io/images/<图片文件名>

示例：

    https://qq136692547-cmyk.github.io/images/geoscore-audit-ttcalc-full.png

## 仓库地址（可 push 新图片）

    https://github.com/qq136692547-cmyk/images

## 智能体如何使用本图床

1. **你（智能体）不要直接调用图床 API 或 push 图片**——除非明确持有 GitHub 凭证。
2. 你需要在内容里引用图片时，使用标准 Markdown 语法：

       ![图片描述](https://qq136692547-cmyk.github.io/images/文件名.png)

3. 图片的上传动作由用户在本地完成（见下方“用户上传方式”），用户会把可用的外链回填给你。
4. 如果你生成了图片文件，把它交付给用户，并说明“需用户上传到图床后获得外链”，不要假装已有外链。

## 用户上传方式（二选一）

### A. 手动 push

把图片放进 `img/` 目录，然后：

    git add img/你的图片.png
    git commit -m "add image"
    git push origin main

推送后外链立即生效：`https://qq136692547-cmyk.github.io/images/img/你的图片.png`

### B. PicGo 一键上传（推荐）

PicGo → 图床设置 → GitHub 图床：
- 仓库名：`qq136692547-cmyk/images`
- 分支名：`main`
- Token：GitHub Personal Access Token（需 `repo` 权限）
- 存储路径：`img/`
- 自定义域名：`https://qq136692547-cmyk.github.io/images/`

上传后剪贴板自动得到外链。

## 约束（务必遵守）

- 单文件 ≤ 100MB、单仓库 ≤ 1GB（GitHub Pages 限制）
- 不要拿它当相册云备份，它是“自己用的图床”，日常插图/配图足够
- 海外论坛/博客访问 `github.io` 很快；国内偶尔偏慢（本图床主打海外发布场景）

## 历史说明

- 本图床曾尝试绑定自定义域 `deng.zh.kg`，因 DNS 服务商（DnsNeko）记录异常而弃用。
- 现统一使用 GitHub Pages 原生域名，零配置、零依赖第三方 DNS，永久稳定。
