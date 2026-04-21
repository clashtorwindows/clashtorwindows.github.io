# Manus News - 专为新闻资讯打造的 SEO 优先 Jekyll 主题

Manus News 是一个高性能、深度 SEO 优化的 Jekyll 主题，专为新闻媒体、科技资讯和个人博客设计。它集成了现代搜索引擎所需的一切优化措施。

## 核心特性

- **🚀 极致 SEO 优化**：内置 TDK (Title, Description, Keywords) 自定义设置。
- **📱 社交媒体友好**：完整支持 Open Graph (OG) 标签和 Twitter Card。
- **📊 结构化数据**：自动生成符合 Schema.org 标准的 `NewsArticle` JSON-LD 数据。
- **⚡ IndexNow 自动推送**：支持向 Bing 和 Yandex 实时推送新内容。
- **📱 响应式设计**：适配所有移动设备和桌面浏览器。
- **🔗 增强内链**：内置相关文章推荐和社交分享组件。
- **📄 符合标准**：自动生成 Sitemap.xml、RSS Feed 和 robots.txt。

## 安装说明

1.  将此主题目录下的文件复制到您的 Jekyll 根目录。
2.  在 `Gemfile` 中添加必要的插件：
    ```ruby
    group :jekyll_plugins do
      gem "jekyll-feed"
      gem "jekyll-sitemap"
      gem "jekyll-seo-tag"
      gem "jekyll-paginate"
    end
    ```
3.  运行 `bundle install`。

## 配置指南 (`_config.yml`)

在 `_config.yml` 中配置您的站点信息：

```yaml
title: "您的站点名称"
description: "您的站点描述（用于首页 SEO）"
url: "https://yourdomain.com"
author: "作者名称"

# IndexNow 配置
indexnow:
  enabled: true
  endpoint: "https://api.indexnow.org/indexnow"
  key: "您的_INDEXNOW_KEY"
  key_location: "https://yourdomain.com/您的_INDEXNOW_KEY.txt"
```

## SEO 使用建议

在撰写文章（Front Matter）时，请务必填写以下字段以获得最佳 SEO 效果：

```markdown
---
layout: post
title: "文章标题"
description: "文章描述（用于搜索结果摘要，建议 120-160 字）"
keywords: [关键词1, 关键词2]
image: "/assets/images/cover.jpg" # 社交媒体分享时的预览图
---
```

## IndexNow 推送

主题附带 `indexnow.py` 脚本。在站点构建完成后，运行以下命令即可将新内容推送至 Bing 等搜索引擎：

```bash
python3 indexnow.py
```

## 许可证

MIT License.
