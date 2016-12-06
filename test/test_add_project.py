import pytest
from model.project import Project
from fixture.application import Application



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_project(app):
    app.open_project_page()
    app.login(username="administrator", password="root")
    app.open_project()
    app.create_project(Project(name="14", description="1414"))
    app.return_project_page()
    app.logout()


def test_add_empty_project(app):
    app.open_project_page()
    app.login(username="administrator", password="root")
    app.open_project()
    app.create_project(Project(name="", description=""))
    app.return_project_page()
    app.logout()

