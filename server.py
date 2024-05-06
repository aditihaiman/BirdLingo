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
        "image": "../static/media/red_tailed_hawk.jpeg",
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
        "attention": [
            "There is some background noise in this recording. Make sure you are listening carefully to the dove and not the other birds."
        ],
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
        "attention": [
            "Are the individual parts repeated?",
            "Is the quality clear like a whistle or harsh?",
        ],
        "characteristics": [
            "Short but complex parts are repeated multiple times in slightly different ways.",
            "A good way to remember this song is that is sounds like an opera singer with lots of vibrato.",
        ],
        "spectrogram": ["Note the repeated individual parts that are mostly similar"],
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
        "options": ["harsh", "falling pitch", "multiple parts", "variable pitch"],
        "spectro-visual": ["media/hawk-spectro.png"],
        "correct": [],
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
            "Northern Cardinal",
        ],
        "spectro-visual": ["media/cardinal-spectro.png"],
        "correct": [],
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
            "American Robin",
        ],
        "spectro-visual": ["media/hawk-spectro.png", "media/robin-spectro.png"],
        "correct": [],
    },
}


# ROUTES


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/learn/<int:id>")
def learn(id):
    if id == 0:  # Check if the request is for the introductory slide
        # Render the introductory template
        return render_template("extra_learn_layout.html", current_id=current_id)
    elif id == 1:
        return render_template("extra_learn_layout_1.html", current_id=current_id)
    else:
        # Adjust ID to align with existing data after the introduction
        adjusted_id = id - 2
        return render_template("learn_layout.html", learn_data=learn_data[adjusted_id])


@app.route("/learn_checkpoint")
def learn_checkpoint():
    return render_template("learn_checkpoint_layout.html")



@app.route("/quiz/<id>")
def quiz(id=None):
    global quiz_data
    return render_template("quiz_layout.html", quiz_data=quiz_data[int(id)])


@app.route("/results")
def results():
    return render_template("quiz_results.html")

@app.route("/transition")
def transition():
    return render_template("transition.html")


@app.route("/update_total", methods=["POST"])
def update_variable():
    global total
    new_value = request.form["variable"]
    if total <= int(new_value):
        total = total + 1
    print(total)
    return "Variable updated successfully!"


@app.route("/get_total", methods=["GET"])
def get_total():
    return jsonify({"variable": total})

@app.route("/clear_total", methods=["POST"])
def clear_total():
    global total
    total = 0
    return "Total cleared"


if __name__ == "__main__":
    app.run(debug=True)
