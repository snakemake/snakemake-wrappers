import os
from jinja2 import Template
import yaml


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WRAPPER_DIR = os.path.dirname(BASE_DIR)
OUTPUT_DIR = os.path.join(BASE_DIR, "wrappers")
SCRIPTS = {"wrapper.py", "wrapper.R"}
BLACKLIST = {"docs", "environment.yaml", ".git", "README.md"} | SCRIPTS
TEMPLATE = Template(os.path.join(BASE_DIR, "_templates", "wrapper.rst"))



def render_wrapper(path):
    with open(os.path.join(path, "meta.yaml")) as meta:
        meta = yaml.load(meta)
    with open(os.path.join(path, "Snakefile")) as snakefile:
        snakefile = snakefile.read()    
    with open(os.path.join(OUTPUT_DIR, "wrappers"), "w") as readme:
        readme.write(TEMPLATE.render(snakefile=snakefile, **meta))


def setup(*args):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for discipline in os.listdir(WRAPPER_DIR):
        if discipline in BLACKLIST:
            continue
        for tool in os.listdir(os.path.join(WRAPPER_DIR, discipline)):
            path = os.path.join(WRAPPER_DIR, discipline, tool)
            if any(f in SCRIPTS for f in os.listdir(path)):
                render_wrapper(path)
                continue
            for subcommand in os.listdir(path):
                render_wrapper(os.path.join(path, subcommand))


if __name__ == '__main__':
    setup()
