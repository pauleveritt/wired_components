def register_foo(*args, **kwargs):
    return 987


def test_decorator_construction():
    from wired_components.decorator import BaseDecorator
    from wired_components.component import IComponent

    # noinspection PyPep8Naming
    class foo(BaseDecorator):
        for_ = IComponent
        register_function = register_foo

    context = object()

    # Construction
    f: foo = foo(context)
    assert f.for_ == IComponent
    assert f.register_function() == 987
    assert f.context == context
    assert f.name is None

    # Calling
    # @foo would be here
    class SomeFoo:
        pass

    # noinspection PyCallingNonCallable
    result = f(SomeFoo)
    assert result == SomeFoo
