================
wired_components
================

*Requests, views, resources, components, and more...for ``wired``.*

System like Sphinx and web systems like Pyramid have similar architectures: Process a request, generate a response.
And along the way, use a view, a configuration system, a resource abstraction, and other pieces.

``wired_components`` is a ready-to-go collection of those pieces, for ``wired``.
These pieces are inter-related -- the Jinja2 ``Environment`` needs information from the ``Configuration`` -- and thus, it makes sense to build them together.

Since ``wired_components`` is done with ``wired``, you can replace any of these pieces.
Thanks to inversion-of-control (IoC), you simply have to put your implementation in the registry.
Everything else that might use it, will use it.