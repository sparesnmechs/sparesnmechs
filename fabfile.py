"""Fabfile for deploying."""
from fabric.api import local


def deploy():
    """Upload to packaging index."""
    local("python setup.py sdist bdist_wheel")
    local(
        "twine upload --repository-url https://upload.pypi.org/legacy/ dist/*"
    )
    local("rm dist/*")
