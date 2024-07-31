
* Home
  * Learn

  * __
  * __

  1. Get Started

  * Get Started

  * Tutorials __

    * FastHTML By Example

    * Web Devs Quickstart

    * JS App Walkthrough

    * BYO Blog

    * Deploying FastHTML Apps

  * Explanations __

    * **ft** Components

    * Routes

  * Reference __

    * Live Reloading

  * Source __

    * Core

    * Components

    * Component extensions

    * Command Line Tools

## On this page

  * Installation
  * Usage
  * Next Steps

  * __Report an issue

# FastHTML

The fastest, most powerful way to create an HTML app

Welcome to the official FastHTML documentation.

FastHTML is a new next-generation web framework for fast, scalable web applications with minimal, compact code. It’s designed to be:

  * Powerful and expressive enough to build the most advanced, interactive web apps you can imagine.
  * Fast and lightweight, so you can write less code and get more done.
  * Easy to learn and use, with a simple, intuitive syntax that makes it easy to build complex apps quickly.

FastHTML apps are just Python code, so you can use FastHTML with the full power of the Python language and ecosystem.

## Installation

Since `fasthtml` is a Python library, you can install it with:

```
pip install python-fasthtml
```

In the near future, we hope to add component libraries that can likewise be installed via `pip`.

## Usage

For a minimal app, create a file “main.py” as follows:

```
**main.py**
```

```
from fasthtml.common import *

app,rt = fast_app()

@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")

serve()
```

Running the app with `python main.py` prints out a link to your running app: `http://localhost:5001/`. Visit that link in your browser and you should see a page with the title “FastHTML” and the text “Let’s do this!”. Congratulations - you’ve just created your first `fasthtml` app!

Adding interactivity is surprisingly easy, thanks to HTMX. If you modify the file to add this function…:

```
**main.py**
```

```
@rt('/change')
def get(): return P('Nice to be here!')
```

…you’ll now have a page with a clickable element that changes the text when clicked. When clicking on this link, the server will respond with an “HTML partial”—that is, just a snippet of HTML which will be inserted into the existing page. In this case, the returned element will replace the original P element (since that’s the default behavior of HTMX) with the new version returned by the second route.

This “hypermedia-based” approach to web development is a powerful way to build web applications.

## Next Steps

Start with the official sources to learn more about FastHTML:

  * About: Learn about the core ideas behind FastHTML
  * Documentation: Learn from examples how to write FastHTML code
  * Idiomatic app: Heavily commented source code walking through a complete application, including custom authentication, JS library connections, and database use.

We also have a 1-hour intro video:

The capabilities of FastHTML are vast and growing, and not all the features and patterns have been documented yet. Be prepared to invest time into studying and modifying source code, such as the main FastHTML repo’s notebooks and the official FastHTML examples repo:

  * FastHTML Examples Repo on GitHub
  * FastHTML Repo on GitHub

Then explore the small but growing third-party ecosystem of FastHTML tutorials, notebooks, libraries, and components:

  * Creating Custom FastHTML Tags for Markdown Rendering by Isaac Flath
  * Your tutorial here!

Finally, join the FastHTML community to ask questions, share your work, and learn from others:

  * Discord

  * __Report an issue
  * Home
  * Learn

  * __
  * __

  1. Tutorials
  2. FastHTML By Example

  * Get Started

  * Tutorials __

    * FastHTML By Example

    * Web Devs Quickstart

    * JS App Walkthrough

    * BYO Blog

    * Deploying FastHTML Apps

  * Explanations __

    * **ft** Components

    * Routes

  * Reference __

    * Live Reloading

  * Source __

    * Core

    * Components

    * Component extensions

    * Command Line Tools

## On this page

  * FastHTML Basics
  * Constructing HTML
  * Defining Routes
  * Styling Basics
  * Web Page -> Web App
  * HTMX
    * Replacing Elements Besides the Target
  * Full Example #1 - ToDo App
  * Full Example #2 - Image Generation App
    * Again, with Style
    * Again, with Sessions
    * Again, with Credits!
  * More on Routing and Request Parameters
    * Cookies
    * User Agent and HX-Request
    * Starlette Requests
    * Starlette Responses
    * Static Files
    * WebSockets
  * Full Example #3 - Chatbot Example with DaisyUI Components
  * Full Example #4 - Multiplayer Game of Life Example with Websockets
  * FT objects and HTML
  * Custom Scripts and Styling
  * Deploying Your App
    * Railway
    * Replit
    * HuggingFace
  * Where Next?

  * __Report an issue

  1. Tutorials
  2. FastHTML By Example

# FastHTML By Example

An introduction to FastHTML from the group up, with four complete examples

There are lots of non-FastHTML-specific tricks and patterns involved in building web apps. The goal of this tutorial is to give an alternate introduction to FastHTML, building out example applications to show common patterns and illustrate some of the ways you can build on top of the FastHTML foundations to create your own custom web apps. A secondary goal is to have this be a useful document to add to the context of an LLM to turn it into a useful FastHTML assistant.

Let’s get started.

## FastHTML Basics

FastHTML is _just Python_. You can install it with `pip install python-fasthtml`. Extensions/components built for it can likewise be distriuted via PyPI or as simple Python files.

The core usage of FastHTML is to define routes, and then to define what to do at each route. This is similar to the FastAPI web framework (in fact we implemented much of the fuctionality to match the FastAPI usage examples), but where FastAPI focuses on returning JSON data to build APIs, FastHTML focuses on returning HTML data.

Here’s a simple FastHTML app that returns a “Hello, World” message:

```
from fasthtml import FastHTML

app = FastHTML()

@app.get("/")
def home():
    return "<h1>Hello, World</h1>"
```

To run this app, place it in a file, say `app.py`, and then run it with `uvicorn app:app --reload`. You’ll see a message like this:

```
INFO:     Will watch for changes in these directories: ['/home/jonathan/fasthtml-example']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [871942] using WatchFiles
INFO:     Started server process [871945]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

If you navigate to http://127.0.0.1:8000 in a browser, you’ll see your “Hello, World”. If you edit the `app.py` file and save it, the server will reload and you’ll see the updated message when you refresh the page in your browser.

## Constructing HTML

Notice we wrote some HTML in the previous example. We don’t want to do that! Some web frameworks require that you learn HTML, CSS, JavaScript AND some templating language AND python. We want to do as much as possible with just one language. Fortunately, the Python module fastcore.xml has all we need for constructing HTML from Python, and FastHTML includes all the tags you need to get started. For example:

```
from fasthtml.common import *
page = Html(
    Head(Title('Some page')),
    Body(Div('Some text, ', A('A link', href='https://example.com'), Img(src="https://placehold.co/200"), cls='myclass')))
print(to_xml(page))
```

```
<!doctype html></!doctype>

<html>
  <head>
    <title>Some page</title>
  </head>
  <body>
    <div class="myclass">
Some text, 
      <a href="https://example.com">A link</a>
      <img src="https://placehold.co/200">
    </div>
  </body>
</html>

```

```
show(page)
```

Some page

Some text, A link

If that `import *` worries you, you can always import only the tags you need.

FastHTML is smart enough to know about fastcore.xml, and so you don’t need to use the `to_xml` function to convert your FT objects to HTML. You can just return them as you would any other Python object. For example, if we modify our previous example to use fastcore.xml, we can return an FT object directly:

```
app = FastHTML()

@app.get("/")
def home():
    return Div(H1('Hello, World'), P('Some text'), P('Some more text'))
```

This will render the HTML in the browser.

For debugging, you can right-click on the rendered HTML in the browser and select “Inspect” to see the underlying HTML that was generated. There you’ll also find the ‘network’ tab, which shows you the requests that were made to render the page. Refresh and look for the request to `127.0.0.1` \- and you’ll see it’s just a `GET` request to `/`, and the response body is the HTML you just returned.

You can also use Starlette’s `TestClient` to try it out in a notebook:

```
from starlette.testclient import TestClient
client = TestClient(app)
r = client.get("/")
r.text
```

```
'<!doctype html></!doctype>\n\n<html>\n  <head>\n    <title>FastHTML page</title>\n    <meta charset="utf-8"></meta>\n    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"></meta>\n    <script src="https://unpkg.com/htmx.org@next/dist/htmx.min.js"></script>\n    <script src="https://cdn.jsdelivr.net/gh/answerdotai/[email protected]/surreal.js"></script>\n    <script src="https://cdn.jsdelivr.net/gh/gnat/css-scope-inline@main/script.js"></script>\n  </head>\n  <body>\n<div>\n  <h1>Hello, World</h1>\n  <p>Some text</p>\n  <p>Some more text</p>\n</div>\n  </body>\n</html>\n'
```

FastHTML wraps things in an Html tag if you don’t do it yourself (unless the request comes from htmx, in which case you get the element directly). See the section ‘FT objects and HTML’ for more on creating custom components or adding HTML rendering to existing python objects. To give the page a non-default title, return a Title before your main content:

```
app = FastHTML()

@app.get("/")
def home():
    return Title("Page Demo"), Div(H1('Hello, World'), P('Some text'), P('Some more text'))

client = TestClient(app)
print(client.get("/").text)
```

```
<!doctype html></!doctype>

<html>
  <head>
    <title>Page Demo</title>
    <meta charset="utf-8"></meta>
    <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"></meta>
    <script src="https://unpkg.com/htmx.org@next/dist/htmx.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/answerdotai/[email protected]/surreal.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/gnat/css-scope-inline@main/script.js"></script>
  </head>
  <body>
<div>
  <h1>Hello, World</h1>
  <p>Some text</p>
  <p>Some more text</p>
</div>
  </body>
</html>

```

We’ll use this pattern often in the examples to follow.

## Defining Routes

The HTTP protocol defines a number of methods (‘verbs’) to send requests to a server. The most common are GET, POST, PUT, DELETE, and HEAD. We saw ‘GET’ in action before - when you navigate to a URL, you’re making a GET request to that URL. We can do different things on a route for different HTTP methods. For example:

```
@app.route("/", methods='get')
def home():
    return H1('Hello, World')

@app.route("/", methods=['post', 'put'])
def post_or_put():
    return "got a POST or PUT request"
```

This says that when someone navigates to the root URL “/” (i.e. sends a GET request), they will see the big “Hello, World” heading. When someone submits a POST or PUT request to the same URL, the server should return the string “got a post or put request”.

Aside: You can test the POST request with `curl -X POST http://127.0.0.1:8000 -d "some data"`. This sends some data to the server, you should see the response “got a post or put request” printed in the terminal.

There are a few other ways you can specify the route+method - FastHTML has `.get`, `.post`, etc. as shorthand for `route(..., methods=['get'])`, etc.

```
@app.get("/")
def my_function():
    return "Hello World from a GET request"
```

Or you can use the `@app.route` decorator without a method but specify the method with the name of the function. For example:

```
@app.route("/")
def post():
    return "Hello World from a POST request"
```

```
client.post("/").text
```

```
'Hello World from a POST request'
```

You’re welcome to pick whichever style you prefer. Using routes let’s you show different content on different pages - ‘/home’, ‘/about’ and so on. You can also respond differently to different kinds of requests to the same route, as we shown above. You can also pass data via the route:

```
@app.get("/greet/{nm}")
def greet(nm:str):
    return f"Good day to you, {nm}!"

client.get("/greet/Dave").text
```

```
'Good day to you, Dave!'
```

More on this in the ‘More on Routing and Requests’ section, which goes deeper into the different ways to get information from a request.

## Styling Basics

Plain HTML probably isn’t quite what you imagine when you visualize your beautiful web app. CSS is the go-to language for styling HTML. But again, we don’t want to learn extra languages unless we absolutely have to! Fortunately, there are ways to get much more visually appealing sites by relying on the hard work of others, using existing CSS libraries. One of our favourites is PicoCSS. To add a CSS file to HTML, you can use the `<link>` tag. Since we typically want things like CSS styling on all pages of our app, FastHTML lets you add shared headers when you define your app. And it already has `picolink` defined for convenience. As per the pico docs, we put all of our content inside a `<main>` tag with a class of `container`:

```
from fasthtml import *
# App with custom styling to override the pico defaults
css = Style(':root { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}')
app = FastHTML(hdrs=(picolink, css))

@app.route("/")
def get():
    return Title("Hello World"), Main(H1('Hello, World'), cls="container")
```

Aside: We’re returning a tuple here (a title and the main page). This is needed to tell FastHTML to turn the main body into a full HTML page that includes the headers (including the pico link and our custom css) which we passed in.

You can check out the Pico examples page to see how different elements will look. If everything is working, the page should now render nice text with our custom font, and it should respect the user’s light/dark mode preferences too.

