from fasthtml.fastapp import * 

app, rt = fast_app(
    default_hdrs=False,
    hdrs=(
        Link(rel='stylesheet', href='assets/normalize.min.css', type='text/css'),
        Link(rel='stylesheet', href='assets/sakura.css', type='text/css'),
        Style("p {color: red;}")
))

@app.get("/")
def home():
    return Titled("FastHTML",
        P("Let's do this!"),
    )

serve()