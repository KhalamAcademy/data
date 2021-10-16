# Setup:
# pip install pyyaml

# This converts all the yaml files into a proper *.min.json's

import json
import os
import shutil
import common

def pformat(d):
    return json.dumps(d, indent=4)

shutil.rmtree("build", ignore_errors=True)
os.mkdir("build")
os.mkdir("build/examples")
os.mkdir("build/index")

info = common.load_info_file()
print("Got info file of: ", pformat(info))

examples = info["examples"]
del info["examples"]

with open("build/examples/info.json", "w") as examples_fp:
    json.dump(examples, examples_fp, indent=4)

with open("build/index/info.min.json", "w") as site_index_info:
    json.dump(info, site_index_info)