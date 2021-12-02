###UviCorn

Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools.

Until recently Python has lacked a minimal low-level server/application interface for asyncio frameworks. The ASGI specification fills this gap, and means we're now able to start building a common set of tooling usable across all asyncio frameworks.

ASGI should help enable an ecosystem of Python web frameworks that are highly competitive against Node and Go in terms of achieving high throughput in IO-bound contexts. It also provides support for HTTP/2 and WebSockets, which cannot be handled by WSGI.

Uvicorn currently supports HTTP/1.1 and WebSockets. Support for HTTP/2 is planned.

>This will install uvicorn with minimal (pure Python) dependencies.
>>pip install uvicorn

>This will install uvicorn with "Cython-based" dependencies (where possible) and other "optional extras"
>>pip install uvicorn[standard]

> run server
>> uvicorn example:app

>><b>uvicorn --help</b> <br>
>>Usage: uvicorn [OPTIONS] APP <br>
>>Options:<br>
  --host TEXT                     Bind socket to this host.  [default:
                                  127.0.0.1]<br>
  --port INTEGER                  Bind socket to this port.  [default: 8000]
  <br>--uds TEXT                      Bind to a UNIX domain socket.
 <br> --fd INTEGER                    Bind to socket from this file descriptor.
 <br> --reload                        Enable auto-reload.
 <br> --reload-dir PATH               Set reload directories explicitly, instead
                                  of using the current working directory.
  <br>--reload-include TEXT           Set glob patterns to include while watching
                                  for files. Includes '*.py' by default, which
                                  can be overridden in reload-excludes.
  <br>--reload-exclude TEXT           Set glob patterns to exclude while watching
                                  for files. Includes '.*, .py[cod], .sw.*,
                                  ~*' by default, which can be overridden in
                                  reload-excludes.
  <br>--reload-delay FLOAT            Delay between previous and next check if
                                  application needs to be. Defaults to 0.25s.
                                  [default: 0.25]
  <br>--workers INTEGER               Number of worker processes. Defaults to the
                                  $WEB_CONCURRENCY environment variable if
                                  available, or 1. Not valid with --reload.
  <br>--loop [auto|asyncio|uvloop]    Event loop implementation.  [default: auto]
  <br>--http [auto|h11|httptools]     HTTP protocol implementation.  [default:
                                  auto]
  <br>--ws [auto|none|websockets|wsproto]
                                  WebSocket protocol implementation.
                                  [default: auto]
  <br>--ws-max-size INTEGER           WebSocket max size message in bytes
                                  [default: 16777216]
  <br>--ws-ping-interval FLOAT        WebSocket ping interval  [default: 20.0]
  <br>--ws-ping-timeout FLOAT         WebSocket ping timeout  [default: 20.0]
 <br> --lifespan [auto|on|off]        Lifespan implementation.  [default: auto]
  <br>--interface [auto|asgi3|asgi2|wsgi]
                                  Select ASGI3, ASGI2, or WSGI as the
                                  application interface.  [default: auto]
  <br>--env-file PATH                 Environment configuration file.
  <br>--log-config PATH               Logging configuration file. Supported
                                  formats: .ini, .json, .yaml.
  <br>--log-level [critical|error|warning|info|debug|trace]
                                  Log level. [default: info]
  <br>--access-log / --no-access-log  Enable/Disable access log.
  <br>--use-colors / --no-use-colors  Enable/Disable colorized logging.
  <br>--proxy-headers / --no-proxy-headers
                                  Enable/Disable X-Forwarded-Proto,
                                  X-Forwarded-For, X-Forwarded-Port to
                                  populate remote address info.
  <br>--server-header / --no-server-header
                                  Enable/Disable default Server header.
  <br>--date-header / --no-date-header
                                  Enable/Disable default Date header.
  <br>--forwarded-allow-ips TEXT      Comma seperated list of IPs to trust with
                                  proxy headers. Defaults to the
                                  $FORWARDED_ALLOW_IPS environment variable if
                                  available, or '127.0.0.1'.
  <br>--root-path TEXT                Set the ASGI 'root_path' for applications
                                  submounted below a given URL path.
  <br>--limit-concurrency INTEGER     Maximum number of concurrent connections or
                                  tasks to allow, before issuing HTTP 503
                                  responses.
  <br>--backlog INTEGER               Maximum number of connections to hold in
                                  backlog
  <br>--limit-max-requests INTEGER    Maximum number of requests to service before
                                  terminating the process.
  <br>--timeout-keep-alive INTEGER    Close Keep-Alive connections if no new data
                                  is received within this timeout.  [default:
                                  5]
  <br>--ssl-keyfile TEXT              SSL key file
  <br>--ssl-certfile TEXT             SSL certificate file
  <br>--ssl-keyfile-password TEXT     SSL keyfile password
  <br>--ssl-version INTEGER           SSL version to use (see stdlib ssl module's)
                                  [default: 17]
  <br>--ssl-cert-reqs INTEGER         Whether client certificate is required (see
                                  stdlib ssl module's)  [default: 0]
  <br>--ssl-ca-certs TEXT             CA certificates file
  <br>--ssl-ciphers TEXT              Ciphers to use (see stdlib ssl module's)
                                  [default: TLSv1]
  <br>--header TEXT                   Specify custom default HTTP response headers
                                  as a Name:Value pair
  <br>--version                       Display the uvicorn version and exit.
  <br>--app-dir TEXT                  Look for APP in the specified directory, by
                                  adding this to the PYTHONPATH. Defaults to
                                  the current working directory.  [default: .]
  <br>--factory                       Treat APP as an application factory, i.e. a
                                  () -> <ASGI app> callable.  [default: False]
  <br>--help                          Show this message and exit. """