import markdown

with open("templates/template.html") as t:
    template = t.read()

with open("index.md") as f:
    data = f.read()

html_data = markdown.markdown(data)
formatted_page = template.replace("../stylesheets/style.css", "stylesheets/style.css").replace("%CONTENT%", html_data)

with open("index.html", "w") as g:
    g.write(formatted_page)