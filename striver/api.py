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

quotedata = {}
for item in quoteslist:
        quotedata[item] = {"likes":0, "dislikes":0}

@app.route('/')
def index():
    
    return "works"


@app.route('/like', methods=["POST"])
def like():
    data = request.data
    quotedata[data["quote"]]["likes"] += 1
    return 


@app.route('/dislike', methods=["POST"])
def dislike():
    data = request.data
    quotedata[data["quote"]]["dislikes"] += 1
    return


@app.route('/quote', methods=["GET"])
def quote():

    quote,info = random.choice(list(quotedata.items()))
    dic = {}
    dic[quote] = info
    return dic
