# Introduction
* Honkit is the fork of GitBook, and it generates the document pages.
* https://honkit.netlify.app/
* Now GitBook is not free and its command-line interface (cli) is no longer developed.

# Usage
1. Installing Honkit
* Install Node.js (if not): `brew install node`
* Install honkit
```bash
npm install honkit --save-dev
```

2. Setting up poject
* Make project directory and cd there, then
```bash
mkdir mybook
cd mybook
```

3. Make initial file
* Making initial configuration file for Honkit
```bash
npx honkit init
```
* This will yield `README.md` and `SUMMARY.md`

4. Add contents
* Edit `README.md` and `SUMMARY.md` to add contents.
* An example of `SUMMARY.md` is
  + Using single directory
  ```markdown
  # Summary
  * [Introduction](README.md)
  * [Part1](part1.md)
  * [Part2](part2.md)
  ```
  + Using multiple directories
  ```markdown
  # Summary
  * [Introduction](README.md)
  * [Chapter 1](chapter1/README.md)
    * [Contents of Chapter 1](chapter1/contents.md)
  * [Chapter 2](chapter2.md)
    * [Contents of Chapter 2](chapter2/contents.md)
  ```

5. Preview with localhost
* You can check webpage with following command
```bash
npx honkit serve
```
* Accessing http://localhost:4000 with browser will show the contents.

# Installing plugin
* Plugins can be found in https://www.npmjs.com/
* Install command is also there.
* Some plugins have Honkit and GitBook versions. Use Honkit version when available, but GitBook version also works.
* Useful plugins
  + `npm install -g gitbook-plugin-hide-published-with`
  + `npm install -g honkit-plugin-katex`
  + `npm install -g gitbook-plugin-katex-mhchem`
  + `npm install -g gitbook-plugin-mathjax`

# Setting `book.json`
* HTML settings should be written in `book.json`.
* Basic format:

```
{
    "plugins":["hide-published-with"]
}
```

## Code highlighting
* Use "prism" if you want to change highligts: `{"plugins": ["prism", "-highlight"]}`

## Deleting "Published with Honkit"
* You can delete "Published with Honkit" in the sidebar: `{"plugins": ["hide-published-with"]}`

## Math
* mathjax: `{"plugins": ["mathjax"]}` (doesn't work?)
* katex: `{"plugins": ["katex"]}`
* katex + mhchem: `{"plugins: ["katex-mhchem"]}`

---

# Publish on the web
1. Initializing the project
* Make project directory in your local environment, and initialize the git repository.
```bash
mkdir mybook
cd mybook
git init
```

2. Setting up Honkit project
* Set up the Honkit project and build HTML.
```bash
npx honkit init
npx honkit build . docs
```

3. Commiting files
* Add all changes and commit.
```bash
git add .
git commit -m "Initial commit"
```

4. Push to remote repository
* Add remote repository, and push the changes in the local.
```bash
git remote add origin https://github.com/your_name/mybook.git
git push -u origin main
```

5. Setting up GitHub Pages
* Go to "Setting" in GitHub repository then find "GitHub Pages" section.
* Set "main" "/docs" to the "Source".

6. Confirming public URL
* When setting is done, URL of GitHub Pages will appear.
* Accessing URL will show the HTML files in the `docs` directory.
* Use Github Pages URL to "About".

## Update the revision
1. `npx honkit {your_document_directories} docs`
2. `git add .`; `git commit -m "updated document"`; `git push`
* The document directories should contain `README.md`, `SUMMARY.md`, and `book.json`. Markdown files can be separate directries.

## References
* https://www.1ft-seabass.jp/memo/2022/12/06/honkit-setting-202212/
* https://mebiusbox.github.io/contents/gitbook/

## Why I didn't choose other documentation services
* GitBook: No CLI. Web service only.
* Fern: Good looking but no free plan.
* Hugo: Good looking but latex math is not easy to use.
* Jekyll: Too complicated.
* MkDocs: Easy to use but latex math is not good (mathjax only).
* Gatsby: Good looking but too complicated.
* Other services on https://dev.to/ismailkamil/top-10-api-documentation-tools-in-2025-with-doc-examples-3pe4: mostly web-service so no CLIs.