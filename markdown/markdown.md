# Basic Markdown Writing Guide
* Markdown is a simple and readable text formatting syntax. Here's a guide to the basic elements.
* **Using Markdown is strongly recommended**  to write any document. Converting a markdown file to html, pdf, Word doc file, slide file, ppt file is all possible.

## Headers

```markdown
# Header 1
## Header 2
### Header 3
```

## Text Formatting

```markdown
*Italic* or _italic_
**Bold** or __bold__
~~Strikethrough~~
```

## Lists

### Unordered Lists

```markdown
- Item 1
- Item 2
  - Sub-item 1
  - Sub-item 2
```

### Ordered Lists

```markdown
1. First item
2. Second item
3. Third item
```

## Links

```markdown
[Display text](URL)
Example: [Google](https://www.google.com)
```

## Images
* Markdown-specific way

```markdown
![Alt text](image URL)
Example: ![Logo](./images/logo.png)
```

* HTML way

```markdown
<img src="./images/logo.png" width=100%>
```

  - HTML way is recommended as you can control the size.

## Blockquotes
```markdown
> This is a blockquote
> It can span multiple lines
```

## Code
### Inline Code

```markdown
`some code`
```

### Code Blocks

````markdown
```python
def hello():
    print("Hello, World!")
```
````

## Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| A1       | B1       | C1       |
| A2       | B2       | C2       |
```

## Horizontal Rules

```markdown
---
or
***
or
___
```

## Task Lists

```markdown
- [ ] Uncompleted task
- [x] Completed task
```

* These are the basic elements of Markdown. By combining these elements, you can create well-structured and readable documents.

## Recommended tools for markdown
### VS Code plugin
* Markdown preview enhanced: for previewing markdown

### Node.js
* slidev: making slides from markdown
