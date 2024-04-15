from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)


current_id = 9

learn_data = {
    0: {
        "id": 0,
        "name": "Red-Tailed Hawk",
        "intro-text": "Let's start with something easy: ",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/319861731-1280px.jpg",
        "audio": "Hawk.mp3",
        "attention": "",
        "characteristics": "",
        "spectrogram": "",
        "spectro-visual": "",
    },
    1: {
        "id": 1,
        "name": "Northern Cardinal",
        "intro-text": "Let's try another bird: ",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/297087301-720px.jpg",
        "audio": "Cardinal.mp3",
        "attention": "",
        "characteristics": "",
        "spectrogram": "",
        "spectro-visual": "",
    },
        2: {
        "id": 2,
        "name": "Mourning Dove",
        "intro-text": "Let's try another bird: ",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/60386921-1280px.jpg",
        "audio": "Dove.mp3",
        "attention": "",
        "characteristics": "",
        "spectrogram": "",
        "spectro-visual": "",
    },
        3: {
        "id": 3,
        "name": "American Robin",
        "intro-text": "Let's try another bird: ",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/303441381-1280px.jpg",
        "audio": "Robin.mp3",
        "attention": "",
        "characteristics": "",
        "spectrogram": "",
        "spectro-visual": "",
    },
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
