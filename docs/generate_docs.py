import os
from jinja2 import Template
import yaml


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WRAPPER_DIR = os.path.dirname(BASE_DIR)
OUTPUT_DIR = os.path.join(BASE_DIR, "wrappers")
SCRIPTS = {"wrapper.py", "wrapper.R"}
BLACKLIST = {"docs", "environment.yaml", ".git", ".gitignore", "README.md"} | SCRIPTS

with open(os.path.join(BASE_DIR, "_templates", "tool.rst")) as f:
    TOOL_TEMPLATE = Template(f.read())

with open(os.path.join(BASE_DIR, "_templates", "wrapper.rst")) as f:
    TEMPLATE = Template(f.read())


def get_tool_dir(tool):
    outdir = os.path.join(OUTPUT_DIR, tool)
    os.makedirs(outdir, exist_ok=True)
    return outdir



def render_wrapper(path, tool):
    with open(os.path.join(path, "meta.yaml")) as meta:
        meta = yaml.load(meta)
    with open(os.path.join(path, "Snakefile")) as snakefile:
        snakefile = snakefile.read()
    name = meta["name"].replace(" ", "_") + ".rst"
    with open(os.path.join(get_tool_dir(tool), name), "w") as readme:
        rst = TEMPLATE.render(snakefile=snakefile, **meta)
        readme.write(rst)
    return name


def setup(*args):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tools = []
    for discipline in os.listdir(WRAPPER_DIR):
        if discipline in BLACKLIST:
            continue
        for tool in os.listdir(os.path.join(WRAPPER_DIR, discipline)):
            tools.append(tool)
            path = os.path.join(WRAPPER_DIR, discipline, tool)
            if any(f in SCRIPTS for f in os.listdir(path)):
                render_wrapper(path, tool)
                continue
            for subcommand in os.listdir(path):
                render_wrapper(os.path.join(path, subcommand), tool)
    with open(os.path.join(BASE_DIR, "_templates", "index.rst")) as f:
        index = Template(f.read()).render(tools=tools)
    with open(os.path.join(BASE_DIR, "index.rst"), "w") as f:
        f.write(index)


if __name__ == '__main__':
    setup()
