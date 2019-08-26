def test_configuration_wired_setup(registry):
    from wired_components.configuration import wired_setup
    assert wired_setup(registry) is None


def test_configuration_init_empty():
    from wired_components.configuration import Configuration
    configuration = Configuration()
    assert configuration.template_dirs == []


def test_configuration_init_values():
    import wired_components
    from wired_components.configuration import Configuration
    configuration = Configuration(
        template_dirs=[
            (wired_components, 'configuration')
        ]

    )
    assert configuration.template_dirs[0][0] == wired_components
    assert configuration.template_dirs[0][1] == 'configuration'
