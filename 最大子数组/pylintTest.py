import pylint.lint

pylint_opts = ['--rcfile=PylintConfig.conf', '-ry', './main.py']

pylint.lint.Run(pylint_opts)