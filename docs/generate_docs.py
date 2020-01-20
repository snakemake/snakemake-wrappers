import os
import textwrap
from jinja2 import Template
import yaml
import subprocess

DISCIPLINES = ["bio", "utils"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WRAPPER_DIR = os.path.dirname(BASE_DIR)
OUTPUT_DIR = os.path.join(BASE_DIR, "wrappers")
SCRIPTS = {"wrapper.py", "wrapper.R"}
BLACKLIST = {".snakemake", ".circleci", "wercker.yml", "docs", "__pycache__", "environment.yaml", ".git", ".gitignore", "README.md", ".cache", "__init__.py", "test.py", ".pytest_cache"} | SCRIPTS
TAG = subprocess.check_output(["git", "describe", "--tags"]).decode().strip()


with open(os.path.join(BASE_DIR, "_templates", "tool.rst")) as f:
    TOOL_TEMPLATE = Template(f.read())

with open(os.path.join(BASE_DIR, "_templates", "wrapper.rst")) as f:
    TEMPLATE = Template(f.read())


def get_tool_dir(tool):
    outdir = os.path.join(OUTPUT_DIR, tool)
    os.makedirs(outdir, exist_ok=True)
    return outdir


def render_tool(tool, subcmds):
    if '' in subcmds:
        raise NotImplementedError(  'You are trying to render the tool "', tool,
                                    '" for subcommands "', subcmds,
                                    '". The empty subcommand \'\' indicates that both the main command, as well ',
                                    'as the subcommand(s) have wrappers. This case requires a Template hybrid ',
                                    'between wrapper.rst and tool.rst that has not been implemented.')
    with open(os.path.join(get_tool_dir(tool) + ".rst"), "w") as f:
        f.write(TOOL_TEMPLATE.render(name=tool))


def render_wrapper(path, target):
    print("rendering", path)
    with open(os.path.join(path, "meta.yaml")) as meta:
        meta = yaml.load(meta)

    envpath = os.path.join(path, "environment.yaml")
    if os.path.exists(envpath):
        with open(envpath) as env:
            env = yaml.load(env)
            pkgs = env["dependencies"]
    else:
        pkgs = []

    with open(os.path.join(path, "test", "Snakefile")) as snakefile:
        snakefile = textwrap.indent(snakefile.read(), "    ").replace("master", TAG)

    wrapper = os.path.join(path, "wrapper.py")
    wrapper_lang = "python"
    if not os.path.exists(wrapper):
        wrapper = os.path.join(path, "wrapper.R")
        wrapper_lang = "R"
    with open(wrapper) as wrapper:
        wrapper = textwrap.indent(wrapper.read(), "    ")

    name = meta["name"].replace(" ", "_") + ".rst"
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w") as readme:
        rst = TEMPLATE.render(snakefile=snakefile, wrapper=wrapper, wrapper_lang=wrapper_lang, pkgs=pkgs, **meta)
        readme.write(rst)
    return name


def setup(*args):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for discipline in DISCIPLINES:
        for tool in os.listdir(os.path.join(WRAPPER_DIR, discipline)):
            if tool in BLACKLIST:
                continue
            subcmds = []
            max_depth = 1
            path = os.path.join(WRAPPER_DIR, discipline, tool)
            for dirpath, dirnames, filenames in os.walk(path):
                if any(f in SCRIPTS for f in filenames):
                    # split up paths including SCRIPTS on the displine and strip tool from start
                    tool_levels = dirpath.rpartition(os.sep.join( ["", discipline, ""] ) )[2].split(sep = os.sep)
                    tool_levels.remove(tool)
                    if len(tool_levels) == 0:
                        continue
                    if any(l in BLACKLIST for l in tool_levels):
                        continue
                    subcommand = os.sep.join(tool_levels)
                    subcmds.append(subcommand)
                    # watermark max_depth for current tool
                    max_depth = max(max_depth, len(tool_levels))
                    render_wrapper(dirpath, os.path.join(get_tool_dir(tool), subcommand + ".rst"))
            if len(subcmds) == 0:
                # no subcommands, render a wrapper for the main tool command
                render_wrapper(path, os.path.join(OUTPUT_DIR, tool + ".rst"))
            else:
                # subcommands found (and rendered above), render the tool's table of content
                render_tool(tool, subcmds)


if __name__ == '__main__':
    setup()
