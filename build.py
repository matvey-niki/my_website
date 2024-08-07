import markdown
import os

with open("templates/template.html") as t:
    template = t.read()

for mdfile in os.scandir("markdown"):
    if mdfile.is_file():
        with open(mdfile.path) as f:
            data = f.read()
        html_data = markdown.markdown(data)
        formatted_page = template.replace("%CONTENT%", html_data)
        with open(f"public/{mdfile.name.removesuffix(".md")}.html", "w") as g:
            g.write(formatted_page)

with open("index.md") as h:
    data = h.read()
html_data = markdown.markdown(data)
formatted_page = template.replace("../", "./").replace("%CONTENT%", html_data)
with open("index.html", "w") as g:
    g.write(formatted_page)