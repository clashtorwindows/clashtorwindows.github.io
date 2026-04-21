---
layout: default
title: 最新文章
permalink: /articles/
---

<section class="section bg-light">
  <div class="container">
    <h1 class="section-title">最新文章</h1>
    <p class="section-subtitle">探索 Clash for Windows、Shadowrocket Windows 的最新动态、使用技巧与配置指南</p>
    
    <div class="articles-grid">
      {% for post in site.posts %}
        <article class="article-card">
          <div class="article-category">{{ post.categories | first | default: "技术指南" }}</div>
          <h3 class="article-title">
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          </h3>
          <p class="article-excerpt">
            {% if post.description and post.description != "" %}
              {{ post.description | strip_html | truncate: 120 }}
            {% else %}
              {{ post.content | strip_html | truncate: 120 }}
            {% endif %}
          </p>
          <div class="article-meta">
            <span class="article-date">{{ post.date | date: "%Y-%m-%d" }}</span>
            <a href="{{ post.url | relative_url }}" class="article-link">阅读全文 →</a>
          </div>
        </article>
      {% endfor %}
    </div>
  </div>
</section>

<style>
.section {
  padding: 60px 20px;
}

.section.bg-light {
  background-color: #f8f9fa;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-title {
  font-size: 36px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.section-subtitle {
  font-size: 18px;
  text-align: center;
  color: #666;
  margin-bottom: 40px;
}

.articles-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 30px;
  margin-top: 40px;
}

.article-card {
  background: white;
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.article-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
}

.article-category {
  display: inline-block;
  background-color: #e8eaf6;
  color: #667eea;
  padding: 5px 12px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  margin-bottom: 12px;
}

.article-title {
  font-size: 18px;
  margin-bottom: 12px;
}

.article-title a {
  color: #333;
  text-decoration: none;
  transition: color 0.3s ease;
}

.article-title a:hover {
  color: #667eea;
}

.article-excerpt {
  color: #666;
  font-size: 14px;
  line-height: 1.6;
  margin-bottom: 15px;
}

.article-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 13px;
  color: #999;
}

.article-link {
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s ease;
}

.article-link:hover {
  color: #5568d3;
}

@media (max-width: 768px) {
  .section-title {
    font-size: 28px;
  }
  
  .articles-grid {
    grid-template-columns: 1fr;
  }
}
</style>
