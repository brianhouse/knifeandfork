#!/usr/local/bin/python3

import os, yaml, markdown, jinja2

directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "content"))

projects = []
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as f:
        project = yaml.safe_load(f)
        if 'text' in project:
            project['text'] = markdown.markdown(project['text'].strip())
        projects.append(project)

projects.sort(key=lambda project: int(project['year']))
projects.reverse()

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html")), 'w') as f:
    template = os.path.join(os.path.dirname(__file__), "template.html")
    renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(".")).get_template(template)
    output = renderer.render({'projects': projects})
    f.write(output)
