from striver import app



@app.route('/')
def index():
    object = {"pet":"dog"}
    return object
@app.route('/like', methods = ["POST"])
def like():
    return

@app.route('/dislike', methods = ["POST"])
def dislike():
    return

@app.route('/quote', methods = ["GET"])
def quote():
    return
    
