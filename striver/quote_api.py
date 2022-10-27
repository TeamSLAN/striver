from . import app
import random
from flask import request

# define quote list
quoteslist = [
    "“Nature has given us all the pieces required to achieve exceptional wellness and health, but has left it to us to put these pieces together.”—Diane McLaren",
    "“It is only when we take chances, when our lives improve. The initial and the most difficult risk that we need to take is to become honest. —Walter Anderson",
    "“When you change your thoughts, remember to also change your world.”—Norman Vincent Peale",
    "“When you give joy to other people, you get more joy in return. You should give a good thought to happiness that you can give out.”— Eleanor Roosevelt",
    "“Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.” — Mark Twain",
    "“Learn as if you will live forever, live like you will die tomorrow.” — Mahatma Gandhi",
    "“We cannot solve problems with the kind of thinking we employed when we came up with them.” — Albert Einstein",
    "“Success usually comes to those who are too busy looking for it.” — Henry David Thoreau",
    "“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie",
    "“There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.” —Mister Rogers"
]

# quoteslist sets the list of quotes
quotedata = {}  # sets an empty dictionary that will get filled up
for i,item in enumerate(quoteslist):  # for loop that goes over every quote inside of quotes list
    # inside of the dictionary the key is the quote and this loop adds likes and dislikes as the key for every quote
    quotedata[i] = {"likes": 0, "dislikes": 0, "comments": [], "quote": item}
#Uses enumerate function to number the quoteslist and convert it into a set of numbered pairs


# this is main route that returns works so that we know the backend is working
@app.route('/')
def index():
    return "works"


# post route with like, when recieving this route we know that we recieved a like for the quote
@app.route('/like', methods=["POST"])
def like():
    # this sets data equal to the dictionary with a quote and the actuall quote
    data = request.data
    id = data["id"]
    # this goes inside of the dictionary quote data and finds the quote and adds one to the like
    quotedata[id]["likes"] += 1
    return quotedata[id]["likes"]

@app.route('/comment', methods=["POST"])
def comment():
    data=request.data
    id = data["id"]
    name = data["name"]
    message = data["message"]
    quotedata[id]["comments"].append({"name": name, "message":message})
    return quotedata[id]["comments"]

@app.route('/dislike', methods=["POST"])  # Dislike post route
def dislike():
    data = request.data  # sets the data variable equal to the quote and the actual quote
    # uses the data quote and adds one to the dislike
    id = data["id"]
    quotedata[id]["dislikes"] += 1
    return quotedata[id]["dislikes"]


@app.route('/quote', methods=["GET"])
def quote():
    # uses the random choice function to set the quote and info = to the actual quote
    id, info = random.choice(list(quotedata.items()))
    dic = {}  # sets the dic dictionary empty
    dic[id] = info  # sets the key id = to the likes and dislikes as the term
    return dic  # returns the dictionary dic with the quotes and likes and dislikes
