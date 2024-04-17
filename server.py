from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)


current_id = 9

total = 0

learn_data = {
    0: {
        "id": 0,
        "name": "Red-Tailed Hawk",
        "intro-text": "Let's start with something easy: ",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/319861731-1280px.jpg",
        "audio": "media/Hawk.mp3",
        "attention": [
            "When is it rising or falling in pitch?",
            "Are the pitches clear (like a whistle) or harsh?",
        ],
        "characteristics": [
            "Sounds like a harsh scream",
            "Short 2-3 second simple call",
            "Falling pitch",
        ],
        "spectrogram": [
            "Does this spectrogram look like it matches the Red Tailed Hawk call?",
            "Note the fuzziness instead of one clear line and the gentle downward slope. Fuzziness in a spectrogram is usually due to harsh sounds.",
        ],
        "spectro-visual": "media/hawk-spectro.png",
    },
    1: {
        "id": 1,
        "name": "Northern Cardinal",
        "intro-text": "Let's try another bird: ",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/297087301-720px.jpg",
        "audio": "media/Cardinal.mp3",
        "attention": [
            "How many sections are there to the song?",
            "Is there any repetition?",
            "Is the tone clear like a whistle or harsh like a scream?",
        ],
        "characteristics": [
            "Two parts: First is slow falling pitch, second is a series of fast notes going up and down",
            "Clear, whistle-like quality",
        ],
        "spectrogram": [
            "What do you notice about how the speed of the notes vary throughout the song?",
            "Does the spectrogram reflect these qualities?",
        ],
        "spectro-visual": "media/cardinal-spectro.png",
    },
    2: {
        "id": 2,
        "name": "Mourning Dove",
        "intro-text": "Let's try another bird: ",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/60386921-1280px.jpg",
        "audio": "media/Dove.mp3",
        "attention": ["There is some background noise in this recording. Make sure you are listening carefully to the dove and not the other birds."],
        "characteristics": [
            "Repeated 'coo-ing' sound",
            "Relatively low pitch that stays constant (doesn't move up or down)",
            "Clear-ish sound (not harsh but not as clear because of how low-pitched it is)",
        ],
        "spectrogram": [
            "Notice how the constant, low pitch is reflected in the spectrogram with lines at the bottom of the graph."
        ],
        "spectro-visual": "media/dove-spectro.png",
    },
    3: {
        "id": 3,
        "name": "American Robin",
        "intro-text": "Let's try another bird: ",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/303441381-1280px.jpg",
        "audio": "media/Robin.mp3",
        "attention": "",
        "characteristics": "",
        "spectrogram": "",
        "spectro-visual": "media/robin-spectro.png",
    },
}

quiz_data = {
    0: {
        "id": 0,
        "type": "multiple_choice",
        "text": "Select which qualities apply to the recording. Use the hint to see a spectrogram.",
        "image": "",
        "audio": ["media/Hawk.mp3"],
        "options": [
            "harsh",
            "falling pitch",
            "multiple parts",
            "variable pitch"
        ],
        "spectro-visual": ["media/hawk-spectro.png"],
        "correct": []
    },
    1: {
        "id": 1,
        "type": "multiple_choice",
        "text": "What bird is singing? Use the hint to see a spectrogram.",
        "image": "",
        "audio": ["media/Cardinal.mp3"],
        "options": [
            "Red Tailed Hawk",
            "American Robin",
            "Mourning Dove",
            "Northern Cardinal"
        ],
        "spectro-visual": ["media/cardinal-spectro.png"],
        "correct": []
    },
    2: {
        "id": 2,
        "type": "drag_drop",
        "text": "Drag the correct name to each recording. Use the hint to see a spectrogram.",
        "image": "",
        "audio": ["media/Hawk.mp3", "media/Robin.mp3"],
        "options": [
            "Northern Cardinal",
            "Mourning Dove",
            "Red-Tailed Hawk",
            "American Robin"
        ],
        "spectro-visual": ["media/hawk-spectro.png", "media/robin-spectro.png"],
        "correct": []
    }
}


# ROUTES


@app.route("/")
def home():
    return render_template("home.html")


# @app.route("/add_bird", methods=["GET", "POST"])
# def add_bird():
#     global birds
#     global current_id

#     new_bird = request.get_json()
#     current_id += 1
#     new_bird["id"] = current_id
#     birds[current_id] = new_bird

#     return [new_bird, current_id]


@app.route("/learn/<id>")
def learn(id=None):
    global learn_data
    return render_template("learn_layout.html", learn_data=learn_data[int(id)])

@app.route("/quiz/<id>")
def quiz(id=None):
    global quiz_data
    return render_template("quiz_layout.html", quiz_data=quiz_data[int(id)])


@app.route("/results")
def results():
    return render_template("quiz_results.html")

@app.route('/update_total', methods=['POST'])
def update_variable():
    global total
    new_value = request.form['variable']
    if total <= int(new_value):
        total = total + 1
    print(total)
    return "Variable updated successfully!"

@app.route('/get_total', methods=['GET'])
def get_total():
    return jsonify({'variable': total})


# @app.route("/search_results/<search_term>", methods=["GET", "POST"])
# def search(search_term=None):
#     global birds

#     print("searching for: ", search_term)
#     name_results = {}
#     size_results = {}
#     color_results = {}
#     for i in range(current_id + 1):
#         if search_term.lower() in birds[i]["name"].lower():
#             name_results[birds[i]["name"]] = list(
#                 birds[i]["name"].lower().partition(search_term.lower())
#             )
#             name_results[birds[i]["name"]].append(birds[i]["id"])
#         if search_term.lower() in birds[i]["size"]:
#             size_results[birds[i]["name"].lower()] = list(
#                 birds[i]["size"].partition(search_term.lower())
#             )
#             size_results[birds[i]["name"].lower()].append(birds[i]["id"])
#         for color in birds[i]["colors"]:
#             if search_term.lower() in color:
#                 color_results[birds[i]["name"].lower()] = list(
#                     color.partition(search_term.lower())
#                 )
#                 color_results[birds[i]["name"].lower()].append(birds[i]["id"])
#                 break

#     return render_template(
#         "search_results.html",
#         results=[name_results, size_results, color_results],
#         search_term=search_term,
#     )


# @app.route("/view/<id>")
# def view_bird(id=None):
#     global birds

#     bird = birds[int(id)]

#     return render_template("view.html", bird=bird)


# @app.route("/edit/<id>")
# def edit(id=None):
#     global birds
#     bird = birds[int(id)]
#     return render_template("edit.html", bird=bird, id=id)


# @app.route("/edit_bird", methods=["GET", "POST"])
# def edit_bird():
#     global birds

#     data = request.get_json()
#     updated_bird = data[0]
#     id = data[1]
#     updated_bird["id"] = id
#     print(id)
#     birds[int(id)] = updated_bird
#     print(birds[int(id)])
#     return [birds[int(id)], id]


if __name__ == "__main__":
    app.run(debug=True)
