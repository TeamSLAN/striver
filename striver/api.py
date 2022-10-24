from . import app
import random
from flask import request
quoteslist = ["“Nature has given us all the pieces required to achieve exceptional wellness and health, but has left it to us to put these pieces together.”—Diane McLaren", 
"“It is only when we take chances, when our lives improve. The initial and the most difficult risk that we need to take is to become honest. —Walter Anderson",
"“When you change your thoughts, remember to also change your world.”—Norman Vincent Peale",
"“When you give joy to other people, you get more joy in return. You should give a good thought to happiness that you can give out.”— Eleanor Roosevelt",
"“Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.” — Mark Twain",
"“Learn as if you will live forever, live like you will die tomorrow.” — Mahatma Gandhi",
"“We cannot solve problems with the kind of thinking we employed when we came up with them.” — Albert Einstein",
"“Success usually comes to those who are too busy looking for it.” — Henry David Thoreau",
"“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie",
"“There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.” —Mister Rogers"]
# quoteslist sets the list of quotes
quotedata = {} # sets an empty dictionary that will get filled up
for item in quoteslist: #for loop that goes over every quote inside of quotes list
        quotedata[item] = {"likes":0, "dislikes":0} # inside of the dictionary the key is the quote and this loop adds likes and dislikes as the key for every quote

@app.route('/') # this is main route that returns works so that we know the backend is working
def index():
    
    return "works"


@app.route('/like', methods=["POST"]) #post route with like, when recieving this route we know that we recieved a like for the quote
def like():
    data = request.data # this sets data equal to the dictionary with a quote and the actuall quote
    quotedata[data["quote"]]["likes"] += 1 #this goes inside of the dictionary quote data and finds the quote and adds one to the like
    return 


@app.route('/dislike', methods=["POST"]) #Dislike post route
def dislike():
    data = request.data # sets the data variable equal to the quote and the actual quote
    quotedata[data["quote"]]["dislikes"] += 1 #uses the data quote and adds one to the dislike
    return


@app.route('/quote', methods=["GET"])
def quote():

    quote,info = random.choice(list(quotedata.items())) #uses the random choice function to set the quote and info = to the actual quote
    dic = {} # sets the dic dictionary empty
    dic[quote] = info #sets the key quote = to the likes and dislikes as the term
    return dic # returns the dictionary dic with the quotes and likes and dislikes
