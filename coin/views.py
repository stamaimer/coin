from coin import coin

@coin.route('/')
@coin.route("/index")
def index():

    return "Hello, World."