If you want to override the default styles or add more custom CSS, you can do so by adding a `<style>` tag to the headers as shown above. So you are allowed to write CSS to your heart’s content - we just want to make sure you don’t necessarily have to! Later on we’ll see examples using other component libraries and tailwind css to do more fancy styling things, along with tips to get an LLM to write all those fiddly bits so you don’t have to.

## Web Page -> Web App

Showing content is all well and good, but we typically expect a bit more _interactivity_ from something calling itself a web app! So, let’s add a few different pages, and use a form to let users add messages to a list:

```
app = FastHTML()
messages = ["This is a message, which will get rendered as a paragraph"]

@app.get("/")
def home():
    return Main(H1('Messages'), 
                *[P(msg) for msg in messages],
                A("Link to Page 2 (to add messages)", href="/page2"))

@app.get("/page2")
def page2():
    return Main(P("Add a message with the form below:"),
                Form(Input(type="text", name="data"),
                     Button("Submit"),
                     action="/", method="post"))

@app.post("/")
def add_message(data:str):
    messages.append(data)
    return home()
```

We re-render the entire homepage to show the newly added message. This is fine, but modern web apps often don’t re-render the entire page, they just update a part of the page. In fact even very complicated applications are often implemented as ‘Single Page Apps’ (SPAs). This is where HTMX comes in.

## HTMX

HTMX addresses some key limitations of HTML. In vanilla HTML, links can trigger a GET request to show a new page, and forms can send requests containing data to the server. A lot of ‘Web 1.0’ design revolved around ways to use these to do everything we wanted. But why should only _some_ elements be allowed to trigger requests? And why should we refresh the _entire page_ with the result each time one does? HTMX extends HTML to allow us to trigger requests from _any_ element on all kinds of events, and to update a part of the page without refreshing the entire page. It’s a powerful tool for building modern web apps.

It does this by adding attributes to HTML tags to make them do things. For example, here’s a page with a counter and a button that increments it:

```
app = FastHTML()

count = 0

@app.get("/")
def home():
    return Title("Count Demo"), Main(
        H1("Count Demo"),
        P(f"Count is set to {count}", id="count"),
        Button("Increment", hx_post="/increment", hx_target="#count", hx_swap="innerHTML")
    )

@app.post("/increment")
def increment():
    print("incrementing")
    global count
    count += 1
    return f"Count is set to {count}"
```

The button triggers a POST request to `/increment` (since we set `hx_post="increment"`), which increments the count and returns the new count. The `hx_target` attribute tells HTMX where to put the result. If no target is specified it replaces the element that triggered the request. The `hx_swap` attribute specifies how it adds the result to the page. Useful options are:

  * _`innerHTML`_ : Replace the target element’s content with the result.
  * _`outerHTML`_ : Replace the target element with the result.
  * _`beforebegin`_ : Insert the result before the target element.
  * _`beforeend`_ : Insert the result inside the target element, after its last child.
  * _`afterbegin`_ : Insert the result inside the target element, before its first child.
  * _`afterend`_ : Insert the result after the target element.

You can also use an hx_swap of `delete` to delete the target element regardless of response, or of `none` to do nothing.

By default, requests are triggered by the “natural” event of an element - click in the case of a button (and most other elements). You can also specify different triggers, along with various modifiers - see the HTMX docs for more.

This pattern of having elements trigger requests that modify or replace other elements is a key part of the HTMX philosophy. It takes a little getting used to, but once mastered it is extremely powerful.

### Replacing Elements Besides the Target

Sometimes having a single target is not enough, and we’d like to specify some additional elements to update or remove. In these cases, returning elements with an id that matches the element to be replaces and `hx_swap_oob='true'` will replace those elements too. We’ll use this in the next example to clear an input field when we submit a form.

## Full Example #1 - ToDo App

The canonical demo web app! A TODO list. Rather than create yet another variant for this tutorial, we recommend starting with this video tutorial from Jeremy:

image.png

We’ve made a number of variants of this app - so in addition to the version shown in the video you can browse this series of examples with increasing complexity, the heavily-commented “idiomatic” version here, and the example linked from the FastHTML homepage.

## Full Example #2 - Image Generation App

Let’s create an image generation app. We’d like to wrap a text-to-image model in a nice UI, where the user can type in a prompt and see a generated image appear. We’ll use a model hosted by Replicate to actually generate the images. Let’s start with the homepage, with a form to submit prompts and a div to hold the generated images:

```
# Main page
@app.get("/")
def get():
    inp = Input(id="new-prompt", name="prompt", placeholder="Enter a prompt")
    add = Form(Group(inp, Button("Generate")), hx_post="/", target_id='gen-list', hx_swap="afterbegin")
    gen_list = Div(id='gen-list')
    return Title('Image Generation Demo'), Main(H1('Magic Image Generation'), add, gen_list, cls='container')
```

Submitting the form will trigger a POST request to `/`, so next we need to generate an image and add it to the list. One problem: generating images is slow! We’ll start the generation in a separate thread, but this now surfaces a different problem: we want to update the UI right away, but our image will only be ready a few seconds later. This is a common pattern - think about how often you see a loading spinner online. We need a way to return a temporary bit of UI which will eventually be replaced by the final image. Here’s how we might do this:

```
def generation_preview(id):
    if os.path.exists(f"gens/{id}.png"):
        return Div(Img(src=f"/gens/{id}.png"), id=f'gen-{id}')
    else:
        return Div("Generating...", id=f'gen-{id}', 
                   hx_post=f"/generations/{id}",
                   hx_trigger='every 1s', hx_swap='outerHTML')

@app.post("/generations/{id}")
def get(id:int): return generation_preview(id)

@app.post("/")
def post(prompt:str):
    id = len(generations)
    generate_and_save(prompt, id)
    generations.append(prompt)
    clear_input =  Input(id="new-prompt", name="prompt", placeholder="Enter a prompt", hx_swap_oob='true')
    return generation_preview(id), clear_input

@threaded
def generate_and_save(prompt, id): ... 
```

The form sends the prompt to the `/` route, which starts the generation in a separate thread then returns two things:

  * A generation preview element that will be added to the top of the `gen-list` div (since that is the target_id of the form which triggered the request)
  * An input field that will replace the form’s input field (that has the same id), using the hx_swap_oob=‘true’ trick. This clears the prompt field so the user can type another prompt.

The generation preview first returns a temporary “Generating…” message, which polls the `/generations/{id}` route every second. This is done by setting hx_post to the route and hx_trigger to ‘every 1s’. The `/generations/{id}` route returns the preview element every second until the image is ready, at which point it returns the final image. Since the final image replaces the temporary one (hx_swap=‘outerHTML’), the polling stops running and the generation preview is now complete.

This works nicely - the user can submit several prompts without having to wait for the first one to generate, and as the images become available they are added to the list. You can see the full code of this version here.

### Again, with Style

The app is functional, but can be improved. The next version adds more stylish generation previews, lays out the images in a grid layout that is responsive to different screen sizes, and adds a database to track generations and make them persistent. The database part is very similar to the todo list example, so let’s just quickly look at how we add the nice grid layout. This is what the result looks like:

image.png

Step one was looking around for existing components. The Pico CSS library we’ve been using has a rudimentary grid but recommends using an alternative layout system. One of the options listed was Flexbox.

To use Flexbox you create a “row” with one or more elements. You can specify how wide things should be with a specific syntax in the class name. For example, `col-xs-12` means a box that will take up 12 columns (out of 12 total) of the row on extra small screens, `col-sm-6` means a column that will take up 6 columns of the row on small screens, and so on. So if you want four columns on large screens you would use `col-lg-3` for each item (i.e. each item is using 3 columns out of 12).

```
<div class="row">
    <div class="col-xs-12">
        <div class="box">This takes up the full width</div>
    </div>
</div>
```

This was non-intuitive to me. Thankfully ChatGPT et al know web stuff quite well, and we can also experiment in a notebook to test things out:

```
grid = Html(
    Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/flexboxgrid/6.3.1/flexboxgrid.min.css", type="text/css"),
    Div(
        Div(Div("This takes up the full width", cls="box", style="background-color: #800000;"), cls="col-xs-12"),
        Div(Div("This takes up half", cls="box", style="background-color: #008000;"), cls="col-xs-6"),
        Div(Div("This takes up half", cls="box", style="background-color: #0000B0;"), cls="col-xs-6"),
        cls="row", style="color: #fff;"
    )
)
show(grid)
```

This takes up the full width

This takes up half

This takes up half

Aside: when in doubt with CSS stuff, add a background color or a border so you can see what’s happening!

Translating this into our app, we have a new homepage with a div (class=“row”) to store the generated images / previews, and a `generation_preview` function that returns boxes with the appropriate classes and styles to make them appear in the grid. I chose a layout with different numbers of columns for different screen sizes, but you could also _just_ specify the `col-xs` class if you wanted the same layout on all devices.

```
gridlink = Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/flexboxgrid/6.3.1/flexboxgrid.min.css", type="text/css")
app = FastHTML(hdrs=(picolink, gridlink))

# Main page
@app.get("/")
def get():
    inp = Input(id="new-prompt", name="prompt", placeholder="Enter a prompt")
    add = Form(Group(inp, Button("Generate")), hx_post="/", target_id='gen-list', hx_swap="afterbegin")
    gen_containers = [generation_preview(g) for g in gens(limit=10)] # Start with last 10
    gen_list = Div(*gen_containers[::-1], id='gen-list', cls="row") # flexbox container: class = row
    return Title('Image Generation Demo'), Main(H1('Magic Image Generation'), add, gen_list, cls='container')

# Show the image (if available) and prompt for a generation
def generation_preview(g):
    grid_cls = "box col-xs-12 col-sm-6 col-md-4 col-lg-3"
    image_path = f"{g.folder}/{g.id}.png"
    if os.path.exists(image_path):
        return Div(Card(
                       Img(src=image_path, alt="Card image", cls="card-img-top"),
                       Div(P(B("Prompt: "), g.prompt, cls="card-text"),cls="card-body"),
                   ), id=f'gen-{g.id}', cls=grid_cls)
    return Div(f"Generating gen {g.id} with prompt {g.prompt}", 
            id=f'gen-{g.id}', hx_get=f"/gens/{g.id}", 
            hx_trigger="every 2s", hx_swap="outerHTML", cls=grid_cls)
```

You can see the final result in main.py in the `image_app_simple` example directory, along with info on deploying it (tl;dr don’t!). We’ve also deployed a version that only shows _your_ generations (tied to browser session) and has a credit system to save our bank accounts. You can access that here. Now for the next question: how do we keep track of different users?

### Again, with Sessions

At the moment everyone sees all images! How do we keep some sort of unique identifier tied to a user? Before going all the way to setting up users, login pages etc., let’s look at a way to at least limit generations to the user’s _session_. You could do this manually with cookies. For convenience and security, fasthtml (via Starlette) has a special mechanism for storing small amounts of data in the user’s browser via the `session` argument to your route. This acts like a dictionary and you can set and get values from it. For example, here we look for a `session_id` key, and if it doesn’t exist we generate a new one:

```
@app.get("/")
def get(session):
    if 'session_id' not in session: session['session_id'] = str(uuid.uuid4())
    return H1(f"Session ID: {session['session_id']}")
```

Refresh the page a few times - you’ll notice that the session ID remains the same. If you clear your browsing data, you’ll get a new session ID. And if you load the page in a different browser (but not a different tab), you’ll get a new session ID. This will persist within the current browser, letting us use it as a key for our generations. As a bonus, someone can’t spoof this session id by passing it in another way (for example, sending a query parameter). Behind the scenes, the data _is_ stored in a browser cookie but it is signed with a secret key that stops the user or anyone nefarious from being able to tamper with it. The cookie is decoded back into a dictionary by something called a middleware function, which we won’t cover here. All you need to know is that we can use this to store bits of state in the user’s browser.

In the image app example, we can add a `session_id` column to our database, and modify our homepage like so:

```
@app.get("/")
def get(session):
    if 'session_id' not in session: session['session_id'] = str(uuid.uuid4())
    inp = Input(id="new-prompt", name="prompt", placeholder="Enter a prompt")
    add = Form(Group(inp, Button("Generate")), hx_post="/", target_id='gen-list', hx_swap="afterbegin")
    gen_containers = [generation_preview(g) for g in gens(limit=10, where=f"session_id == '{session['session_id']}'")]
    ...
```

So we check if the session id exists in the session, add one if not, and then limit the generations shown to only those tied to this session id. We filter the database with a where clause - see TODO link Jeremy’s example for a more reliable to do this. The only other change we need to make is to store the session id in the database when a generation is made. You can check out this version here. You could instead write this app without relying on a database at all - simply storing the filenames of the generated images in the session, for example. But this more general approach of linking some kind of unique session identifier to users or data in our tables is a useful general pattern for more complex examples.

### Again, with Credits!

