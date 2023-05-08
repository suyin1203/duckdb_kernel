import glob
import json
import os
import sys
from setuptools import setup, find_packages

with open('duckdb_kernel/__init__.py', 'rb') as fid:
    for line in fid:
        line = line.decode('utf-8')
        if line.startswith('__version__'):
            version = line.strip().split()[-1][1:-1]
            break

DISTNAME = 'duckdb_kernel'
PY_EXECUTABLE = 'python'

# when building wheels, directly use 'python' in the kernelspec.
if any(a.startswith("bdist") for a in sys.argv):
    PY_EXECUTABLE = 'python'

# when directly installing, use sys.executable to get python full path.
if any(a.startswith("install") for a in sys.argv):
    PY_EXECUTABLE = sys.executable

# generating kernel.json for both kernels
os.makedirs(os.path.join(DISTNAME, 'duckdb'), exist_ok=True)
with open(os.path.join(DISTNAME, 'kernel_template.json'), 'r') as fp:
    duckdb_json = json.load(fp)
duckdb_json['argv'][0] = PY_EXECUTABLE
with open(os.path.join(DISTNAME, 'duckdb','kernel.json'), 'w') as fp:
    json.dump(duckdb_json, fp)

# os.makedirs(os.path.join(DISTNAME, 'duckdb_connect'), exist_ok=True)
# with open(os.path.join(DISTNAME, 'kernel_template.json'), 'r') as fp:
#     duckdb_json = json.load(fp)

# duckdb_json['argv'][0] = PY_EXECUTABLE
# duckdb_json['display_name'] = 'duckdb (Connection)'
# duckdb_json['name'] = "duckdb_connect"

# duckdb_json['env'] = {'connect-to-existing-kernel': '1'}
# with open(os.path.join(DISTNAME, 'duckdb_connect','kernel.json'), 'w') as fp:
#     json.dump(duckdb_json, fp)

PACKAGE_DATA = {
    DISTNAME: ['*.m'] + glob.glob('%s/**/*.*' % DISTNAME)
}

# DATA_FILES = [
#     ('Jupyter/kernels/duckdb', [
#         '%s/duckdb/kernel.json' % DISTNAME
#      ] + glob.glob('%s/images/*.png' % DISTNAME)
#     ), 
#     ('share/jupyter/kernels/duckdb_connect', [
#         '%s/duckdb_connect/kernel.json' % DISTNAME
#      ] + glob.glob('%s/images/*.png' % DISTNAME)
#     )
# ]

if __name__ == "__main__":
    setup(name="duckdb_kernel",
          author="suyin",
          version=version,
          url="https://github.com/suyin1203/duckdb_kernel",
          license="MID",
          long_description=open("README.rst").read(),
          long_description_content_type='text/x-rst',
          classifiers=["Framework :: IPython",
                       "License :: OSI Approved :: MIT License",
                       "Programming Language :: Python :: 3.4",
                       "Programming Language :: Python :: 3.5",
                       "Programming Language :: Python :: 3.6",
                       "Programming Language :: Python :: 3.7",
                       "Programming Language :: Python :: 3.8",
                       "Programming Language :: Python :: 3.9",
                       "Programming Language :: Python :: 3.10",
                       "Programming Language :: Python :: 3.11",
                       "Topic :: System :: Shells"],
          packages=find_packages(include=["duckdb_kernel", "duckdb_kernel.*"]),
          package_data=PACKAGE_DATA,
          include_package_data=True,
          # data_files=DATA_FILES,
          requires=["duckdb", 
                    "ipython"],
          install_requires=["duckdb",
                            "ipython"]
          )
