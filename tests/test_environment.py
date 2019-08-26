from wired import ServiceRegistry


def test_environment_wired_setup(registry: ServiceRegistry):
    from wired_components.environment import wired_setup
    assert wired_setup(registry) is None


# def test_environment_construction():
#     env = make_environment()
#     assert env
