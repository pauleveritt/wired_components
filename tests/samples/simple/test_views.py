import pytest
from bs4 import BeautifulSoup


@pytest.fixture
def app(registry) -> None:
    from wired_components.samples.simple import wired_setup
    wired_setup(registry)


@pytest.mark.parametrize(
    'path, heading',
    [
        ('/', 'Root: My Site'),
        ('/f1', 'Folder: The Folder At The Root'),
        ('/d1', 'Document: A Doc At The Root'),
    ]
)
def test_pages(registry, app, path, heading):
    from wired_components.samples.simple import render_path
    result = render_path(registry, path)

    # Parse it and do some tests
    soup: BeautifulSoup = BeautifulSoup(result, 'html.parser')
    nav = soup.find('nav').string.strip()
    assert nav == 'BC: label is BC'
    h1 = soup.find('h1').string.strip()
    assert h1 == heading
