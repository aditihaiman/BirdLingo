from flask import Flask
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)


current_id = 9

birds = {
    0: {
        "id": 0,
        "name": "Blue Jay",
        "latin_name": "Cyanocitta cristata",
        "image": "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/311635911/1800",
        "colors": ["blue", "white", "grey", "black"],
        "description": "Large crested songbird with broad, rounded tail. Blue Jays are smaller than crows, larger than robins. White or light gray underneath, various shades of blue, black, and white above. Blue Jays make a large variety of calls that carry long distances. Most calls produced while the jay is perched within a tree. Usually flies across open areas silently, especially during migration. Stuffs food items in throat pouch to cache elsewhere; when eating, holds a seed or nut in feet and pecks it open. Blue Jays are birds of forest edges. A favorite food is acorns, and they are often found near oaks, in forests, woodlots, towns, cities, parks.",
        "rarity": 0,
        "size": "robin",
        "order": "Passeriformes",
        "family": "Corvidae"
    },
    1:{
        "id": 1,
        "name": "Fish Crow",
        "latin_name": "Corvus ossifragus",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/302400101-1280px.jpg",
        "colors": ["black"],
        "description": "Fish Crows are all black. Immatures are less glossy and can become brownish as their feathers wear in their first year. Fish Crows are very social birds—look for them in pairs in the breeding season and up to several hundred or more during migration or winter. When feeding and roosting they may mix with American Crows. When Fish Crows give their distinctive nasal calls from the ground, they often puff out their neck and body feathers, forming a distinctive, ragged ruff on the throat.",
        "rarity": 0,
        "size": "crow",
        "order": "Passeriformes",
        "family": "Corvidae"
    },
    2:{
        "id": 2,
        "name": "Northern Cardinal",
        "latin_name": "Cardinalis cardinalis",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/297087301-720px.jpg",
        "colors": ["red", "black", "orange", "brown"],
        "description": "The male Northern Cardinal is perhaps responsible for getting more people to open up a field guide than any other bird. They’re a perfect combination of familiarity, conspicuousness, and style: a shade of red you can’t take your eyes off. Even the brown females sport a sharp crest and warm red accents. Cardinals don’t migrate and they don’t molt into a dull plumage, so they’re still breathtaking in winter’s snowy backyards. In summer, their sweet whistles are one of the first sounds of the morning.",
        "rarity": 0,
        "size": "robin",
        "order": "Passeriformes",
        "family": "Cardinalidae"
    },
    3:{
        "id": 3,
        "name": "Summer Tanager",
        "latin_name": "Piranga rubra",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/67450051-1280px.jpg",
        "colors": ["red", "yellow", "grey", "black"],
        "description": "The only completely red bird in North America, the strawberry-colored male Summer Tanager is an eye-catching sight against the green leaves of the forest canopy. The mustard-yellow female is harder to spot, though both sexes have a very distinctive chuckling call note. Fairly common during the summer, these birds migrate as far as the middle of South America each winter. All year long they specialize in catching bees and wasps on the wing, somehow avoiding being stung by their catches.",
        "rarity": 6,
        "size": "robin",
        "order": "Passeriformes",
        "family": "Cardinalidae"
    },
    4:{
        "id": 4,
        "name": "Scarlet Tanager",
        "latin_name": "Piranga olivacea",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/297081931-1280px.jpg",
        "colors": ["red", "black", "yellow", "green"],
        "description": "Male Scarlet Tanagers are among the most blindingly gorgeous birds in an eastern forest in summer, with blood-red bodies set off by jet-black wings and tail. They’re also one of the most frustratingly hard to find as they stay high in the forest canopy singing rich, burry songs. The yellowish-green, dark-winged females can be even harder to spot until you key in on this bird’s chick-burr call note. In fall, males trade red feathers for yellow-green and the birds take off for northern South America.",
        "rarity": 4,
        "size": "robin",
        "order": "Passeriformes",
        "family": "Cardinalidae"
    },
    5:{
        "id": 5,
        "name": "Black-capped Chickadee",
        "latin_name": "Poecile atricapillus",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/302472691-480px.jpg",
        "colors": ["brown", "white", "grey", "black"],
        "description": "A bird almost universally considered “cute” thanks to its oversized round head, tiny body, and curiosity about everything, including humans. The chickadee’s black cap and bib; white cheeks; gray back, wings, and tail; and whitish underside with buffy sides are distinctive. Its habit of investigating people and everything else in its home territory, and quickness to discover bird feeders, make it one of the first birds most people learn.",
        "rarity": 1,
        "size": "sparrow",
        "order": "Passeriformes",
        "family": "Paridae"
    },
    6:{
        "id": 6,
        "name": "Tufted Titmouse",
        "latin_name": "Baeolophus bicolor",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/302627281-1280px.jpg",
        "colors": ["orange", "white", "grey", "black"],
        "description": "A little gray bird with an echoing voice, the Tufted Titmouse is common in eastern deciduous forests and a frequent visitor to feeders. The large black eyes, small, round bill, and brushy crest gives these birds a quiet but eager expression that matches the way they flit through canopies, hang from twig-ends, and drop in to bird feeders. When a titmouse finds a large seed, you’ll see it carry the prize to a perch and crack it with sharp whacks of its stout bill.",
        "rarity": 1,
        "size": "sparrow",
        "order": "Passeriformes",
        "family": "Paridae"
    },
    7:{
        "id": 7,
        "name": "White-throated Sparrow",
        "latin_name": "Zonotrichia albicollis",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/64980371-1280px.jpg",
        "colors": ["yellow", "white", "brown", "black", "grey"],
        "description": "Crisp facial markings make the White-throated Sparrow an attractive bird as well as a hopping, flying anatomy lesson. There’s the black eyestripe, the white crown and supercilium, the yellow lores, the white throat bordered by a black whisker, or malar stripe. They’re also a great entrée into the world of birdsong, with their pretty, wavering whistle of Oh-sweet-canada. These forest sparrows breed mostly across Canada, but they’re familiar winter birds across most of eastern and southern North America and California.",
        "rarity": 0,
        "size": "sparrow",
        "order": "Passeriformes",
        "family": "Passerellidae"
    },
    8:{
        "id": 8,
        "name": "Field Sparrow",
        "latin_name": "Spizella pusilla",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/297663691-1280px.jpg",
        "colors": ["brown", "white", "grey", "black"],
        "description": "The clear, “bouncing-ball” trill of the Field Sparrow is a familiar summer sound in brushy fields and roadsides of the East and Midwest. The singer is a small, warm-toned sparrow with a rusty cap, neat white eyering, and pink bill. Though still common, Field Sparrows have declined sharply in the last half-century, partly because of the expansion of suburbs, where Field Sparrows will not nest. Populations in the prairies have remained strong thanks in part to measures like the Conservation Reserve Program.",
        "rarity": 8,
        "size": "sparrow",
        "order": "Passeriformes",
        "family": "Passerellidae"
    },
    9:{
        "id": 9,
        "name": "American Tree Sparrow",
        "latin_name": "Spizelloides arborea",
        "image": "https://www.allaboutbirds.org/guide/assets/photo/297719081-1280px.jpg",
        "colors": ["brown", "white", "grey", "black"],
        "description": "Plump and long-tailed, American Tree Sparrows are busy visitors in winter backyards and weedy, snow-covered fields across southern Canada and the northern United States. Hopping up at bent weeds or even beating their wings to dislodge seeds from grass heads, they scratch and peck the ground in small flocks, trading soft, musical twitters. Come snowmelt, these small rusty-capped and smooth-breasted sparrows begin their long migrations to breeding grounds in the tundra of the far North.",
        "rarity": 7,
        "size": "sparrow",
        "order": "Passeriformes",
        "family": "Passerellidae"
    },
}


