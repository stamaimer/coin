
@coin.route('/')
@coin.route("/index")
def index():

    return "Hello, World."

@coin.route("signup", methods=["POST"])
def signup():

    pass
