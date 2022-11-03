from . import app
from flask import request
import uuid

# Goal Forum
goals = {}


# approute to give goal data to the frontend
@app.route('/getgoal', methods=["GET"])
def getgoal():
    return goals


# Post route that adds goals to the forum
@app.route('/addgoal', methods=["POST"])
def addgoal():
    # retrieves the data from the fronted, the goal, the person who wrote the goal
    data = request.json
    goal = data["goal"]
    name = data["name"]
    # assigns each goal a specific uuid to differentiate the goals in the dictionary
    goal_id = str(uuid.uuid4())
    goals[goal_id] = {  # this adds an entry into the dictionary, adds the goal, along with the emoji reactions
        "goal": goal, "name": name, "smileys": 0, "thumbs": 0, "heart": 0
    }
    return goals  # returns the most recent goal to the frontend to keep website updated


@app.route("/react", methods=["POST"])  # reaction route
def react():
    data = request.json  # retrieves the data
    goal_id = data["goal_id"]
    # gets the data that tells backend what reaction it is
    reaction = data["reaction"]
    goals[goal_id][reaction] += 1  # adds one reaction to the goal
    return goals[goal_id]
