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
    skip_data=False,
)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
kwargs = {}
args = snakemake.params.get("args", "")
if args != "":
    parsed_args = cravat.util.get_args(
        cravat.cravat_class.cravat_cmd_parser, [args.split()], {}
    )
    kwargs.update(parsed_args.__dict__)
sysconf = cravat.admin_util.get_system_conf()
modules_dir = sysconf.get("modules_dir")
for k, v in snakemake.params.items():
    if k == "args":
        continue
    else:
        kwargs[k] = v
kwargs["inputs"] = snakemake.input
local_module_names = cravat.admin_util.list_local()
if "annotators" not in kwargs:
    print("No annotator was given. Exiting.")
elif "reports" not in kwargs:
    print("No report type was given. Exiting.")
else:
    if kwargs["annotators"] is not None and len(kwargs["annotators"]) > 0:
        for i in range(len(kwargs["annotators"])):
            mv = kwargs["annotators"][i]
            if "=" in mv:
                module_name, version = mv.split("=")
                install_module_name = module_name
            else:
                module_name = mv
                install_module_name = module_name
                version = None
            if install_module_name not in local_module_names:
                install_flag = True
            else:
                if version is None:
                    install_flag = False
                else:
                    local_ver = cravat.admin_util.get_local_module_info(
                        install_module_name
                    ).version
                    if local_ver != version:
                        install_flag = True
                    else:
                        install_flag = False
            if install_flag:
                ns = SimpleNamespace(modules=[install_module_name], version=version)
                ns.__dict__.update(default_ns.__dict__)
                cravat_admin.install_modules(ns)
            kwargs["annotators"][i] = module_name
    if kwargs["reports"] is not None and len(kwargs["reports"]) > 0:
        for i in range(len(kwargs["reports"])):
            mv = kwargs["reports"][i]
            if "=" in mv:
                module_name, version = mv.split("=")
                install_module_name = module_name + "reporter"
            else:
                module_name = mv
                install_module_name = module_name + "reporter"
                version = None
            if install_module_name not in local_module_names:
                install_flag = True
            else:
                if version is None:
                    install_flag = False
                else:
                    local_ver = cravat.admin_util.get_local_module_info(
                        install_module_name
                    ).version
                    if local_ver != version:
                        install_flag = True
                    else:
                        install_flag = False
            if install_flag:
                ns = SimpleNamespace(modules=[install_module_name], version=version)
                ns.__dict__.update(default_ns.__dict__)
                cravat_admin.install_modules(ns)
            kwargs["reports"][i] = module_name
    ret = cravat.run(**kwargs)