Generating images with replicate costs money. So next let’s add a pool of credits that get used up whenever anyone generates an image. To recover our lost funds, we’ll also set up a payment system so that generous users can buy more credits for everyone. You could modify this to let users buy credits tied to their session ID, but at that point you risk angry customers loosing their money after wiping their browser history, and should consider setting up proper account management :)

Taking payments with Stripe is intimidating but very doable. Here’s a tutorial that shows the general principle using Flask. As with other popular tasks in the web-dev world, ChatGPT knows a lot about Stripe - but you should exercise extra caution when writing code that handles money!

For the finished example we add the bare minimum:

  * A way to create a Stripe checkout session and redirect the user to the session URL
  * ‘Success’ and ‘Cancel’ routes to handle the result of the checkout
  * A route that listens for a webhook from Stripe to update the number of credits when a payment is made.

In a typical application you’ll want to keep track of which users make payments, catch other kinds of stripe events and so on. This example is more ‘this is possible, do your own research’ than ‘this is how you do it’. But hopefully it does illustrate the key idea: there is no magic here. Stripe (and many other technologies) relies on sending users to different routes and shuttling data back and forth in requests. And we know how to do that!

## More on Routing and Request Parameters

There are a number of ways information can be passed to the server. When you specify arguments to a route, FastHTML will search the request for values with the same name, and convert them to the correct type. In order, it searchs

  * The path parameters
  * The query parameters
  * The cookies
  * The headers
  * The session
  * Form data

There are also a few special arguments

  * `request` (or any prefix like `req`): gets the raw Starlette `Request` object
  * `session` (or any prefix like `sess`): gets the session object
  * `auth`
  * `htmx`
  * `app`

In this section let’s quickly look at some of these in action.

```
app = FastHTML()
cli = TestClient(app)
```

Part of the route (path parameters):

```
@app.get('/user/{nm}')
def _(nm:str): return f"Good day to you, {nm}!"

cli.get('/user/jph').text
```

```
'Good day to you, jph!'
```

Matching with a regex:

```
reg_re_param("imgext", "ico|gif|jpg|jpeg|webm")

@app.get(r'/static/{path:path}{fn}.{ext:imgext}')
def get_img(fn:str, path:str, ext:str): return f"Getting {fn}.{ext} from /{path}"

cli.get('/static/foo/jph.ico').text
```

```
'Getting jph.ico from /foo/'
```

Using an enum (try using a string that isn’t in the enum):

```
ModelName = str_enum('ModelName', "alexnet", "resnet", "lenet")

@app.get("/models/{nm}")
def model(nm:ModelName): return nm

print(cli.get('/models/alexnet').text)
```

```
alexnet
```

Casting to a Path:

```
@app.get("/files/{path}")
def txt(path: Path): return path.with_suffix('.txt')

print(cli.get('/files/foo').text)
```

```
foo.txt
```

An integer with a default value:

```
fake_db = [{"name": "Foo"}, {"name": "Bar"}]

@app.get("/items/")
def read_item(idx:int|None = 0): return fake_db[idx]

print(cli.get('/items/?idx=1').text)
```

```
{"name":"Bar"}
```

```
print(cli.get('/items/').text)
```

```
{"name":"Foo"}
```

Boolean values (takes anything “truthy” or “falsy”):

```
@app.get("/booly/")
def booly(coming:bool=True): return 'Coming' if coming else 'Not coming'

print(cli.get('/booly/?coming=true').text)
```

```
Coming
```

```
print(cli.get('/booly/?coming=no').text)
```

```
Not coming
```

Getting dates:

```
@app.get("/datie/")
def datie(d:date): return d

date_str = "17th of May, 2024, 2p"
print(cli.get(f'/datie/?d={date_str}').text)
```

```
2024-05-17 14:00:00
```

Matching a dataclass:

```
from dataclasses import dataclass, asdict

@dataclass
class Bodie:
    a:int;b:str

@app.route("/bodie/{nm}")
def post(nm:str, data:Bodie):
    res = asdict(data)
    res['nm'] = nm
    return res

cli.post('/bodie/me', data=dict(a=1, b='foo')).text
```

```
'{"a":1,"b":"foo","nm":"me"}'
```

### Cookies

Cookies can be set via a Starlette Response object, and can be read back by specifying the name:

```
from datetime import datetime

@app.get("/setcookie")
def setc(req):
    now = datetime.now()
    res = Response(f'Set to {now}')
    res.set_cookie('now', str(now))
    return res

cli.get('/setcookie').text
```

```
'Set to 2024-07-20 23:14:54.364793'
```

```
@app.get("/getcookie")
def getc(now:date): return f'Cookie was set at time {now.time()}'

cli.get('/getcookie').text
```

```
'Cookie was set at time 23:14:54.364793'
```

### User Agent and HX-Request

An argument of `user_agent` will match the header `User-Agent`. This holds for special headers like `HX-Request` (used by HTMX to signal when a request comes from an HTMX request) - the general pattern is that “-” is replaced with “_” and strings are turned to lowercase.

```
@app.get("/ua")
async def ua(user_agent:str): return user_agent

cli.get('/ua', headers={'User-Agent':'FastHTML'}).text
```

```
'FastHTML'
```

```
@app.get("/hxtest")
def hxtest(htmx): return htmx.request

cli.get('/hxtest', headers={'HX-Request':'1'}).text
```

```
'1'
```

### Starlette Requests

If you add an argument called `request`(or any prefix of that, for example `req`) it will be populated with the Starlette `Request` object. This is useful if you want to do your own processing manually. For example, although FastHTML will parse forms for you, you could instead get form data like so:

```
@app.get("/form")
async def form(request:Request):
    form_data = await request.form()
    a = form_data.get('a')
```

See the Starlette docs for more information on the `Request` object.

### Starlette Responses

You can return a Starlette Response object from a route to control the response. For example:

```
@app.get("/redirect")
def redirect():
    return RedirectResponse(url="/")
```

We used this to set cookies in the previous example. See the Starlette docs for more information on the `Response` object.

### Static Files

We often want to serve static files like images. This is easily done! For common file types (images, CSS etc) we can create a route that returns a Starlette `FileResponse` like so:

```
# For images, CSS, etc.
@app.get("/{fname:path}.{ext:static}")
def static(fname: str, ext: str):
  return FileResponse(f'{fname}.{ext}')
```

You can customize it to suit your needs (for example, only serving files in a certain directory). You’ll notice some variant of this route in all our complete examples - even for apps with no static files the browser will typically request a `/favicon.ico` file, for example, and as the astute among you will have noticed this has sparked a bit of competition between Johno and Jeremy regarding which country flag should serve as the default!

### WebSockets

For certain applications such as multiplayer games, websockets can be a powerful feature. Luckily HTMX and FastHTML has you covered! Simply specify that you wish to include the websocket header extension from HTMX:

```
app = FastHTML(ws_hdr=True)
rt = app.route
```

With that, you are now able to specify the different websocket specific HTMX goodies. For example, say we have a website we want to setup a websocket, you can simply:

```
def mk_inp(): return Input(id='msg')

@rt('/')
async def get(request):
    cts = Div(
        Div(id='notifications'),
        Form(mk_inp(), id='form', ws_send=True),
        hx_ext='ws', ws_connect='/ws')
    return Titled('Websocket Test', cts)
```

And this will setup a connection on the route `/ws` along with a form that will send a message to the websocket whenever the form is submitted. Let’s go ahead and handle this route:

```
@app.ws('/ws')
async def ws(msg:str, send):
    await send(Div('Hello ' + msg, id="notifications"))
    await sleep(2)
    return Div('Goodbye ' + msg, id="notifications"), mk_inp()
```

One thing you might have noticed is a lack of target id for our websocket trigger for swapping HTML content. This is because HTMX always swaps content with websockets with Out of Band Swaps. Therefore, HTMX will look for the id in the returned HTML content from the server for determining what to swap. To send stuff to the client, you can either use the `send` parameter or simply return the content or both!

Now, sometimes you might want to perform actions when a client connects or disconnects such as add or remove a user from a player queue. To hook into these events, you can pass your connection or disconnection function to the `app.ws` decorator:

```
async def on_connect(send):
    print('Connected!')
    await send(Div('Hello, you have connected', id="notifications"))

async def on_disconnect(ws):
    print('Disconnected!')

@app.ws('/ws', conn=on_connect, disconn=on_disconnect)
async def ws(msg:str, send):
    await send(Div('Hello ' + msg, id="notifications"))
    await sleep(2)
    return Div('Goodbye ' + msg, id="notifications"), mk_inp()
```

## Full Example #3 - Chatbot Example with DaisyUI Components

Let’s go back to the topic of adding components or styling beyond the simple PicoCSS examples so far. How might we adopt a component or framework? In this example, let’s build a chatbot UI leveraging the DaisyUI chat bubble. The final result will look like this:

image.png

At first glance, DaisyUI’s chat component looks quite intimidating. The examples look like this:

```
<div class="chat chat-start">
  <div class="chat-image avatar">
    <div class="w-10 rounded-full">
      <img alt="Tailwind CSS chat bubble component" src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
    </div>
  </div>
  <div class="chat-header">
    Obi-Wan Kenobi
    <time class="text-xs opacity-50">12:45</time>
  </div>
  <div class="chat-bubble">You were the Chosen One!</div>
  <div class="chat-footer opacity-50">
    Delivered
  </div>
</div>
<div class="chat chat-end">
  <div class="chat-image avatar">
    <div class="w-10 rounded-full">
      <img alt="Tailwind CSS chat bubble component" src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg" />
    </div>
  </div>
  <div class="chat-header">
    Anakin
    <time class="text-xs opacity-50">12:46</time>
  </div>
  <div class="chat-bubble">I hate you!</div>
  <div class="chat-footer opacity-50">
    Seen at 12:46
  </div>
</div>
```

We have several things going for us however.

  * ChatGPT knows DaisyUI and Tailwind (DaisyUI is a Tailwind component library)
  * We can build things up piece by piece with AI standing by to help.

https://h2x.answer.ai/ is a tool that can convert HTML to FT (fastcore.xml) and back, which is useful for getting a quick starting point when you have an HTML example to start from.

We can strip out some unnecessary bits and try to get the simplest possible example working in a notebook first:

```
# Loading tailwind and daisyui
headers = (Script(src="https://cdn.tailwindcss.com"),
           Link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/[email protected]/dist/full.min.css"))

# Displaying a single message
d = Div(
    Div("Chat header here", cls="chat-header"),
    Div("My message goes here", cls="chat-bubble chat-bubble-primary"),
    cls="chat chat-start"
)
# show(Html(*headers, d)) # uncomment to view
```

Now we can extend this to render multiple messages, with the message being on the left (`chat-start`) or right (`chat-end`) depending on the role. While we’re at it, we can also change the color (`chat-bubble-primary`) of the message and put them all in a `chat-box` div:

```
messages = [
    {"role":"user", "content":"Hello"},
    {"role":"assistant", "content":"Hi, how can I assist you?"}
]

def ChatMessage(msg):
    return Div(
        Div(msg['role'], cls="chat-header"),
        Div(msg['content'], cls=f"chat-bubble chat-bubble-{'primary' if msg['role'] == 'user' else 'secondary'}"),
        cls=f"chat chat-{'end' if msg['role'] == 'user' else 'start'}")

chatbox = Div(*[ChatMessage(msg) for msg in messages], cls="chat-box", id="chatlist")

# show(Html(*headers, chatbox)) # Uncomment to view
```

Next, it was back to the ChatGPT to tweak the chat box so it wouldn’t grow as messages were added. I asked:

```
"I have something like this (it's working now) 
[code]
The messages are added to this div so it grows over time. 
Is there a way I can set it's height to always be 80% of the total window height with a scroll bar if needed?"
```

Based on this query GPT4o helpfully shared that “This can be achieved using Tailwind CSS utility classes. Specifically, you can use h-[80vh] to set the height to 80% of the viewport height, and overflow-y-auto to add a vertical scroll bar when needed.”

To put it another way: none of the CSS classes in the following example were written by a human, and what edits I did make were informed by advice from the AI that made it relatively painless!

The actual chat functionality of the app is based on our claudette library. As with the image example, we face a potential hiccup in that getting a response from an LLM is slow. We need a way to have the user message added to the UI immadiately, and then have the response added once it’s available. We could do something similar to the image generation example above, or use websockets. Check out the full example for implementations of both, along with further details.

## Full Example #4 - Multiplayer Game of Life Example with Websockets

Let’s see how we can implement a collaborative website using Websockets in FastHTML. To showcase this, we will use the famous Conway’s Game of Life, which is a game that takes place in a grid world. Each cell in the grid can be either alive or dead. The cell’s state is initially given by a user before the game is started and then evolves through the iteration of the grid world once the clock starts. Whether a cell’s state will change from the previous state depends on simple rules based on its neighboring cells’ states. Here is the standard Game of Life logic implemented in Python courtesy of ChatGPT:

