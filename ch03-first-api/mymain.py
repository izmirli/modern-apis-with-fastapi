import fastapi
import uvicorn

from typing import Optional

api = fastapi.FastAPI()


@api.get('/')
def index():
    body = """
<html>
<body style='padding: 10px;'>
  <h1>Welcome to the API</h1>
  <div>
    Try it: <a href='/api/calc?x=7&y=11'>/api/calc?x=7&y=11</a>
  </div>
</body>
</html>"""

    return fastapi.responses.HTMLResponse(content=body)


# @api.get('/api/calc/{x}/{y}/{z}')  # can have parameters after endpoint (like /endpoint/{param})
@api.get('/api/calc')  # path fot this endpoint
def calc(x: int, y: int, z: Optional[int] = None):  # unless type give, use str; unless has default, param is required.
    if z == 0:
        # return an error as string, unless we explicitly keep it JSON.
        # return fastapi.Response(content='{"ERROR": "z cannot be zero."}',
        #                         media_type="application/json", status_code=400)

        # use JSONResponse is better in this case
        return fastapi.responses.JSONResponse({"ERROR": "z cannot be zero."}, status_code=400)

    value = (x + y)
    if z is not None:
        value /= z

    return {'value': value}  # dic will be return as JSON


# uvicorn server runs this app (pass host and/or port, or get default: 127.0.0.1:8000).
uvicorn.run(api)
