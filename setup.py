from setuptools import setup, Extension, find_packages
import platform
from pathlib import Path
from Cython.Build import cythonize
from setuptools.config.expand import entry_points


def is_windows():
    return platform.system() == "Windows"

packages = find_packages(include=("cython_vst_loader*",), exclude=("tests",))

this_directory = Path(__file__).parent

include_paths = [
    this_directory.as_posix() + "/build/vstsdk/pluginterfaces/vst2.x",
    this_directory.as_posix() + "/cython_vst_loader/include"
]

ext = Extension("cython_vst_loader.vst_loader_wrapper",
                sources=['cython_vst_loader/vst_loader_wrapper.pyx'],
                include_dirs=include_paths
)

if not is_windows():
    ext.extra_compile_args = ["-Wno-unused-function"]

ext_modules = cythonize(ext,
    compiler_directives={'language_level': "3"},
    )

setup(
    packages=packages,
    #package_data={"cython_vst_loader": ["*.py"]},
    ext_modules=ext_modules
)
