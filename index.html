---
layout: default
title: "首页"
---

<div class="home">
  {%- if page.title -%}
    <h1 class="page-heading">{{ page.title }}</h1>
  {%- endif -%}

  {{ content }}

  {% if site.paginate %}
    {% assign posts = paginator.posts %}
  {% else %}
    {% assign posts = site.posts %}
  {% endif %}

  {%- if posts.size > 0 -%}
    <ul class="post-list">
      {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
      {%- for post in posts -%}
      <li>
        <span class="post-meta">{{ post.date | date: date_format }}</span>
        <h3>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
        </h3>
        {%- if site.show_excerpts -%}
          {{ post.excerpt }}
        {%- endif -%}
      </li>
      {%- endfor -%}
    </ul>

    {% if site.paginate %}
      <div class="pagination">
        {% if paginator.previous_page %}
          <a href="{{ paginator.previous_page_path | relative_url }}" class="previous">上一页</a>
        {% else %}
          <span class="previous">上一页</span>
        {% endif %}
        <span class="page_number ">第 {{ paginator.page }} 页，共 {{ paginator.total_pages }} 页</span>
        {% if paginator.next_page %}
          <a href="{{ paginator.next_page_path | relative_url }}" class="next">下一页</a>
        {% else %}
          <span class="next">下一页</span>
        {% endif %}
      </div>
    {% endif %}

  {%- endif -%}
</div>

<style>
.post-list {
  list-style: none;
  padding: 0;
}
.post-list li {
  margin-bottom: 30px;
  border-bottom: 1px solid #eee;
  padding-bottom: 20px;
}
.post-list li h3 {
  margin-top: 5px;
  font-size: 24px;
}
.post-list li a {
  text-decoration: none;
  color: #2a7ae2;
}
.post-list li a:hover {
  text-decoration: underline;
}
.post-meta {
  font-size: 14px;
  color: #828282;
}
.pagination {
  margin-top: 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.pagination a, .pagination span {
  padding: 8px 16px;
  border: 1px solid #ddd;
  border-radius: 4px;
  text-decoration: none;
}
.pagination a:hover {
  background-color: #f5f5f5;
}
</style>
