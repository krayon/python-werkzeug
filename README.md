<div align="center"><img src="https://raw.githubusercontent.com/pallets/werkzeug/refs/heads/stable/docs/_static/werkzeug-name.svg" alt="" height="150"></div>

# Werkzeug

*werkzeug* German noun: "tool". Etymology: *werk* ("work"), *zeug* ("stuff")

Werkzeug is a comprehensive [WSGI][] web application library. It began as
a simple collection of various utilities for WSGI applications and has
become one of the most advanced WSGI utility libraries.

It includes:

-   An interactive debugger that allows inspecting stack traces and
    source code in the browser with an interactive interpreter for any
    frame in the stack.
-   A full-featured request object with objects to interact with
    headers, query args, form data, files, and cookies.
-   A response object that can wrap other WSGI applications and handle
    streaming data.
-   A routing system for matching URLs to endpoints and generating URLs
    for endpoints, with an extensible system for capturing variables
    from URLs.
-   HTTP utilities to handle entity tags, cache control, dates, user
    agents, cookies, files, and more.
-   A threaded WSGI server for use while developing applications
    locally.
-   A test client for simulating HTTP requests during testing without
    requiring running a server.

Werkzeug doesn't enforce any dependencies. It is up to the developer to
choose a template engine, database adapter, and even how to handle
requests. It can be used to build all sorts of end user applications
such as blogs, wikis, or bulletin boards.

[Flask][] wraps Werkzeug, using it to handle the details of WSGI while
providing more structure and patterns for defining powerful
applications.

[WSGI]: https://wsgi.readthedocs.io/en/latest/
[Flask]: https://www.palletsprojects.com/p/flask/


## A Simple Example

```python
# save this as app.py
from werkzeug.wrappers import Request, Response

@Request.application
def application(request: Request) -> Response:
    return Response("Hello, World!")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("127.0.0.1", 5000, application)
```

```
$ python -m app
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


## Donate

The Pallets organization develops and supports Werkzeug and other
popular packages. In order to grow the community of contributors and
users, and allow the maintainers to devote more time to the projects,
[please donate today][].

[please donate today]: https://palletsprojects.com/donate

## Contributing

See our [detailed contributing documentation][contrib] for many ways to
contribute, including reporting issues, requesting features, asking or answering
questions, and making PRs.

[contrib]: https://palletsprojects.com/contributing/
