###UviCorn

Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

Until recently Python has lacked a minimal low-level server/application interface for asyncio frameworks. The ASGI specification fills this gap, and means we're now able to start building a common set of tooling usable across all asyncio frameworks.

ASGI should help enable an ecosystem of Python web frameworks that are highly competitive against Node and Go in terms of achieving high throughput in IO-bound contexts. It also provides support for HTTP/2 and WebSockets, which cannot be handled by WSGI.

Uvicorn currently supports HTTP/1.1 and WebSockets. Support for HTTP/2 is planned.

>This will install uvicorn with minimal (pure Python) dependencies.
>>pip install uvicorn

>This will install uvicorn with "Cython-based" dependencies (where possible) and other "optional extras"
>>pip install uvicorn[standard]
