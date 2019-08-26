def test_url_wired_setup(registry):
    from wired_components.url import wired_setup
    assert wired_setup(registry) is None


def test_url_construction():
    from wired_components.url import Url
    url = Url(path='somepath')
    assert url.path == 'somepath'
