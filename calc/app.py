# Put your app in here.
from Flask import flask
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def do_add():
    """Add the two parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = add(a, b)

    return str(total)


@app.route('/sub')
def do_sub():
    """Subtract the two parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = sub(a, b)

    return str(total)


@app.route('/mult')
def do_mult():
    """Multiply the parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    product = mult(a, b)

    return str(product)


@app.route('/div')
def do_div():
    """Divide the parameters"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    quotient = div(a, b)

    return str(quotient)


# further study

ops = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<operation>")
def basic_math(operation):
    """basic math on two parameters a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = ops[operation](a, b)

    return str(result)
