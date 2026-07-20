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

### B. PicGo 一键上传（推荐，图文步骤）

> 适用场景：日常写博客/发论坛，拖图即传、自动得外链，不用碰 git 命令。

#### 步骤 1：下载并安装 PicGo

- 官网：https://picgo.github.io/PicGo-Doc/ （或 GitHub  releases：`Molunerfinn/PicGo`）
- 支持 Windows / macOS / Linux，按系统下载安装包，一路下一步安装。
- 打开后常驻系统托盘（任务栏右下角）。

> 图示说明（无截图，按文字操作即可）：主界面左侧为「图床设置 / 上传区 / 相册」，顶部为拖拽上传区。

#### 步骤 2：准备 GitHub Token（只需做一次）

1. 打开 https://github.com/settings/tokens?type=beta （或 头像 → Settings → Developer settings → Personal access tokens → Tokens (classic)）
2. 点 **Generate new token**（选 classic 最稳）
3. Note 填 `picgo-imgbed`，Expiration 按需（建议选 90 天或 No expiration 仅自用）
4. 勾选 **`repo`**（全勾 repo 那一组即可，给仓库读写权限）
5. 点 Generate token，**立刻复制那一长串 `ghp_...`**（只显示一次！）

> ⚠️ Token 等同你账号密码，只存本地 PicGo，不要发给别人或提交到仓库。

#### 步骤 3：配置 GitHub 图床

1. 打开 PicGo → 左侧 **图床设置** → 选 **GitHub 图床**
2. 按图填写：

   | 字段 | 填写值 |
   |---|---|
   | 仓库名 | `qq136692547-cmyk/images` |
   | 分支名 | `main` |
   | Token | 步骤 2 复制的 `ghp_...` |
   | 存储路径 | `img/` （结尾带斜杠）|
   | 自定义域名 | `https://qq136692547-cmyk.github.io/images/` （结尾带斜杠）|

3. 点 **确定** 保存。

> 图示说明（无截图，按上表填写即可）：GitHub 图床配置页共 5 个输入框，依次对应上表「字段 / 填写值」。

#### 步骤 4：设为默认图床并测试

1. PicGo 左侧 **图床设置** 顶部「设置为默认图床」选 **GitHub 图床**。
2. 拖一张图片到 PicGo 主界面上传区，或点「上传区」选择文件。
3. 上传成功 → 外链自动复制到剪贴板，格式即：

       https://qq136692547-cmyk.github.io/images/img/你的图片.png

4. 打开该链接确认能显示（GitHub Pages 构建约 1 分钟生效）。

> 图示说明（无截图）：上传成功后 PicGo 相册列表会出现该图，鼠标悬停可复制「GitHub 外链」。

#### 步骤 5（可选）：Typora / 写作软件联动

- Typora：偏好设置 → 图像 → 上传服务选「PicGo (app)」→ 上传时自动传图床并替换本地路径。
- 任何 Markdown 编辑器粘贴图片即可自动变外链，写博客插图零摩擦。

#### 常见问题

- **上传失败 / 401**：Token 没勾 `repo`，或复制时被截断。重做步骤 2。
- **外链打不开 / 404**：等 1 分钟让 GitHub Pages 重新构建；确认存储路径和自定义域名结尾都带 `/`。
- **国内偶尔慢**：本图床主打海外场景，`github.io` 国内偶偏慢属正常，不影响海外论坛/博客。

## 约束（务必遵守）

- 单文件 ≤ 100MB、单仓库 ≤ 1GB（GitHub Pages 限制）
- 不要拿它当相册云备份，它是“自己用的图床”，日常插图/配图足够
- 海外论坛/博客访问 `github.io` 很快；国内偶尔偏慢（本图床主打海外发布场景）

## 历史说明

- 本图床曾尝试绑定自定义域 `deng.zh.kg`，因 DNS 服务商（DnsNeko）记录异常而弃用。
- 现统一使用 GitHub Pages 原生域名，零配置、零依赖第三方 DNS，永久稳定。
