#!venv/bin/python

import os, yaml, markdown, jinja2

directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "content"))

projects = []
for filename in sorted(os.listdir(directory)):
    if not filename.endswith((".yaml", ".yml")):
        continue
    with open(os.path.join(directory, filename)) as f:
        project = yaml.safe_load(f)
        if 'text' in project:
            project['text'] = markdown.markdown(project['text'].strip())
        projects.append(project)

projects.sort(key=lambda project: int(project['year']))
projects.reverse()

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html")), 'w') as f:
    base = os.path.dirname(os.path.abspath(__file__))
    renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(base))
    template = renderer.get_template("template.html")
    output = template.render(projects=projects)
    f.write(output)