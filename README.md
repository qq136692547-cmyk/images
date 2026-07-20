# images — 免费自建图床

基于 GitHub Pages 的零成本图床。图床根地址：

    https://qq136692547-cmyk.github.io/images/

图片外链格式：`https://qq136692547-cmyk.github.io/images/<文件名>`

- 新图片放 `img/` 目录，push 后外链即生效
- 推荐用 PicGo（GitHub 图床插件）一键上传，自定义域名填 `https://qq136692547-cmyk.github.io/images/`
- 约束：单文件 ≤100MB、单仓库 ≤1GB
- 智能体协作用法、PicGo 完整图文配置步骤见 `FOR_AGENTS.md`

### PicGo 快速配置（详细见 FOR_AGENTS.md）

1. 装 PicGo（https://picgo.github.io/PicGo-Doc/）
2. GitHub 生成 Token：Settings → Developer settings → PAT(classic)，勾 `repo`
3. PicGo → 图床设置 → GitHub 图床：
   - 仓库名：`qq136692547-cmyk/images`
   - 分支：`main`
   - Token：上面的 `ghp_...`
   - 存储路径：`img/`
   - 自定义域名：`https://qq136692547-cmyk.github.io/images/`
4. 设为默认图床，拖图上传，外链自动复制

> 注：曾尝试自定义域 `deng.zh.kg`（DnsNeko 提供），因 DNS 记录异常弃用，现用原生 github.io 域名。
