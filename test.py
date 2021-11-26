import os


def generate_tree(path, html=""):
    for file in os.listdir(path):
        rel = path + "/" + file
        try:
            if os.path.isdir(rel):
                html += "<li class='toggle'><a href='#'>{}</a></li><li class='child' hidden='False'>".format(file)
                html += generate_tree(rel)
                html += "</li>"
            else:
                html += "<li><a href='#'>{}</a></li>".format(file)
        except:
            pass
    return html


html = "<ul>"
html = generate_tree("D:\\", html)
html = html + "</ul>"
print(html)
