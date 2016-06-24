import {{ cookiecutter.project_package }}


def test_package_metadata():
    assert {{ cookiecutter.project_package }}.__author__
    assert {{ cookiecutter.project_package }}.__email__
    assert {{ cookiecutter.project_package }}.__version__
