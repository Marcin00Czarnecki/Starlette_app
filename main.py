from starlette.applications import Starlette
from starlette.routing  import Route
from starlette.requests import Request
from starlette.responses import PlainTextResponse


async def index(request:Request):
    return PlainTextResponse(content="Hello World")


routes=[
    Route("/", endpoint=index)
]

app=Starlette(
    debug=True,
    routes=routes
)
