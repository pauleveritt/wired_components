import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def app(registry) -> None:
    from wired_components.samples.simple import wired_setup
    wired_setup(registry)


def test_homepage(registry, app):
    from wired_components.samples.simple import render_path
    result = render_path(registry, '/')

    # Parse it and do some tests
    soup: BeautifulSoup = BeautifulSoup(result, 'html.parser')
    nav = soup.find('nav').string.strip()
    assert nav == 'BC: label is BC'
    h1 = soup.find('h1').string.strip()
    assert h1 == 'Root: My Site'
