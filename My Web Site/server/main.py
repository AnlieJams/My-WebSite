from fastapi import FastAPI, HTTPException
from starlette.responses import HTMLResponse
from os.path import join, dirname, exists

app = FastAPI()

FILE_PATH = join(dirname(__file__), 'client_forms.txt')


@app.get("/", response_class=HTMLResponse)
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Backend for Portfolio</title>
        </head>
        <body>
            This is Backend for Portfolio website <a href="">github/</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get('/client_form')
def test_func(name, email, phone=None):
    user = {
        "name": name,
        "email": email
    }

    if phone and len(phone) > 6:
        user["phone"] = phone
    else:
        raise HTTPException(status_code=422, detail="Incorrect phone number")

    with open(FILE_PATH, 'a') as f:
        f.write(str(user) + '\n')

    return user


@app.get('/all_client_form')
def all_client_form():
    users = []

    if exists(FILE_PATH):
        with open(FILE_PATH) as f:
            for line in f:
                users.append(eval(line.rstrip()))

    return users