```
grid = [[0 for _ in range(20)] for _ in range(20)]}
def update_grid(grid: list[list[int]]) -> list[list[int]]:
    new_grid = [[0 for _ in range(20)] for _ in range(20)]
    def count_neighbors(x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]): count += grid[nx][ny]
        return count
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(i, j)
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3: new_grid[i][j] = 0
                else: new_grid[i][j] = 1
            elif neighbors == 3: new_grid[i][j] = 1
    return new_grid
```

This would be a very pooring game if ran since the initial state of everything would stay dead. Therefore, we need a way of letting the user give an initial state before starting the game. FastHTML to the rescue!

```
def Grid():
    cells = []
    for y, row in enumerate(game_state['grid']):
        for x, cell in enumerate(row):
            cell_class = 'alive' if cell else 'dead'
            cell = Div(cls=f'cell {cell_class}', hx_put='/update', hx_vals={'x': x, 'y': y}, hx_swap='none', hx_target='#gol', hx_trigger='click')
            cells.append(cell)
    return Div(*cells, id='grid')

@rt('/update')
async def put(x: int, y: int):
    grid[y][x] = 1 if grid[y][x] == 0 else 0
```

Above is a component for representing the game’s state that the user can interact with and update on the server using cool HTMX features such as `hx_vals` for determining which cell was clicked to make it dead or alive. Now, you probably noticed that the HTTP request in this case is a PUT request, which does not return anything and this means our client’s view of the grid world and the server’s game state will immediately become out of sync :(. We could of course just return a new Grid component with the updated state, but that would only work for a single client, if we had more, they quickly get out of sync with each other and the server. Now Websockets to the rescue!

Websockets are a way for the server to keep a persistent connection with clients and send data to the client without explictly being requested for information, which is not possible with HTTP. Luckily FastHTML and HTMX work well with Websockets. Simply state you wish to use websockets for your app and define a websocket route:

```
...
app = FastHTML(hdrs=(picolink, gridlink, css, htmx_ws), ws_hdr=True)

player_queue = []
async def update_players():
    for i, player in enumerate(player_queue):
        try: await player(Grid())
        except: player_queue.pop(i)
async def on_connect(send): player_queue.append(send)
async def on_disconnect(send): await update_players()

@app.ws('/gol', conn=on_connect, disconn=on_disconnect)
async def ws(msg:str, send): pass

def Home(): return Title('Game of Life'), Main(gol, Div(Grid(), id='gol', cls='row center-xs'), hx_ext="ws", ws_connect="/gol")

@rt('/update')
async def put(x: int, y: int):
    grid[y][x] = 1 if grid[y][x] == 0 else 0
    await update_players()
...
```

Here we simply keep track of all the players that have connected or disconnected to our site and when an update ocurrs, we send updates to all the players still connected via websockets. Via HTMX, you are still simply exchanging HTML from the server to the client and will swap in the content based on how you setup your `hx_swap` attribute. There is only one difference, that being all swaps are OOB. You can find more information on the HTMX websocket extension documentation page here. You can find a full fledge hosted example of this app here.

## FT objects and HTML

These FT objects create a ‘FastTag’ structure [tag,children,attrs] for `toxml()`. When we call `Div(...)`, the elements we pass in are the children. Attributes are passed in as keywords. `class` and `for` are special words in python, so we use `cls`, `klass` or `_class` instead of `class` and `fr` or `_for` instead of `for`. Note these objects are just 3-element lists - you can create custom ones too as long as they’re also 3-element lists. Alternately, leaf nodes can be strings instead (which is why you can do `Div('some text')`). If you pass something that isn’t a 3-element list or a string, it will be converted to a string using str()… unless (our final trick) you define a `__ft__` method that will run before str(), so you can render things a custom way.

For example, here’s one way we could make a custom class that can be rendered into HTML:

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __ft__(self):
        return ['div', [f'{self.name} is {self.age} years old.'], {}]

p = Person('Jonathan', 28)
print(to_xml(Div(p, "more text", cls="container")))
```

```
<div class="container">
  <div>Jonathan is 28 years old.</div>
more text
</div>

```

In the examples, you’ll see we often patch in `__ft__` methods to existing classes to control how they’re rendered. For example, if Person didn’t have a `__ft__` method or we wanted to override it, we could add a new one like this:

```
from fastcore.all import patch

@patch
def __ft__(self:Person):
    return Div("Person info:", Ul(Li("Name:",self.name), Li("Age:", self.age)))

show(p)
```

Person info:

  * Name: Jonathan 
  * Age: 28 

Some tags from fastcore.xml are overwritten by fasthtml.core and a few are furter extended by fasthtml.xtend using this method. Over time, we hope to see others developing custom components too, giving us a larger and larger ecosystem of reusable components.

## Custom Scripts and Styling

There are many popular JavaScript and CSS libraries that can be used via a simple `Script` or `Style` tag. But in some cases you will need to write more custom code. FastHTML’s js.py contains a few examples that may be useful as reference.

For example, to use the marked.js library to render markdown in a div, including in components added after the page has loaded via htmx, we do something like this:

```
import { marked } from "https://cdn.jsdelivr.net/npm/marked/lib/marked.esm.js";
import { proc_htmx} from "https://cdn.jsdelivr.net/gh/answerdotai/fasthtml-js/fasthtml.js";
proc_htmx('%s', e => e.innerHTML = marked.parse(e.textContent));
```

`proc_htmx` is a shortcut we wrote that we wrote to apply a function to elements matching a selector, including the element that triggered the event. Here’s the code for reference:

```
export function proc_htmx(sel, func) {
  htmx.onLoad(elt => {
    const elements = htmx.findAll(elt, sel);
    if (elt.matches(sel)) elements.unshift(elt)
    elements.forEach(func);
  });
}
```

The AI Pictionary example uses a larger chunk of custom JavaScript to handle the drawing canvas. It’s a good example of the type of application where running code on the client side makes the most sense, but still shows how you can integrate it with FastHTML on the server side to add functionality (like the AI responses) easily.

Adding styling with custom CSS and libraries such as tailwind is done the same way we add custom JavaScript. The doodle example uses Doodle.CSS to style the page in a quirky way.

## Deploying Your App

We can deply FastHTML almost anywhere you can deploy python apps. We’ve tested Railway, Replit, HuggingFace, and PythonAnywhere.

### Railway

  1. Install the Railway CLI and sign up for an account.
  2. Set up a folder with our app as `main.py`
  3. In the folder, run `railway login`.
  4. Use the `fh_railway_deploy` script to deploy our project:

```
fh_railway_deploy MY_APP_NAME
```

What the script does for us:

  4. Do we have an existing railway project? 
     * Yes: Link the project folder to our existing Railway project.
     * No: Create a new Railway project.
  5. Deploy the project. We’ll see the logs as the service is built and run!
  6. Fetches and displays the URL of our app.
  7. By default, mounts a `/app/data` folder on the cloud to our app’s root folder. The app is run in `/app` by default, so from our app anything we store in `/data` will persist across restarts.

A final note about Railway: We can add secrets like API keys that can be accessed as environment variables from our apps via ‘Variables’. For example, for the image app (TODO link), we can add a `REPLICATE_API_KEY` variable, and then in `main.py` we can access it as `os.environ['REPLICATE_API_KEY']`.

### Replit

Fork https://replit.com/@johnowhitaker/FastHTML-Example for a minimal example you can edit to your heart’s content. `.replit` has been edited to add the right run command (`run = ["uvicorn", "main:app", "--reload"]`) and to set up the ports correctly. FastHTML was installed with `poetry add python-fasthtml`, you can add additional packages as needed in the same way. Running the app in Replit will show you a webview, but you may need to open in a new tab for all features (such as cookies) to work. When you’re ready, you can deploy your app by clicking the ‘Deploy’ button. You pay for usage - for an app that is mostly idle the cost is usually a few cents per month.

You can store secrets like API keys via the ‘Secrets’ tab in the Replit project settings.

### HuggingFace

Follow the instructions in this repository to deploy to HuggingFace spaces.

## Where Next?

We’ve covered a lot of ground here! Hopefully this has given you plenty to work with in building your own FastHTML apps. If you have any questions, feel free to ask in the #fasthtml Discord channel (in the fastai community Discord). You can look through the other examples in the fasthtml-example repository for more ideas, and keep an eye on Jeremy’s YouTube channel where we’ll be releasing a number of “dev chats” related to FastHTML in the near future.

  * __Report an issue
  * Home
  * Learn

  * __
  * __

  1. Explanations
  2. **ft** Components

  * Get Started

  * Tutorials __

    * FastHTML By Example

    * Web Devs Quickstart

    * JS App Walkthrough

    * BYO Blog

    * Deploying FastHTML Apps

  * Explanations __

    * **ft** Components

    * Routes

  * Reference __

    * Live Reloading

  * Source __

    * Core

    * Components

    * Component extensions

    * Command Line Tools

## On this page

  * How FastHTML names ft components
  * Default **ft** components
  * The `fasthtml.ft` Namespace
  * Attributes

  * __Report an issue

  1. Explanations
  2. **ft** Components

# **ft** Components

_In a nutshell,**ft** components turn Python objects into HTML._

ft, or ‘FastTags’, are the display component of FastHTML. In fact, the use of the word “components” in the context of FastHTML is often synonymous with ft.

For example, when we look at a FastHTML app, in particular the views, as well as various functions and other objects, we see something like the code snippet below. It’s return statement that we want to pay attention to:

```
from fasthtml.common import *

def example():
    # The code below is a set of ft components
    return Div(
            H1("FastHTML APP"),
            P("Let's do this"),
            cls="go"
    )
```

Let’s go ahead and call our function and print the result:

```
example()
```

```
<div class="go">
  <h1>FastHTML APP</h1>
  <p>Let&#x27;s do this</p>
</div>
```

As you can see, when returned to the user from a Python callable like a function the ft components are transformed into their string representations of XML or XML-like content such as HTML. Or more concisely, _ft turns Python objects into HTML_.

Now that we know that ft components look and behave like we can begin to understand them. At their most fundamental level, ft components:

  1. Are Python callables, specifically functions, classes, methods of classes, lambda functions, and anything else called with parenthesis that returns a value.
  2. Return a sequence of values which has three elements: 
    1. The tag to be generated
    2. The content of the tag, which is a tuple of strings/tuples. If a tuple it is the three element structure of an ft component
    3. A dictionary of XML attributes and their values
  3. FastHTML’s default ft components words begin with an uppercase letter. Examples include `Title()`, `Ul()`, and `Div()` Custom components have included things like `BlogPost` and `CityMap`

## How FastHTML names ft components

When it comes to naming ft components, FastHTML appears to break from PEP8. Specifically, PEP8 specifies that when naming variables, functions and instantiated classes we use the `snake_case_pattern`. That is to say, lowercase with words seperated by underscores. However, FastHTML uses `PascalCase` for ft components.

There’s a couple of reasons for this:

  1. ft components can be made from any type of callable, so adhering to any one pattern doesn’t make much sense
  2. It makes for easier reading of FastHTML code, as anything that is PascalCase is probably an ft component

## Default **ft** components

FastHTML comes with over 150 **ft** components designed to accelerate web development. Most of these mirror HTML tags such as `<div>`, `<p>`, `<a>`, `<title`, and more. However, there are a number of extra tags added, including:

  * `Titled`, a combination of the `Title()` and `H1()` tags
  * `Socials`, renders popular social media tags

## The `fasthtml.ft` Namespace

Some people prefer to write code using namespaces while adhering to PEP8. If that’s a preference, projects can be coded using the `fasthtml.ft` namespace.

```
from fasthtml import ft

ft.Ul(
    ft.Li("one"),
    ft.Li("two"),
    ft.Li("three")
)
```

```
<ul>
  <li>one</li>
  <li>two</li>
  <li>three</li>
</ul>
```

## Attributes

This example demonstrates many important things to know about how ft components handle attributes.

```
#| echo: False
1Label(
    "Choose an option", 
    Select(
2        Option("one", value="1", selected=True),
3        Option("two", value="2", selected=False),
4        Option("three", value=3),
5        cls="selector",
6        _id="counter",
7        **{'@click':"alert('Clicked');"},
    ),
8    _for="counter",
)
```

1

     Line 1 demonstrates that FastHTML appreciates Labels surrounding their fields.
2

     On line 4, we can see that attributes set to the `boolean` value of `True` are rendered with just the name of the attribute
3

     On line 5, we demonstration that attributes set to the `boolean` value of `False` do not appear in the rendered output
4

     On line 6 is an example of how integers and other non-string values are in the rendered output are converted to strings
5

     Line 7 is where we set the HTML class using the `cls` argument. We use `cls` here as `class` is a reserved word in Python. During the rendering process this will be converted to the word “class”
6

     Line 9 demonstrates that any named argument passed into an ft component will have the leading underscore stripped away before rendering. Useful for handling reserved words in Python
7

     On line 10 we have an attribute name that cannot be represented as a python variable. We can use an unpacked `dict` in these cases to represent these values.
8

     The use of `_for` on line 12 is another demonstrated of an argument having the leading underscore stripped during render. We can also use `fr` as that will be expanded to `for`.

This renders the following HTML snippet:

```
Label(
    "Choose an option", 
    Select(
        Option("one", value="1", selected=True),
        Option("two", value="2", selected=False),
        Option("three", value=3),  # <4>,
        cls="selector",
        _id="counter",
        **{'@click':"alert('Clicked');"},
    ),
    _for="counter",
)
```

```
<label for="counter">
Choose an option
  <select id="counter" @click="alert(&#x27;Clicked&#x27;);" class="selector" name="counter">
    <option value="1" selected>one</option>
    <option value="2" >two</option>
    <option value="3">three</option>
  </select>
</label>
```

  * __Report an issue
  Behaviour in FastHTML apps is defined by routes. The syntax is largely the same as the wonderful FastAPI (which is what you should be using instead of this if you’re creating a JSON service. FastHTML is for mainly for making HTML web apps, not APIs).

Note that you need to include the types of your parameters, so that `FastHTML` knows what to pass to your function. Here, we’re just expecting a string:

```
from fasthtml.common import *
```

```
app = FastHTML()

@app.get('/user/{nm}')
def get_nm(nm:str): return f"Good day to you, {nm}!"
```

Normally you’d save this into a file such as main.py, and then run it in `uvicorn` using:

```
uvicorn main:app
```

However, for testing, we can use Starlette’s `TestClient` to try it out:

```
from starlette.testclient import TestClient
```

```
client = TestClient(app)
r = client.get('/user/Jeremy')
r
```

```
<Response [200 OK]>
```

TestClient uses `httpx` behind the scenes, so it returns a `httpx.Response`, which has a `text` attribute with our response body:

```
r.text
```

```
'Good day to you, Jeremy!'
```

In the previous example, the function name (`get_nm`) didn’t actually matter – we could have just called it `_`, for instance, since we never actually call it directly. It’s just called through HTTP. In fact, we often do call our functions `_` when using this style of route, since that’s one less thing we have to worry about naming.

An alternative approach to creating a route is to use `app.route` instead, in which case you make the function name the HTTP method you want. Since this is such a common pattern, you might like to give a shorter name to `app.route` – we normally use `rt`:

```
rt = app.route

@rt('/')
def post(): return "Going postal!"

client.post('/').text
```

```
'Going postal!'
```

## Unfinished

We haven’t yet written complete documentation of all of FastHTML’s routing features – until we add that, the best place to see all the available functionality is to look over the tests

  * __Report an issue
  When building your app it can be useful to view your changes in a web browser as you make them. FastHTML supports live reloading which means that it watches for any changes to your code and automatically refreshes the webpage in your browser.

To enable live reloading simply replace `FastHTML` in your app with `FastHTMLWithLiveReload`.

```
from fasthtml.common import *
app = FastHTMLWithLiveReload()
```

Then in your terminal run `uvicorn` with reloading enabled.

```
uvicorn: main:app --reload
```

**⚠️ Gotchas** \- A reload is only triggered when you save your changes. - `FastHTMLWithLiveReload` should only be used during development. - If your app spans multiple directories you might need to use the `--reload-dir` flag to watch all files in each directory. See the uvicorn docs for more info.

## Live reloading with `fast_app`

In development the `fast_app` function provides the same functionality. It instantiates the `FastHTMLWithLiveReload` class if you pass `live=True`:

```
**main.py**
```

```
from fasthtml.common import *

1app, rt = fast_app(live=True)

2serve()
```

1

     `fast_app()` instantiates the `FastHTMLWithLiveReload` class.
2

     `serve()` is a wrapper around a `uvicorn` call.

To run `main.py` in live reload mode, just do `python main.py`. We recommend turning off live reload when deploying your app to production.

  * __Report an issue
  This is the source code to fasthtml. You won’t need to read this unless you want to understand how things are built behind the scenes, or need full details of a particular API. The notebook is converted to the Python module fasthtml/core.py using nbdev.

## Imports and utils

```
import time

from IPython import display
from enum import Enum
from pprint import pprint

from fastcore.test import *
from starlette.testclient import TestClient
from starlette.requests import Headers
```

We write source code _first_ , and then tests come _after_. The tests serve as both a means to confirm that the code works and also serves as working examples. The first declared function, `is_typeddict`, is an example of this pattern.

* * *

source

### is_typeddict

>
```
>      is_typeddict (cls:type)
```

_Check if`cls` is a `TypedDict`_

```
class MyDict(TypedDict): name:str

assert is_typeddict(MyDict)
assert not is_typeddict({'a':1})
```

* * *

source

### is_namedtuple

>
```
>      is_namedtuple (cls)
```

_`True` is `cls` is a namedtuple type_

```
assert is_namedtuple(namedtuple('tst', ['a']))
assert not is_namedtuple(tuple)
```

* * *

source

### date

>
```
>      date (s:str)
```

_Convert`s` to a datetime_

```
date('2pm')
```

```
datetime.datetime(2024, 7, 29, 14, 0)
```

* * *

source

### snake2hyphens

>
```
>      snake2hyphens (s:str)
```

_Convert`s` from snake case to hyphenated and capitalised_

```
snake2hyphens("snake_case")
```

```
'Snake-Case'
```

* * *

source

### HtmxHeaders

>
```
>      HtmxHeaders (boosted:str|None=None, current_url:str|None=None,
>                   history_restore_request:str|None=None, prompt:str|None=None,
>                   request:str|None=None, target:str|None=None,
>                   trigger_name:str|None=None, trigger:str|None=None)
```

```
def test_request(url: str='/', headers: dict={}, method: str='get') -> Request:
    scope = {
        'type': 'http',
        'method': method,
        'path': url,
        'headers': Headers(headers).raw,
        'query_string': b'',
        'scheme': 'http',
        'client': ('127.0.0.1', 8000),
        'server': ('127.0.0.1', 8000),
    }
    receive = lambda: {"body": b"", "more_body": False}
    return Request(scope, receive)
```

```
h = test_request(headers=Headers({'HX-Request':'1'}))
_get_htmx(h.headers)
```

```
HtmxHeaders(boosted=None, current_url=None, history_restore_request=None, prompt=None, request='1', target=None, trigger_name=None, trigger=None)
```

* * *

source

### str2int

>
```
>      str2int (s)
```

_Convert`s` to an `int`_

```
str2int('1'),str2int('none')
```

```
(1, 0)
```

## Request and response

```
_fix_anno(Union[str,None]),_fix_anno(float)
```

```
(str, float)
```

```
_fix_anno(int)('1')
```

```
1
```

```
_fix_anno(list[int])(['1','2'])
```

```
[1, 2]
```

```
_fix_anno(list[int])('1')
```

```
[1]
```

```
d = dict(k=int, l=List[int])
_form_arg('k', "1", d)
```

```
1
```

```
_form_arg('l', "1", d)
```

```
[1]
```

```
_form_arg('l', ["1","2"], d)
```

```
[1, 2]
```

* * *

source

### HttpHeader

>
```
>      HttpHeader (k:str, v:str)
```

* * *

source

### form2dict

>
```
>      form2dict (form:starlette.datastructures.FormData)
```

_Convert starlette form data to a dict_

```
d = [('a',1),('a',2),('b',0)]
fd = FormData(d)
res = form2dict(fd)
test_eq(res['a'], [1,2])
test_eq(res['b'], 0)
```

```
async def f(req):
    def _f(p:HttpHeader): ...
    p = first(signature(_f).parameters.values())
    result = await _from_body(req, p)
    return JSONResponse(result.__dict__)

app = Starlette(routes=[Route('/', f, methods=['POST'])])
client = TestClient(app)

d = dict(k='value1',v=['value2','value3'])
response = client.post('/', data=d)
print(response.json())
```

```
{'k': 'value1', 'v': "['value2', 'value3']"}
```

```
def g(req, this:Starlette, a:str, b:HttpHeader): ...

async def f(req):
    a = await _wrap_req(req, signature(g).parameters)
    return Response(str(a))

app = Starlette(routes=[Route('/', f, methods=['POST'])])
client = TestClient(app)

response = client.post('/?a=1', data=d)
print(response.text)
```

```
[<starlette.requests.Request object>, <starlette.applications.Starlette object>, '1', HttpHeader(k='value1', v="['value2', 'value3']")]
```

* * *

source

### flat_xt

>
```
>      flat_xt (lst)
```

_Flatten lists, except for`FT`s_

```
x = FT('a',1)
flat_xt([x, x, [x,x]])
```

```
[['a', 1, {}], ['a', 1, {}], ['a', 1, {}], ['a', 1, {}]]
```

* * *

source

### Beforeware

>
```
>      Beforeware (f, skip=None)
```

_Initialize self. See help(type(self)) for accurate signature._

## Websockets

```
def on_receive(self, msg:str): return f"Message text was: {msg}"
c = _ws_endp(on_receive)
app = Starlette(routes=[WebSocketRoute('/', _ws_endp(on_receive))])

cli = TestClient(app)
with cli.websocket_connect('/') as ws:
    ws.send_text('{"msg":"Hi!"}')
    data = ws.receive_text()
    assert data == 'Message text was: Hi!'
```

## Routing and application

* * *

source

### WS_RouteX

>
```
>      WS_RouteX (path:str, recv, conn:<built-infunctioncallable>=None,
>                 disconn:<built-infunctioncallable>=None, name=None,
>                 middleware=None, hdrs=None, before=None)
```

_Initialize self. See help(type(self)) for accurate signature._

* * *

source

### RouteX

>
```
>      RouteX (path:str, endpoint, methods=None, name=None,
>              include_in_schema=True, middleware=None, hdrs=None, ftrs=None,
>              before=None, after=None, htmlkw=None, **bodykw)
```

_Initialize self. See help(type(self)) for accurate signature._

* * *

source

### RouterX

>
```
>      RouterX (routes=None, redirect_slashes=True, default=None,
>               on_startup=None, on_shutdown=None, lifespan=None,
>               middleware=None, hdrs=None, ftrs=None, before=None, after=None,
>               htmlkw=None, **bodykw)
```

_Initialize self. See help(type(self)) for accurate signature._

* * *

source

### get_key

>
```
>      get_key (key=None, fname='.sesskey')
```

```
get_key()
```

```
'08b63b51-be3a-4f54-8d26-4cd27eb17c0d'
```

* * *

source

### FastHTML

>
```
>      FastHTML (debug=False, routes=None, middleware=None,
>                exception_handlers=None, on_startup=None, on_shutdown=None,
>                lifespan=None, hdrs=None, ftrs=None, before=None, after=None,
>                default_hdrs=True, secret_key=None, session_cookie='session_',
>                max_age=31536000, ws_hdr=False, sess_path='/', same_site='lax',
>                sess_https_only=False, sess_domain=None, key_fname='.sesskey',
>                htmlkw=None, **bodykw)
```

*Creates an application instance.

**Parameters:**

  * **debug** \- Boolean indicating if debug tracebacks should be returned on errors.
  * **routes** \- A list of routes to serve incoming HTTP and WebSocket requests.
  * **middleware** \- A list of middleware to run for every request. A starlette application will always automatically include two middleware classes. `ServerErrorMiddleware` is added as the very outermost middleware, to handle any uncaught errors occurring anywhere in the entire stack. `ExceptionMiddleware` is added as the very innermost middleware, to deal with handled exception cases occurring in the routing or endpoints.
  * **exception_handlers** \- A mapping of either integer status codes, or exception class types onto callables which handle the exceptions. Exception handler callables should be of the form `handler(request, exc) -> response` and may be either standard functions, or async functions.
  * **on_startup** \- A list of callables to run on application startup. Startup handler callables do not take any arguments, and may be either standard functions, or async functions.
  * **on_shutdown** \- A list of callables to run on application shutdown. Shutdown handler callables do not take any arguments, and may be either standard functions, or async functions.
  * **lifespan** \- A lifespan context function, which can be used to perform startup and shutdown tasks. This is a newer style that replaces the `on_startup` and `on_shutdown` handlers. Use one or the other, not both.*

## Extras

* * *

source

### cookie

>
```
>      cookie (key:str, value='', max_age=None, expires=None, path='/',
>              domain=None, secure=False, httponly=False, samesite='lax')
```

_Create a ‘set-cookie’`HttpHeader`_

* * *

source

### reg_re_param

>
```
>      reg_re_param (m, s)
```

* * *

source

### MiddlewareBase

>
```
>      MiddlewareBase ()
```

_Initialize self. See help(type(self)) for accurate signature._

## Tests

```
def get_cli(app): return app,TestClient(app),app.route
```

```
app,cli,rt = get_cli(FastHTML(secret_key='soopersecret'))
```

```
@rt("/hi")
def get(): return 'Hi there'

r = cli.get('/hi')
r.text
```

```
'Hi there'
```

```
@rt("/hi")
def post(): return 'Postal'

cli.post('/hi').text
```

```
'Postal'
```

```
@app.get("/")
def show_host(req): return req.headers['host']

cli.get('/').text
```

```
'testserver'
```

```
@rt('/user/{nm}', name='gday')
def get(nm:str=''): return f"Good day to you, {nm}!"

cli.get('/user/Alexis').text
```

```
'Good day to you, Alexis!'
```

```
test_eq(app.router.url_path_for('gday', nm='Jeremy'), '/user/Jeremy')
```

```
hxhdr = {'headers':{'hx-request':"1"}}

@rt('/ft')
def get(): return Title('Foo'),H1('bar')

txt = cli.get('/ft').text
assert '<title>Foo</title>' in txt and '<h1>bar</h1>' in txt and '<html>' in txt

@rt('/xt2')
def get(): return H1('bar')

txt = cli.get('/xt2').text
assert '<title>FastHTML page</title>' in txt and '<h1>bar</h1>' in txt and '<html>' in txt

assert cli.get('/xt2', **hxhdr).text.strip() == '<h1>bar</h1>'

@rt('/xt3')
def get(): return Html(Head(Title('hi')), Body(P('there')))

txt = cli.get('/xt3').text
assert '<title>FastHTML page</title>' not in txt and '<title>hi</title>' in txt and '<p>there</p>' in txt
```

```
def test_r(cli, path, exp, meth='get', hx=False, **kwargs):
    if hx: kwargs['headers'] = {'hx-request':"1"}
    test_eq(getattr(cli, meth)(path, **kwargs).text, exp)

app.chk = 'foo'
ModelName = str_enum('ModelName', "alexnet", "resnet", "lenet")
fake_db = [{"name": "Foo"}, {"name": "Bar"}]
```

```
@rt('/html/{idx}')
async def get(idx:int): return Body(H4(f'Next is {idx+1}.'))

reg_re_param("imgext", "ico|gif|jpg|jpeg|webm")

@rt(r'/static/{path:path}{fn}.{ext:imgext}')
def get(fn:str, path:str, ext:str): return f"Getting {fn}.{ext} from /{path}"

@rt("/models/{nm}")
def get(nm:ModelName): return nm

@rt("/files/{path}")
async def get(path: Path): return path.with_suffix('.txt')

@rt("/items/")
def get(idx:int|None = 0): return fake_db[idx]
```

```
test_r(cli, '/html/1', '<body>\n  <h4>Next is 2.</h4>\n</body>\n', hx=True)
test_r(cli, '/static/foo/jph.ico', 'Getting jph.ico from /foo/')
test_r(cli, '/models/alexnet', 'alexnet')
test_r(cli, '/files/foo', 'foo.txt')
test_r(cli, '/items/?idx=1', '{"name":"Bar"}')
test_r(cli, '/items/', '{"name":"Foo"}')
assert cli.get('/items/?idx=g').status_code==404
```

```
@app.get("/booly/")
def _(coming:bool=True): return 'Coming' if coming else 'Not coming'

@app.get("/datie/")
def _(d:date): return d

@app.get("/ua")
async def _(user_agent:str): return user_agent

@app.get("/hxtest")
def _(htmx): return htmx.request

@app.get("/hxtest2")
def _(foo:HtmxHeaders, req): return foo.request

@app.get("/app")
def _(app): return app.chk

@app.get("/app2")
def _(foo:FastHTML): return foo.chk,HttpHeader("mykey", "myval")
```

```
test_r(cli, '/booly/?coming=true', 'Coming')
test_r(cli, '/booly/?coming=no', 'Not coming')
date_str = "17th of May, 2024, 2p"
test_r(cli, f'/datie/?d={date_str}', '2024-05-17 14:00:00')
test_r(cli, '/ua', 'FastHTML', headers={'User-Agent':'FastHTML'})
test_r(cli, '/hxtest' , '1', headers={'HX-Request':'1'})
test_r(cli, '/hxtest2', '1', headers={'HX-Request':'1'})
test_r(cli, '/app' , 'foo')
```

```
r = cli.get('/app2', **hxhdr)
test_eq(r.text, 'foo\n')
test_eq(r.headers['mykey'], 'myval')
```

```
@app.post('/profile/me')
def profile_update(username: str): return username

test_r(cli, '/profile/me', 'Alexis', 'post', data={'username' : 'Alexis'})
test_r(cli, '/profile/me', 'Missing required field: username', 'post', data={})
```

```
# Example post request with parameter that has a default value
@app.post('/pet/dog')
def pet_dog(dogname: str = None): return dogname

# Working post request with optional parameter
test_r(cli, '/pet/dog', '', 'post', data={})
```

```
@dataclass
class Bodie: a:int;b:str

@rt("/bodie/{nm}")
def post(nm:str, data:Bodie):
    res = asdict(data)
    res['nm'] = nm
    return res

@app.post("/bodied/")
def bodied(data:dict): return data

nt = namedtuple('Bodient', ['a','b'])

@app.post("/bodient/")
def bodient(data:nt): return data._asdict()

class BodieTD(TypedDict): a:int;b:str='foo'

@app.post("/bodietd/")
def bodient(data:BodieTD): return data

class Bodie2:
    a:int|None; b:str
    def __init__(self, a, b='foo'): store_attr()

@app.post("/bodie2/")
def bodie(d:Bodie2): return f"a: {d.a}; b: {d.b}"
```

```
d = dict(a=1, b='foo')

test_r(cli, '/bodie/me', '{"a":1,"b":"foo","nm":"me"}', 'post', data=dict(a=1, b='foo', nm='me'))
test_r(cli, '/bodied/', '{"a":"1","b":"foo"}', 'post', data=d)
test_r(cli, '/bodie2/', 'a: 1; b: foo', 'post', data={'a':1})
test_r(cli, '/bodient/', '{"a":"1","b":"foo"}', 'post', data=d)
test_r(cli, '/bodietd/', '{"a":1,"b":"foo"}', 'post', data=d)
```

```
@rt("/setcookie")
def get(req): return cookie('now', datetime.now())

@rt("/getcookie")
def get(now:date): return f'Cookie was set at time {now.time()}'
```

```
print(cli.get('/setcookie').text)
time.sleep(0.01)
cli.get('/getcookie').text
```

[/code]

```
'Cookie was set at time 18:20:22.628240'
```

```
@rt("/setsess")
def get(sess):
    now = datetime.now()
    sess['noo'] = str(now)
    return f'Set to {now}'

@rt("/getsess")
def get(noo:date): return f'Session time: {noo.time()}'
```

```
print(cli.get('/setsess').text)
time.sleep(0.01)
cli.get('/getsess').text
```

```
Set to 2024-07-27 18:20:22.674757
```

```
'Session time: 18:20:22.674757'
```

```
@rt("/upload")
async def post(uploadfile:str): return (await uploadfile.read()).decode()

fn = '../CHANGELOG.md'
data = {'message': 'Hello, world!'}
with open(fn, 'rb') as f:
    print(cli.post('/upload', files={'uploadfile': f}, data=data).text[:80])
```

```
# Release notes

<!-- do not remove -->

## 0.1.8

### New Features

- Remove co
```

```
from fasthtml.authmw import user_pwd_auth
```

```
auth = user_pwd_auth(testuser='spycraft')
app,cli,rt = get_cli(FastHTML(middleware=[auth]))

@rt("/locked")
def get(auth): return 'Hello, ' + auth

test_eq(cli.get('/locked').text, 'not authenticated')
test_eq(cli.get('/locked', auth=("testuser","spycraft")).text, 'Hello, testuser')
```

```
hdrs, routes = app.router.hdrs, app.routes
```

```
from fasthtml.live_reload import FastHTMLWithLiveReload
```

```
app,cli,rt = get_cli(FastHTMLWithLiveReload())

@rt("/hi")
def get(): return 'Hi there'

test_eq(cli.get('/hi').text, "Hi there")

lr_hdrs, lr_routes = app.router.hdrs, app.routes
test_eq(len(lr_hdrs), len(hdrs)+1)
assert app.LIVE_RELOAD_HEADER in lr_hdrs
test_eq(len(lr_routes), len(routes)+1)
assert app.LIVE_RELOAD_ROUTE in lr_routes
```

  * __Report an issue

  1. Source
  2. Components

# Components

```
from lxml import html as lx
from pprint import pprint
```

* * *

source

### show

>
```
>      show (ft, *rest)
```

* * *

source

### ft_html

>
```
>      ft_html (tag:str, *c, id=None, cls=None, title=None, style=None,
>               **kwargs)
```

* * *

source

### ft_hx

>
```
>      ft_hx (tag:str, *c, target_id=None, id=None, cls=None, title=None,
>             style=None, accesskey=None, contenteditable=None, dir=None,
>             draggable=None, enterkeyhint=None, hidden=None, inert=None,
>             inputmode=None, lang=None, popover=None, spellcheck=None,
>             tabindex=None, translate=None, hx_get=None, hx_post=None,
>             hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None,
>             hx_target=None, hx_swap=None, hx_include=None, hx_select=None,
>             hx_indicator=None, hx_push_url=None, hx_confirm=None,
>             hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs)
```

* * *

source

### File

>
```
>      File (fname)
```

_Use the unescaped text in file`fname` directly_

For tags that have a `name` attribute, it will be set to the value of `id` if not provided explicitly:

```
Form(Button(target_id='foo', id='btn'),
     hx_post='/', target_id='tgt', id='frm')
```

```
<form hx-post="/" hx-target="#tgt" id="frm" name="frm">
  <button hx-target="#foo" id="btn" name="btn"></button>
</form>
```

* * *

source

### fill_form

>
```
>      fill_form (form:fastcore.xml.FT, obj)
```

_Fills named items in`form` using attributes in `obj`_

```
@dataclass
class TodoItem:
    title:str; id:int; done:bool; details:str

todo = TodoItem(id=2, title="Profit", done=True, details="Details")
check = Label(Input(type="checkbox", cls="checkboxer", id="done", data_foo="bar"), "Done")
form = Form(Fieldset(Input(cls="char", id="title"), check, Input(type="hidden", id="id"), Textarea(id='details'), Button("Save")))
form = fill_form(form, todo)
form
```

```
<form>
  <fieldset>
    <input id="title" class="char" name="title" value="Profit"></input>
    <label>
      <input type="checkbox" data-foo="bar" id="done" class="checkboxer" name="done" checked="1"></input>
Done
    </label>
    <input type="hidden" id="id" name="id" value="2"></input>
    <textarea id="details" name="details">Details</textarea>
    <button>Save</button>
  </fieldset>
</form>
```

* * *

source

### fill_dataclass

>
```
>      fill_dataclass (src, dest)
```

_Modifies dataclass in-place and returns it_

```
nt = TodoItem('', 0, False, '')
fill_dataclass(todo, nt)
nt
```

```
TodoItem(title='Profit', id=2, done=True, details='Details')
```

* * *

source

### find_inputs

>
```
>      find_inputs (e, tags='input', **kw)
```

Exported source

```
def find_inputs(e, tags='input', **kw):
    # Recursively find all elements in `e` with `tags` and attrs matching `kw`
    if not isinstance(e, (list,tuple)): return []
    inputs = []
    if isinstance(tags,str): tags = [tags]
    elif tags is None: tags = []
    cs = e
    if isinstance(e, list):
        tag,cs,attr = e
        if e[0] in tags and kw.items()<=e[2].items(): inputs.append(e)
    for o in cs: inputs += find_inputs(o, tags, **kw)
    return inputs
```

```
find_inputs(form, id='title')
```

```
[['input',
  (),
  {'id': 'title', 'class': 'char', 'name': 'title', 'value': 'Profit'}]]
```

You can also use lxml for more sophisticated searching:

```
elem = lx.fromstring(to_xml(form))
elem.xpath("//input[@id='title']/@value")
```

```
['Profit']
```

* * *

source

### **getattr**

>
```
>      __getattr__ (tag)
```

* * *

source

### html2ft

>
```
>      html2ft (html)
```

_Convert HTML to an`ft` expression_

```
h = to_xml(form)
hl_md(html2ft(h), 'python')
```

```
Form(
    Fieldset(
        Input(id='title', name='title', value='Profit', cls='char'),
        Label(
            Input(type='checkbox', data_foo='bar', id='done', name='done', checked='1', cls='checkboxer'),
            'Done'
        ),
        Input(type='hidden', id='id', name='id', value='2'),
        Textarea('Details', id='details', name='details'),
        Button('Save')
    )
)
```

  * __Report an issue

  1. Source
  2. Component extensions

# Component extensions

```
from pprint import pprint
```

`picocondlink` is the class-conditional css `link` tag, and `picolink` is the regular tag.

```
show(picocondlink)
```

* * *

source

### set_pico_cls

>
```
>      set_pico_cls ()
```

Run this to make jupyter outputs styled with pico:

```
set_pico_cls()
```

* * *

source

### Html

>
```
>      Html (*c, doctype=True, **kwargs)
```

_An HTML tag, optionally preceeded by`!DOCTYPE HTML`_

* * *

source

### A

>
```
>      A (*c, hx_get=None, target_id=None, hx_swap=None, href='#', id=None,
>         cls=None, title=None, style=None, accesskey=None,
>         contenteditable=None, dir=None, draggable=None, enterkeyhint=None,
>         hidden=None, inert=None, inputmode=None, lang=None, popover=None,
>         spellcheck=None, tabindex=None, translate=None, hx_post=None,
>         hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None,
>         hx_target=None, hx_include=None, hx_select=None, hx_indicator=None,
>         hx_push_url=None, hx_confirm=None, hx_disable=None,
>         hx_replace_url=None, hx_on=None, **kwargs)
```

_An A tag;`href` defaults to ‘#’ for more concise use with HTMX_

```
A('text', ht_get='/get', target_id='id')
```

```
<a href="#" ht-get="/get" hx-target="#id">text</a>
```

* * *

source

### AX

>
```
>      AX (txt, hx_get=None, target_id=None, hx_swap=None, href='#', id=None,
>          cls=None, title=None, style=None, accesskey=None,
>          contenteditable=None, dir=None, draggable=None, enterkeyhint=None,
>          hidden=None, inert=None, inputmode=None, lang=None, popover=None,
>          spellcheck=None, tabindex=None, translate=None, hx_post=None,
>          hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None,
>          hx_target=None, hx_include=None, hx_select=None, hx_indicator=None,
>          hx_push_url=None, hx_confirm=None, hx_disable=None,
>          hx_replace_url=None, hx_on=None, **kwargs)
```

_An A tag with just one text child, allowing hx_get, target_id, and hx_swap to be positional params_

```
AX('text', '/get', 'id')
```

```
<a href="#" hx-get="/get" hx-target="#id">text</a>
```

* * *

source

### Checkbox

>
```
>      Checkbox (checked:bool=False, label=None, value='1', target_id=None,
>                id=None, cls=None, title=None, style=None, accesskey=None,
>                contenteditable=None, dir=None, draggable=None,
>                enterkeyhint=None, hidden=None, inert=None, inputmode=None,
>                lang=None, popover=None, spellcheck=None, tabindex=None,
>                translate=None, hx_get=None, hx_post=None, hx_put=None,
>                hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None,
>                hx_swap=None, hx_include=None, hx_select=None,
>                hx_indicator=None, hx_push_url=None, hx_confirm=None,
>                hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs)
```

_A Checkbox optionally inside a Label_

```
show(Checkbox(True, 'Check me out!'))
```

Check me out!

* * *

source

### Card

>
```
>      Card (*c, header=None, footer=None, target_id=None, id=None, cls=None,
>            title=None, style=None, accesskey=None, contenteditable=None,
>            dir=None, draggable=None, enterkeyhint=None, hidden=None,
>            inert=None, inputmode=None, lang=None, popover=None,
>            spellcheck=None, tabindex=None, translate=None, hx_get=None,
>            hx_post=None, hx_put=None, hx_delete=None, hx_patch=None,
>            hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None,
>            hx_select=None, hx_indicator=None, hx_push_url=None,
>            hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None,
>            **kwargs)
```

_A PicoCSS Card, implemented as an Article with optional Header and Footer_

```
show(Card('body', header=P('head'), footer=P('foot')))
```

head

body

foot

* * *

source

### Group

>
```
>      Group (*c, target_id=None, id=None, cls=None, title=None, style=None,
>             accesskey=None, contenteditable=None, dir=None, draggable=None,
>             enterkeyhint=None, hidden=None, inert=None, inputmode=None,
>             lang=None, popover=None, spellcheck=None, tabindex=None,
>             translate=None, hx_get=None, hx_post=None, hx_put=None,
>             hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None,
>             hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None,
>             hx_push_url=None, hx_confirm=None, hx_disable=None,
>             hx_replace_url=None, hx_on=None, **kwargs)
```

_A PicoCSS Group, implemented as a Fieldset with role ‘group’_

```
show(Group(Input(), Button("Save")))
```

* * *

source

### Search

>
```
>      Search (*c, target_id=None, id=None, cls=None, title=None, style=None,
>              accesskey=None, contenteditable=None, dir=None, draggable=None,
>              enterkeyhint=None, hidden=None, inert=None, inputmode=None,
>              lang=None, popover=None, spellcheck=None, tabindex=None,
>              translate=None, hx_get=None, hx_post=None, hx_put=None,
>              hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None,
>              hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None,
>              hx_push_url=None, hx_confirm=None, hx_disable=None,
>              hx_replace_url=None, hx_on=None, **kwargs)
```

_A PicoCSS Search, implemented as a Form with role ‘search’_

```
show(Search(Input(type="search"), Button("Search")))
```

* * *

source

### Grid

>
```
>      Grid (*c, cls='grid', target_id=None, id=None, title=None, style=None,
>            accesskey=None, contenteditable=None, dir=None, draggable=None,
>            enterkeyhint=None, hidden=None, inert=None, inputmode=None,
>            lang=None, popover=None, spellcheck=None, tabindex=None,
>            translate=None, hx_get=None, hx_post=None, hx_put=None,
>            hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None,
>            hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None,
>            hx_push_url=None, hx_confirm=None, hx_disable=None,
>            hx_replace_url=None, hx_on=None, **kwargs)
```

_A PicoCSS Grid, implemented as child Divs in a Div with class ‘grid’_

```
colors = [Input(type="color", value=o) for o in ('#e66465', '#53d2c5', '#f6b73c')]
show(Grid(*colors))
```

* * *

source

### DialogX

>
```
>      DialogX (*c, open=None, header=None, footer=None, id=None,
>               target_id=None, cls=None, title=None, style=None,
>               accesskey=None, contenteditable=None, dir=None, draggable=None,
>               enterkeyhint=None, hidden=None, inert=None, inputmode=None,
>               lang=None, popover=None, spellcheck=None, tabindex=None,
>               translate=None, hx_get=None, hx_post=None, hx_put=None,
>               hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None,
>               hx_swap=None, hx_include=None, hx_select=None,
>               hx_indicator=None, hx_push_url=None, hx_confirm=None,
>               hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs)
```

_A PicoCSS Dialog, with children inside a Card_

```
hdr = Div(Button(aria_label="Close", rel="prev"), P('confirm'))
ftr = Div(Button('Cancel', cls="secondary"), Button('Confirm'))
d = DialogX('thank you!', header=hdr, footer=ftr, open=None, id='dlgtest')
# use js or htmx to display modal
```

* * *

source

### Hidden

>
```
>      Hidden (value:str='', target_id=None, id=None, cls=None, title=None,
>              style=None, accesskey=None, contenteditable=None, dir=None,
>              draggable=None, enterkeyhint=None, hidden=None, inert=None,
>              inputmode=None, lang=None, popover=None, spellcheck=None,
>              tabindex=None, translate=None, hx_get=None, hx_post=None,
>              hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None,
>              hx_target=None, hx_swap=None, hx_include=None, hx_select=None,
>              hx_indicator=None, hx_push_url=None, hx_confirm=None,
>              hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs)
```

_An Input of type ‘hidden’_

* * *

source

### Container

>
```
>      Container (*args, target_id=None, id=None, cls=None, title=None,
>                 style=None, accesskey=None, contenteditable=None, dir=None,
>                 draggable=None, enterkeyhint=None, hidden=None, inert=None,
>                 inputmode=None, lang=None, popover=None, spellcheck=None,
>                 tabindex=None, translate=None, hx_get=None, hx_post=None,
>                 hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None,
>                 hx_target=None, hx_swap=None, hx_include=None, hx_select=None,
>                 hx_indicator=None, hx_push_url=None, hx_confirm=None,
>                 hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs)
```

_A PicoCSS Container, implemented as a Main with class ‘container’_

* * *

source

### Script

>
```
>      Script (code:str='', id=None, cls=None, title=None, style=None, **kwargs)
```

_A Script tag that doesn’t escape its code_

* * *

source

### Style

>
```
>      Style (*c, id=None, cls=None, title=None, style=None, **kwargs)
```

_A Style tag that doesn’t escape its code_

* * *

source

### double_braces

>
```
>      double_braces (s)
```

_Convert single braces to double braces if next to special chars or newline_

* * *

source

### undouble_braces

>
```
>      undouble_braces (s)
```

_Convert double braces to single braces if next to special chars or newline_

* * *

source

### loose_format

>
```
>      loose_format (s, **kw)
```

_String format`s` using `kw`, without being strict about braces outside of template params_

* * *

source

### ScriptX

>
```
>      ScriptX (fname, type=None, _async=None, defer=None, charset=None,
>               crossorigin=None, integrity=None, **kw)
```

_A`script` element with contents read from `fname`_

* * *

source

### replace_css_vars

>
```
>      replace_css_vars (css, pre='tpl', **kwargs)
```

_Replace`var(--)` CSS variables with `kwargs` if name prefix matches `pre`_

* * *

source

### StyleX

>
```
>      StyleX (fname, **kw)
```

_A`style` element with contents read from `fname` and variables replaced from `kw`_

* * *

source

### run_js

>
```
>      run_js (js, id=None, **kw)
```

_Run`js` script, auto-generating `id` based on name of caller if needed, and js-escaping any `kw` params_

* * *

source

### Titled

>
```
>      Titled (title:str='FastHTML app', *args, target_id=None, id=None,
>              cls=None, style=None, accesskey=None, contenteditable=None,
>              dir=None, draggable=None, enterkeyhint=None, hidden=None,
>              inert=None, inputmode=None, lang=None, popover=None,
>              spellcheck=None, tabindex=None, translate=None, hx_get=None,
>              hx_post=None, hx_put=None, hx_delete=None, hx_patch=None,
>              hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None,
>              hx_select=None, hx_indicator=None, hx_push_url=None,
>              hx_confirm=None, hx_disable=None, hx_replace_url=None,
>              hx_on=None, **kwargs)
```

_An HTML partial containing a`Title`, and `H1`, and any provided children_

* * *

source

### Socials

>
```
>      Socials (title, site_name, description, image, url=None, w=1200, h=630,
>               twitter_site=None, creator=None, card='summary')
```

_OG and Twitter social card headers_

* * *

source

### Favicon

>
```
>      Favicon (light_icon, dark_icon)
```

_Light and dark favicon headers_

* * *

source

### jsd

>
```
>      jsd (org, repo, root, path, prov='gh', typ='script', ver=None, esm=False,
>           **kwargs)
```

# Command Line Tools

* * *

source

### railway_link

>
```
>      railway_link ()
```

_Link the current directory to the current project’s Railway service_

* * *

source

### railway_deploy

>
```
>      railway_deploy (name:str, mount:<function bool_arg>=True)
```

_Deploy a FastHTML app to Railway_

| **Type** | **Default** | **Details**  
---|---|---|---  
name | str |  | The project name to deploy  
mount | bool_arg | True | Create a mounted volume at /app/data?  
We’re going to be adding more to this document, so check back frequently for updates.

## Installation

```
pip install python-fasthtml
```

## A Minimal Application

A minimal FastHTML application looks something like this:

```
**main.py**
```

```
1from fasthtml.fastapp import *

2app, rt = fast_app()

3@rt("/")
4def get():
5    return Titled("FastHTML", P("Let's do this!"))

6serve()
```

1

     We import what we need for rapid development! A carefully-curated set of FastHTML functions and other Python objects is brought into our global namespace for convenience.
2

     We instantiate a FastHTML app with the `fast_app()` utility function. This provides a number of really useful defaults that we’ll take advantage of later in the tutorial.
3

     We use the `rt()` decorator to tell FastHTML what to return when a user visits `/` in their browser.
4

     We connect this route to HTTP GET requests by defining a view function called `get()`.
5

     A tree of Python function calls that return all the HTML required to write a properly formed web page. You’ll soon see the power of this approach.
6

     The `serve()` utility configures and runs FastHTML using a library called `uvicorn`.

Run the code:

```
python main.py
```

The terminal will look like this:

```
INFO:     Uvicorn running on http://0.0.0.0:5001 (Press CTRL+C to quit)
INFO:     Started reloader process [58058] using WatchFiles
INFO:     Started server process [58060]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Confirm FastHTML is running by opening your web browser to 127.0.0.1:5001. You should see something like the image below:

__

Note

While some linters and developers will complain about the wildcard import, it is by design here and perfectly safe. FastHTML is very deliberate about the objects it exports in `fasthtml.common`. If it bothers you, you can import the objects you need individually, though it will make the code more verbose and less readable.

## A Minimal Charting Application

The `Script` function allows you to include JavaScript. You can use Python to generate parts of your JS or JSON like this:

```
import json
from fasthtml.common import * 

app, rt = fast_app(hdrs=(Script(src="https://cdn.plot.ly/plotly-2.32.0.min.js"),))

data = json.dumps({
    "data": [{"x": [1, 2, 3, 4],"type": "scatter"},
            {"x": [1, 2, 3, 4],"y": [16, 5, 11, 9],"type": "scatter"}],
    "title": "Plotly chart in FastHTML ",
    "description": "This is a demo dashboard",
    "type": "scatter"
})


@rt("/")
def get():
  return Titled("Chart Demo", Div(id="myDiv"),
    Script(f"var data = {data}; Plotly.newPlot('myDiv', data);"))

serve()
```

## Debug Mode

When we can’t figure out a bug in FastHTML, we can run it in `DEBUG` mode. When an error is thrown, the error screen is displayed in the browser. This error setting should never be used in a deployed app.

```
from fasthtml.fastapp import *

1app, rt = fast_app(debug=True)

@rt("/")
def get():
2    1/0
    return Titled("FastHTML Error!", P("Let's error!"))

serve()
```

1

     `debug=True` sets debug mode on.
2

     Python throws an error when it tries to divide an integer by zero.

## Routing

FastHTML builds upon FastAPI’s friendly decorator pattern for specifying URLs, with extra features:

```
**main.py**
```

```
from fasthtml.fastapp import * 

app, rt = fast_app()

1@rt("/")
def get():
  return Titled("FastHTML", P("Let's do this!"))

2@rt("/hello")
def get():
  return Titled("Hello, world!")

serve()
```

1

     The “/” URL on line 5 is the home of a project. This would be accessed at 127.0.0.1:5001.
2

     “/hello” URL on line 9 will be found by the project if the user visits 127.0.0.1:5001/hello.

__

Tip

It looks like `get()` is being defined twice, but that’s not the case. Each function decorated with `rt` is totally separate, and is injected into the router. We’re not calling them in the module’s namespace (`locals()`). Rather, we’re loading them into the routing mechanism using the `rt` decorator.

You can do more! Read on to learn what we can do to make parts of the URL dynamic.

## Variables in URLs

You can add variable sections to a URL by marking them with `{variable_name}`. Your function then receives the `{variable_name}` as a keyword argument, but only if it is the correct type. Here’s an example:

```
**main.py**
```

```
from fasthtml.fastapp import * 

app, rt = fast_app()

1@rt("/{name}/{age}")
2def get(name: str, age: int):
3  return Titled(f"Hello {name.title()}, age {age}")

serve()
```

1

     We specify two variable names, `name` and `age`.
2

     We define two function arguments named identically to the variables. You will note that we specify the Python types to be passed.
3

     We use these functions in our project.

Try it out by going to this address: 127.0.0.1:5001/uma/5. You should get a page that says,

> “Hello Uma, age 5”.

### What happens if we enter incorrect data?

The 127.0.0.1:5001/uma/5 URL works because `5` is an integer. If we enter something that is not, such as 127.0.0.1:5001/uma/five, then FastHTML will return an error instead of a web page.

__

FastHTML URL routing supports more complex types

The two examples we provide here use Python’s built-in `str` and `int` types, but you can use your own types, including more complex ones such as those defined by libraries like attrs, pydantic, and even sqlmodel.

## HTTP Methods

FastHTML matches function names to HTTP methods. So far the URL routes we’ve defined have been for HTTP GET methods, the most common method for web pages.

Form submissions often are sent as HTTP POST. When dealing with more dynamic web page designs, also known as Single Page Apps (SPA for short), the need can arise for other methods such as HTTP PUT and HTTP DELETE. The way FastHTML handles this is by changing the function name.

```
**main.py**
```

```
from fasthtml.fastapp import * 

app, rt = fast_app()

@rt("/")  
1def get():
  return Titled("HTTP GET", P("Handle GET"))

@rt("/")  
2def post():
  return Titled("HTTP POST", P("Handle POST"))

serve()
```

1

     On line 6 because the `get()` function name is used, this will handle HTTP GETs going to the `/` URI.
2

     On line 10 because the `post()` function name is used, this will handle HTTP POSTs going to the `/` URI.

## CSS Files and Inline Styles

Here we modify default headers to demonstrate how to use the Sakura CSS microframework instead of FastHTML’s default of Pico CSS.

```
**main.py**
```

```
from fasthtml.fastapp import * 

app, rt = fast_app(
1    default_hdrs=False,
    hdrs=(
        Link(rel='stylesheet', href='assets/normalize.min.css', type='text/css'),
2        Link(rel='stylesheet', href='assets/sakura.css', type='text/css'),
3        Style("p {color: red;}")
))

@app.get("/")
def home():
    return Titled("FastHTML",
        P("Let's do this!"),
    )

serve()
```

1

     By setting `default_hdrs` to `False`, FastHTML will not include `pico.min.css`.
2

     This will generate an HTML `<link>` tag for sourcing the css for Sakura.
3

     If you want an inline styles, the `Style()` function will put the result into the HTML.

Check it out!

## Other Static Media File Locations

As you saw, `Script` and `Link` are specific to the most common static media use cases in web apps: including JavaScript, CSS, and images. But it also works with videos and other static media files. The default behavior is to look for these files in the root directory - typically we don’t do anything special to include them.

FastHTML also allows us to define a route that uses `FileResponse` to serve the file at a specified path. This is useful for serving images, videos, and other media files from a different directory without having to change the paths of many files. So if we move the directory containing the media files, we only need to change the path in one place. In the example below, we call images from a directory called `public`.

```
@rt("/{fname:path}.{ext:static}")
async def get(fname:str, ext:str): 
    return FileResponse(f'public/{fname}.{ext}')
```

## Rendering Markdown

```
from fasthtml.common import *

hdrs = (MarkdownJS(), HighlightJS(langs=['python', 'javascript', 'html', 'css']), )

app, rt = fast_app(hdrs=hdrs)

content = """
Here are some _markdown_ elements.

- This is a list item
- This is another list item
- And this is a third list item

**Fenced code blocks work here.**
"""

@rt('/')
def get(req):
    return Titled("Markdown rendering example", Div(content,cls="marked"))

serve()
```

## Defining new `ft` components

We can build our own `ft` components and combine them with other components. The simplest method is defining them as a function.

```
def hero(title, statement):
    return Div(H1(title),P(statement), cls="hero")

# usage example
Main(
    hero("Hello World", "This is a hero statement")
)
```

```
<main>
  <div class="hero">
    <h1>Hello World</h1>
    <p>This is a hero statement</p>
  </div>
</main>
```

### Pass through components

For when we need to define a new component that allows zero-to-many components to be nested within them, we lean on Python’s `*args` and `**kwargs` mechanism. Useful for creating page layout controls.

```
def layout(*args, **kwargs):
    """Dashboard layout for all our dashboard views"""
    return Main(
        H1("Dashboard"),
        Div(*args, **kwargs),
        cls="dashboard",
    )

# usage example
layout(
    Ul(*[Li(o) for o in range(3)]),
    P("Some content", cls="description"),
)
```

```
<main class="dashboard">
  <h1>Dashboard</h1>
  <div>
    <ul>
      <li>0</li>
      <li>1</li>
      <li>2</li>
    </ul>
    <p class="description">Some content</p>
  </div>
</main>
```

### Dataclasses as ft components

While functions are easy to read, for more complex components some might find it easier to use a dataclass.

```
from dataclasses import dataclass

@dataclass
class Hero:
    title: str
    statement: str

    def __ft__(self):
        """ The __ft__ method renders the dataclass at runtime."""
        return Div(H1(self.title),P(self.statement), cls="hero")

# usage example
Main(
    Hero("Hello World", "This is a hero statement")
)
```

```
<main>
  <div class="hero">
    <h1>Hello World</h1>
    <p>This is a hero statement</p>
  </div>
</main>
```

## Testing views in notebooks

Because of the ASGI event loop it is currently impossible to run FastHTML inside a notebook. However, we can still test the output of our views. To do this, we leverage Starlette, an ASGI toolkit that FastHTML uses.

```
# First we instantiate our app, in this case we remove the
# default headers to reduce the size of the output.
app, rt = fast_app(default_hdrs=False)

# Setting up the Starlette test client
from starlette.testclient import TestClient
client = TestClient(app)

# Usage example
@rt("/")
def get():
    return Titled("FastHTML is awesome", 
        P("The fastest way to create web apps in Python"))

print(client.get("/").text)
```

```
<!doctype html></!doctype>

<html>
  <head>
    <title>FastHTML is awesome</title>
  </head>
  <body>
<main class="container">
  <h1>FastHTML is awesome</h1>
  <p>The fastest way to create web apps in Python</p>
</main>
  </body>
</html>


```

## Cookies

Using Starlette’s Response object, we can set cookies. In our example, we’ll create a `timestamp` cookie.

```
from starlette.responses import Response
from datetime import datetime

@rt('/settimestamp')
def get(request):
    now = datetime.now()
    res = Response(f'Set to {now}')
    res.set_cookie('timestamp', str(now))
    return res

client.get('/settime').text
```

```
'Set to 2024-07-27 08:46:31.732189'
```

Now let’s get it back using the Starlette’s `Request` object, passed as an argument into our view.

```
@rt('/gettimestamp')
def get(request):
    res = Response(f'Get timestamp: {request.cookies.get("now")}')
    return res

client.get('/gettimestamp').text
```

```
'Getting our timestamp: 2024-07-27 08:46:31.732189'
```

## Sessions

For convenience and security, FastHTML has a mechanism for storing small amounts of data in the user’s browser. We can do this by adding a `session` argument to routes. FastHTML sessions are Python dictonaries, and we can leverage to our benefit. The example below shows how to concisely set and get sessions.

```
@rt('/adder/{num}')
def get(session, num: int):
    session.setdefault('sum', 0)
    session['sum'] = session.get('sum') + num
    return Response(f'The sum is {session["sum"]}.')
```

## Toasts (also known as Messages)

Toasts, sometimes called “Messages” are small notifications usually in colored boxes used to notify users that something has happened. Toasts can be of four types:

  * info
  * success
  * warning
  * error

Examples toasts might include:

  * “Payment accepted”
  * “Data submitted”
  * “Request approved”

Toasts take a little configuration plus views that use them require the `session` argument.

```
1setup_toasts(app)

@rt('/toasting')
2def get(session):
    # Normally one toast is enough, this allows us to see
    # different toast types in action.
    add_toast(session, f"Toast is being cooked", "info")
    add_toast(session, f"Toast is ready", "success")
    add_toast(session, f"Toast is getting a bit crispy", "warning")
    add_toast(session, f"Toast is burning!", "error")
    return Titled("I like toast")
```

1

     `setup_toasts` is a helper function that adds toast dependencies. Usually this would be declared right after `fast_app()`.
2

     Toasts require sessions.

## Authentication and authorization

In FastHTML the tasks of authentication and authorization are handled with Beforeware. Beforeware are functions that run before the route handler is called. They are useful for global tasks like ensuring users are authenticated or have permissions to access a view.

First, we write a function that accepts a request and session arguments:

```
# Status code 303 is a redirect that can change POST to GET,
# so it's appropriate for a login page.
login_redir = RedirectResponse('/login', status_code=303)

def user_auth_before(req, sess):
    # The `auth` key in the request scope is automatically provided
    # to any handler which requests it, and can not be injected
    # by the user using query params, cookies, etc, so it should
    # be secure to use.    
    auth = req.scope['auth'] = sess.get('auth', None)
    # If the session key is not there, it redirects to the login page.
    if not auth: return login_redir
```

Now we pass our `user_auth_before` function as the first argument into a `Beforeware` class. We also pass a list of regular expressions to the `skip` argument, designed to allow users to still get to the home and login pages.

```
beforeware = Beforeware(
    user_auth_before,
    skip=[r'/favicon\.ico', r'/static/.*', r'.*\.css', r'.*\.js', '/login', '/']
)

app, rt = fast_app(before=beforeware)
```

## Unwritten quickstart sections

  * Websockets
  * Tables

  * __Report an issue