# ROUTES

@app.route("/")
def home():
    global birds
    return render_template("home.html", birds=birds)


@app.route("/add_bird", methods=["GET", "POST"])
def add_bird():
    global birds
    global current_id

    new_bird = request.get_json()
    current_id += 1
    new_bird['id'] = current_id
    birds[current_id] = new_bird

    return [new_bird, current_id]

@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/search_results/<search_term>", methods=["GET", "POST"])
def search(search_term=None):
    global birds 
    
    print("searching for: ", search_term)
    name_results = {}
    size_results = {}
    color_results = {}
    for i in range(current_id+1):
        if(search_term.lower() in birds[i]["name"].lower()):
            name_results[birds[i]['name']] = list(birds[i]['name'].lower().partition(search_term.lower()))
            name_results[birds[i]['name']].append(birds[i]['id'])
        if(search_term.lower() in birds[i]["size"]):
            size_results[birds[i]['name'].lower()] = list(birds[i]['size'].partition(search_term.lower()))
            size_results[birds[i]['name'].lower()].append(birds[i]['id'])
        for color in birds[i]["colors"]:
            if(search_term.lower() in color):
                color_results[birds[i]["name"].lower()] = list(color.partition(search_term.lower()))
                color_results[birds[i]['name'].lower()].append(birds[i]['id'])
                break 
    
    return render_template('search_results.html', results=[name_results, size_results, color_results], search_term=search_term)


@app.route("/view/<id>")
def view_bird(id=None):
    global birds

    bird = birds[int(id)]

    return render_template('view.html', bird=bird)


@app.route("/edit/<id>")
def edit(id=None):
    global birds
    bird = birds[int(id)]
    return render_template('edit.html', bird=bird, id=id)

@app.route("/edit_bird", methods=["GET", "POST"])
def edit_bird():
    global birds

    data = request.get_json()
    updated_bird = data[0]
    id = data[1]
    updated_bird['id'] = id
    print(id)
    birds[int(id)] = updated_bird
    print(birds[int(id)])
    return [birds[int(id)], id]

if __name__ == "__main__":
    app.run(debug=True)
