# `name` is the name of the package as used for `pip install package`
name = "src"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
# Your version number should follow https://python.org/dev/peps/pep-0440 and
# https://semver.org
version = "0.1.dev0"
author = "Akhil Karra"
author_email = "akhil.karra@me.com"
description = "Source package for Akhil Karra's Python files and notebooks"  # One-liner
url = "akhilkarra/python-lab"  # your project homepage
license = "Private"  # See https://choosealicense.com
