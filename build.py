import markdown

data = open("index.md").read()

html_content = markdown.markdown(data)

with open("index.html", "w") as g:
    g.write(html_content)