# slidev
* Making presentation/slides from markdown file (.md).

## Install
### Mac
1. Install node and npm (if not): `brew install node`
2. Install slidev globally: `npm i -g @slidev/cli`

## Slidev usage
* Make slides from "test.md": `slidev test.md`
* Make pdf file from "test.md": `slidev export test.md`

## Markdown syntax
```markdown
---
theme: your-favorite-theme
---

# first slide

<v-clicks>

## topic 1
* The tabs are shown each line by clicking
* In the browser mode

</v-clicks>

---

# second slide

```

## Theme
* `theme: apple-basic`
* `theme: light-icons`
* `theme: unicorn`

## VS-code
* You can use "Simple Browser" (default VS code functional) to see the slide: Alt + Shift + p then Simple Browser.

## Export
* pdf file: `slidev export your_file.md`
* pptx file: `slidev export --format pptx your_file.md`
