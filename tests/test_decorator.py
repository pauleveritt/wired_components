def register_foo(*args, **kwargs):
    return 987


def test_decorator_construction():
    from wired_components.decorator import BaseDecorator
    from wired_components.resource import IResource
    from wired_components.view import IView

    # noinspection PyPep8Naming
    class foo(BaseDecorator):
        for_ = IView
        register_function = register_foo

    # Construction
    f: foo = foo(context=IResource)
    assert f.for_ == IView
    assert f.register_function() == 987
    assert f.context == IResource
    assert f.name is None

    # Calling
    # @foo would be here
    class SomeFoo:
        pass

    # noinspection PyCallingNonCallable
    result = f(SomeFoo)
    assert result == SomeFoo
