[metadata]
name = pomo
version = 0.0.0
description = A Pomodoro timer for the terminal
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/GonzalezAndrew/pomo
author = Andrew Gonzalez
author_email = andrewgonzo23@gmail.com
license = MIT
license_file = LICENSE
classifiers =
    License :: OSI Approved :: MIT License
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: 3.10

[options]
packages = find:
python_requires = >=3.6.1

[options.packages.find]
exclude =
    tests*

[options.entry_points]
console_scripts =
    pomo = pomo.main:main

[bdist_wheel]
universal = True

[coverage:run]
plugins = covdefaults

[mypy]
check_untyped_defs = true
disallow_any_generics = true
disallow_incomplete_defs = true
disallow_untyped_defs = true
no_implicit_optional = true

[mypy-tests.*]
disallow_untyped_defs = false
