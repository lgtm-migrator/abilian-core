
# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")


setup(
    long_description=readme,
    name="abilian-core",
    version="0.11.21",
    description="A framework for enterprise applications (CRM, ERP, collaboration...).",
    python_requires="==3.*,>=3.8.0",
    project_urls={"repository": "https://github.com/abilian/abilian-core"},
    author="Abilian SAS",
    license="LGPL-2.0-or-later",
    packages=[
        "abilian",
        "abilian.cli",
        "abilian.core",
        "abilian.core.extensions",
        "abilian.core.models",
        "abilian.core.models.tests",
        "abilian.core.tests",
        "abilian.services",
        "abilian.services.activity",
        "abilian.services.antivirus",
        "abilian.services.audit",
        "abilian.services.auth",
        "abilian.services.conversion",
        "abilian.services.image",
        "abilian.services.image.tests",
        "abilian.services.indexing",
        "abilian.services.preferences",
        "abilian.services.repository",
        "abilian.services.security",
        "abilian.services.settings",
        "abilian.services.tagging",
        "abilian.services.viewtracker",
        "abilian.services.vocabularies",
        "abilian.testing",
        "abilian.web",
        "abilian.web.admin",
        "abilian.web.admin.panels",
        "abilian.web.admin.panels.groups",
        "abilian.web.admin.panels.users",
        "abilian.web.assets",
        "abilian.web.attachments",
        "abilian.web.comments",
        "abilian.web.coreviews",
        "abilian.web.forms",
        "abilian.web.preferences",
        "abilian.web.search",
        "abilian.web.setupwizard",
        "abilian.web.tags",
        "abilian.web.tests",
        "abilian.web.tools",
        "abilian.web.uploads",
        "abilian.web.views",
        "demo",
        "docs.exts",
    ],
    package_dir={"": "src"},
    package_data={
        "abilian": [
            "translations/*.pot",
            "translations/de_DE/LC_MESSAGES/*.mo",
            "translations/de_DE/LC_MESSAGES/*.po",
            "translations/en/LC_MESSAGES/*.mo",
            "translations/en/LC_MESSAGES/*.po",
            "translations/es/LC_MESSAGES/*.mo",
            "translations/es/LC_MESSAGES/*.po",
            "translations/es_ES/LC_MESSAGES/*.mo",
            "translations/es_ES/LC_MESSAGES/*.po",
            "translations/fr/LC_MESSAGES/*.mo",
            "translations/fr/LC_MESSAGES/*.po",
            "translations/fr_FR/LC_MESSAGES/*.mo",
            "translations/fr_FR/LC_MESSAGES/*.po",
            "translations/id_ID/LC_MESSAGES/*.mo",
            "translations/id_ID/LC_MESSAGES/*.po",
            "translations/it_IT/LC_MESSAGES/*.mo",
            "translations/it_IT/LC_MESSAGES/*.po",
            "translations/nl/LC_MESSAGES/*.mo",
            "translations/nl/LC_MESSAGES/*.po",
            "translations/nl_NL/LC_MESSAGES/*.mo",
            "translations/nl_NL/LC_MESSAGES/*.po",
            "translations/pt_BR/LC_MESSAGES/*.mo",
            "translations/pt_BR/LC_MESSAGES/*.po",
            "translations/pt_PT/LC_MESSAGES/*.mo",
            "translations/pt_PT/LC_MESSAGES/*.po",
            "translations/tr_TR/LC_MESSAGES/*.mo",
            "translations/tr_TR/LC_MESSAGES/*.po",
            "translations/zh_CN/LC_MESSAGES/*.mo",
            "translations/zh_CN/LC_MESSAGES/*.po",
            "translations/zh_TW/LC_MESSAGES/*.mo",
            "translations/zh_TW/LC_MESSAGES/*.po",
        ],
        "abilian.core": ["*.yml"],
        "abilian.services": ["sandbox/*.txt"],
        "abilian.services.auth": [
            "templates/login/*.html",
            "templates/login/email/*.txt",
        ],
        "abilian.services.conversion": [
            "dummy_files/*.doc",
            "dummy_files/*.docx",
            "dummy_files/*.jpg",
            "dummy_files/*.odt",
            "dummy_files/*.pdf",
            "dummy_files/*.xls",
        ],
        "abilian.services.image.tests": ["*.jpg"],
        "abilian.services.vocabularies": [
            "templates/admin/*.html",
            "templates/admin/macros/*.html",
        ],
        "abilian.web": [
            "resources/bootbox/*.js",
            "resources/bootstrap-datepicker/css/*.css",
            "resources/bootstrap-datepicker/js/*.js",
            "resources/bootstrap-datepicker/js/locales/*.js",
            "resources/bootstrap-datepicker/less/*.less",
            "resources/bootstrap-switch/*.js",
            "resources/bootstrap-switch/less/bootstrap3/*.less",
            "resources/bootstrap-timepicker/css/*.css",
            "resources/bootstrap-timepicker/js/*.js",
            "resources/bootstrap-timepicker/less/*.less",
            "resources/bootstrap/fonts/*.eot",
            "resources/bootstrap/fonts/*.svg",
            "resources/bootstrap/fonts/*.ttf",
            "resources/bootstrap/fonts/*.woff",
            "resources/bootstrap/fonts/*.woff2",
            "resources/bootstrap/js/*.js",
            "resources/bootstrap/less/*.json",
            "resources/bootstrap/less/*.less",
            "resources/bootstrap/less/mixins/*.less",
            "resources/ckeditor/*.css",
            "resources/ckeditor/*.js",
            "resources/ckeditor/*.md",
            "resources/ckeditor/adapters/*.js",
            "resources/ckeditor/lang/*.js",
            "resources/ckeditor/plugins/*.png",
            "resources/ckeditor/plugins/a11yhelp/dialogs/*.js",
            "resources/ckeditor/plugins/a11yhelp/dialogs/lang/*.js",
            "resources/ckeditor/plugins/a11yhelp/dialogs/lang/*.txt",
            "resources/ckeditor/plugins/about/dialogs/*.js",
            "resources/ckeditor/plugins/about/dialogs/*.png",
            "resources/ckeditor/plugins/about/dialogs/hidpi/*.png",
            "resources/ckeditor/plugins/autolink/*.js",
            "resources/ckeditor/plugins/bootstrapVisibility/*.js",
            "resources/ckeditor/plugins/bootstrapVisibility/*.md",
            "resources/ckeditor/plugins/bootstrapVisibility/*.txt",
            "resources/ckeditor/plugins/bootstrapVisibility/lang/*.js",
            "resources/ckeditor/plugins/clipboard/dialogs/*.js",
            "resources/ckeditor/plugins/colordialog/dialogs/*.js",
            "resources/ckeditor/plugins/dialog/*.js",
            "resources/ckeditor/plugins/div/dialogs/*.js",
            "resources/ckeditor/plugins/find/dialogs/*.js",
            "resources/ckeditor/plugins/flash/dialogs/*.js",
            "resources/ckeditor/plugins/flash/images/*.png",
            "resources/ckeditor/plugins/forms/dialogs/*.js",
            "resources/ckeditor/plugins/forms/images/*.gif",
            "resources/ckeditor/plugins/iframe/dialogs/*.js",
            "resources/ckeditor/plugins/iframe/images/*.png",
            "resources/ckeditor/plugins/image/dialogs/*.js",
            "resources/ckeditor/plugins/image/images/*.png",
            "resources/ckeditor/plugins/link/dialogs/*.js",
            "resources/ckeditor/plugins/link/images/*.png",
            "resources/ckeditor/plugins/link/images/hidpi/*.png",
            "resources/ckeditor/plugins/liststyle/dialogs/*.js",
            "resources/ckeditor/plugins/magicline/images/*.png",
            "resources/ckeditor/plugins/magicline/images/hidpi/*.png",
            "resources/ckeditor/plugins/pagebreak/images/*.gif",
            "resources/ckeditor/plugins/pastefromword/filter/*.js",
            "resources/ckeditor/plugins/preview/*.html",
            "resources/ckeditor/plugins/scayt/*.md",
            "resources/ckeditor/plugins/scayt/dialogs/*.css",
            "resources/ckeditor/plugins/scayt/dialogs/*.js",
            "resources/ckeditor/plugins/showblocks/images/*.png",
            "resources/ckeditor/plugins/smiley/dialogs/*.js",
            "resources/ckeditor/plugins/smiley/images/*.gif",
            "resources/ckeditor/plugins/smiley/images/*.png",
            "resources/ckeditor/plugins/specialchar/dialogs/*.js",
            "resources/ckeditor/plugins/specialchar/dialogs/lang/*.js",
            "resources/ckeditor/plugins/specialchar/dialogs/lang/*.txt",
            "resources/ckeditor/plugins/table/dialogs/*.js",
            "resources/ckeditor/plugins/tabletools/dialogs/*.js",
            "resources/ckeditor/plugins/templates/dialogs/*.css",
            "resources/ckeditor/plugins/templates/dialogs/*.js",
            "resources/ckeditor/plugins/templates/templates/*.js",
            "resources/ckeditor/plugins/templates/templates/images/*.gif",
            "resources/ckeditor/plugins/wsc/*.md",
            "resources/ckeditor/plugins/wsc/dialogs/*.css",
            "resources/ckeditor/plugins/wsc/dialogs/*.html",
            "resources/ckeditor/plugins/wsc/dialogs/*.js",
            "resources/ckeditor/samples/*.html",
            "resources/ckeditor/samples/css/*.css",
            "resources/ckeditor/samples/img/*.png",
            "resources/ckeditor/samples/js/*.js",
            "resources/ckeditor/samples/old/*.css",
            "resources/ckeditor/samples/old/*.html",
            "resources/ckeditor/samples/old/*.js",
            "resources/ckeditor/samples/old/*.php",
            "resources/ckeditor/samples/old/assets/*.jpg",
            "resources/ckeditor/samples/old/assets/*.php",
            "resources/ckeditor/samples/old/assets/inlineall/*.png",
            "resources/ckeditor/samples/old/assets/outputxhtml/*.css",
            "resources/ckeditor/samples/old/assets/uilanguages/*.js",
            "resources/ckeditor/samples/old/dialog/*.html",
            "resources/ckeditor/samples/old/dialog/assets/*.js",
            "resources/ckeditor/samples/old/enterkey/*.html",
            "resources/ckeditor/samples/old/htmlwriter/*.html",
            "resources/ckeditor/samples/old/htmlwriter/assets/outputforflash/*.fla",
            "resources/ckeditor/samples/old/htmlwriter/assets/outputforflash/*.js",
            "resources/ckeditor/samples/old/htmlwriter/assets/outputforflash/*.swf",
            "resources/ckeditor/samples/old/magicline/*.html",
            "resources/ckeditor/samples/old/toolbar/*.html",
            "resources/ckeditor/samples/old/wysiwygarea/*.html",
            "resources/ckeditor/samples/toolbarconfigurator/*.html",
            "resources/ckeditor/samples/toolbarconfigurator/css/*.css",
            "resources/ckeditor/samples/toolbarconfigurator/font/*.eot",
            "resources/ckeditor/samples/toolbarconfigurator/font/*.json",
            "resources/ckeditor/samples/toolbarconfigurator/font/*.svg",
            "resources/ckeditor/samples/toolbarconfigurator/font/*.ttf",
            "resources/ckeditor/samples/toolbarconfigurator/font/*.txt",
            "resources/ckeditor/samples/toolbarconfigurator/font/*.woff",
            "resources/ckeditor/samples/toolbarconfigurator/js/*.js",
            "resources/ckeditor/samples/toolbarconfigurator/lib/codemirror/*.css",
            "resources/ckeditor/samples/toolbarconfigurator/lib/codemirror/*.js",
            "resources/ckeditor/skins/moono/*.css",
            "resources/ckeditor/skins/moono/*.md",
            "resources/ckeditor/skins/moono/*.png",
            "resources/ckeditor/skins/moono/images/*.gif",
            "resources/ckeditor/skins/moono/images/*.png",
            "resources/ckeditor/skins/moono/images/hidpi/*.png",
            "resources/datatables/css/*.css",
            "resources/datatables/images/*.ico",
            "resources/datatables/images/*.png",
            "resources/datatables/images/*.psd",
            "resources/datatables/js/*.js",
            "resources/fileapi/*.js",
            "resources/fileapi/*.swf",
            "resources/fileapi/plugins/*.js",
            "resources/font-awesome/css/*.css",
            "resources/font-awesome/fonts/*.eot",
            "resources/font-awesome/fonts/*.otf",
            "resources/font-awesome/fonts/*.svg",
            "resources/font-awesome/fonts/*.ttf",
            "resources/font-awesome/fonts/*.woff",
            "resources/font-awesome/fonts/*.woff2",
            "resources/font-awesome/less/*.less",
            "resources/font-awesome/scss/*.scss",
            "resources/highlightjs/*.css",
            "resources/highlightjs/*.js",
            "resources/img/*.png",
            "resources/jquery/js/*.js",
            "resources/js/*.js",
            "resources/js/widgets/*.js",
            "resources/less/*.less",
            "resources/nvd3/*.css",
            "resources/nvd3/*.js",
            "resources/nvd3/*.txt",
            "resources/requirejs/*.js",
            "resources/select2/*.css",
            "resources/select2/*.gif",
            "resources/select2/*.js",
            "resources/select2/*.json",
            "resources/select2/*.md",
            "resources/select2/*.png",
            "resources/select2/*.sh",
            "resources/select2/*.template",
            "resources/typeahead/*.css",
            "resources/typeahead/*.js",
            "resources/typeahead/*.less",
            "templates/*.html",
            "templates/*.js",
            "templates/debug_panels/*.html",
            "templates/default/*.html",
            "templates/default/*.svg",
            "templates/macros/*.html",
            "templates/preferences/*.html",
            "templates/widgets/*.html",
        ],
        "abilian.web.admin": ["templates/admin/*.html"],
        "abilian.web.preferences": ["tests/*.png"],
        "abilian.web.search": ["templates/search/*.html"],
        "abilian.web.setupwizard": ["templates/setupwizard/*.html"],
        "abilian.web.tags": ["templates/admin/*.html"],
    },
    install_requires=[
        "alembic>=0.9",
        "bcrypt",
        "bleach>=2",
        "celery==4.*,>=4.0.0",
        "clamd",
        "closure",
        "cssmin",
        "deprecated",
        "devtools",
        "flask==1.*,>=1.0.0",
        "flask-assets>=0.12",
        "flask-babel<2,>=0.11",
        "flask-login>=0.4",
        "flask-mail>=0.9.1",
        "flask-migrate>=2.0",
        "flask-sqlalchemy<=2.1",
        "flask-talisman>=0.6",
        "flask-wtf<0.13,>=0.12",
        "hyperlink",
        "jinja2<3",
        "jsmin",
        "lxml",
        "markupsafe>=0.21",
        "pandas>=0.17",
        "pathlib",
        "pillow",
        "pygeoip",
        "python-dateutil==2.*,>=2.4.0",
        "python-magic",
        "pyyaml",
        "redis==3.*,>=3.0.0",
        "sentry-sdk[flask]",
        "sqlalchemy==1.*,==1.3.*,>=1.1.0,>=1.3.0",
        "sqlparse",
        "tqdm",
        "webassets<2",
        "werkzeug<1",
        "whoosh==2.*,>=2.5.0",
        "wtforms-alchemy>=0.12",
        "wtforms-sqlalchemy",
    ],
    extras_require={
        "dev": [
            "black",
            "docformatter",
            "docutils",
            "flake8",
            "flake8-assertive",
            "flake8-blind-except",
            "flake8-bugbear",
            "flake8-comprehensions",
            "flake8-isort",
            "flake8-logging-format",
            "flake8-mutable",
            "flake8-pytest",
            "flake8-super-call",
            "flake8-tidy-imports",
            "flask-debugtoolbar>=0.10",
            "gitchangelog==3.*,>=3.0.0",
            "html5lib",
            "isort",
            "mastool",
            "mccabe",
            "mypy",
            "nox",
            "pre-commit",
            "pytest>=2.4.0",
            "pytest-cov",
            "pytest-flask==1.*,>=1.0.0",
            "pytest-randomly",
            "pytest-repeat",
            "pytest-xdist",
            "requests",
            "restructuredtext-lint",
            "sphinx>=1.5.5",
            "sphinx-rtd-theme",
            "tox",
            "typeguard",
        ]
    },
)
