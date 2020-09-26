from snakemake.shell import shell
import os
import cravat
from types import SimpleNamespace
from cravat import cravat_admin

default_ns = SimpleNamespace(
    force_data=False,
    skip_installed=True,
    yes=True,
    private=False,
    skip_dependencies=False,
    force=False,
    skip_data=False
)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
args = snakemake.params.get('options', [])
sysconf = cravat.admin_util.get_system_conf()
modules_dir = sysconf.get('modules_dir')
kwargs = {}
for k, v in snakemake.params.items():
    if k == 'args':
        continue
    if k == 'annotators' or k == 'reports':
        kwargs[k] = []
        for mv in v:
            if '=' in mv:
                module, version = mv.split('=')
            else:
                module = mv
                version = None
            if k == 'reports':
                install_module = module + 'reporter'
            else:
                install_module = module
            ns = SimpleNamespace(modules=[install_module], version=version)
            ns.__dict__.update(default_ns.__dict__)
            cravat_admin.install_modules(ns)
            kwargs[k].append(module)
    else:
        kwargs[k] = v
kwargs['inputs'] = snakemake.input
cravat.run(*args, **kwargs)
