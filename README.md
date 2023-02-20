<!--
    =====================================
    generator=datazen
    version=3.1.0
    hash=ce08dca2813c60d52cc066c7ff68fcce
    =====================================
-->

# typescript-package-template

![Build Status](https://github.com/vkottler/typescript-package-template/workflows/Build%20Template/badge.svg)

*This is a template intended to be used with
[Cookiecutter](https://github.com/cookiecutter/cookiecutter).*

# Usage

Invoke `cookiecutter` and fill out information about your project:

```
$ cookiecutter git@github.com:vkottler/typescript-package-template.git
name [Vaughn Kottler]: <Your Name>
project_name [package-name]: <your-project-name>
description: [Short project description.]: <Your project's description.>
...
```

## Structure

```
$ tree -a -I venv*|__pycache__|*cov*|*-out|config|build|tags|.git*|.*cache*|node_modules -- package-name

package-name
├── .eslintrc.cjs
├── jest.config.js
├── LICENSE
├── local
│   ├── configs
│   │   ├── html.yaml
│   │   └── license.yaml
│   ├── templates
│   │   └── app.html.j2
│   └── variables
│       └── html.yaml
├── Makefile
├── manifest.yaml
├── package.json
├── package-lock.json
├── package-name -> src
├── README.md
├── src
│   ├── dev_requirements.txt
│   ├── favicon.ico
│   ├── index.css
│   ├── index.html
│   ├── index.ts
│   ├── requirements.txt
│   └── ts
│       └── App.ts
├── tests
│   └── App.test.ts
├── tsconfig.json
└── .vimrc

8 directories, 22 files

```
