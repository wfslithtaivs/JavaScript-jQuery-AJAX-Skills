"""Flask server for Javascript assessment.

IMPORTANT: you don't need to change this file at all to finish
the assessment!
"""

from random import randint
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

PUPPIES = {"1": "http://cdn1-www.dogtime.com/assets/uploads/gallery/30-impossibly-cute-puppies/impossibly-cute-puppy-2.jpg",
           "2": "http://pictures.4ever.eu/data/download/animals/dogs/husky-puppies,-two-puppies-147859.jpg",
           "3": "http://www.cutestpaw.com/wp-content/uploads/2012/12/Three-pups-just-hanging-around.jpg",
           "lots": "http://www.lifedaily.com/wp-content/uploads/2015/09/puppy-pile-5-terriblycute.com_.jpg"}


@app.route("/")
def show_index():
    """Show the index page"""

    return render_template("index.html")


@app.route("/practice")
def show_practice():
    """Show the practice page."""

    return render_template("js-practice.html")


@app.route("/assessment")
def show_assessment():
    """Show the assessment page."""

    return render_template("js-assessment.html")


@app.route("/puppies.json")
def get_puppies():
    """Return a URL linking to a photo of the requested number of puppies."""

    #get the form data from the AJAX request
    num_puppies = request.args.get("num-puppies")

    #get the appropriate URL
    puppy_url = PUPPIES.get(num_puppies)

    #package everything up in a dictionary, jsonify it, and return it
    result_data = {"url": puppy_url}
    return jsonify(result_data)



@app.route("/t-rex-attack.json", methods=["POST"])
def bite_all_the_things():
    """Returns a random destruction reaction and corresponding image."""

    #get the form data from the AJAX request
    target = request.form.get("attack-target")

    #pick a random level of destruction
    destruction_level = randint(0, 4)
    reactions = ["Aw! He's so cute!",
                 "What a mess!",
                 "Oh. That doesn't look good.",
                 "We weren't prepared for this.",
                 "Total destruction!"]
    reaction = reactions[destruction_level]

    # make url proportionate to the size of the t-rex
    img_size = destruction_level + 1
    base_url = "https://ih1.redbubble.net/image.318166904.3572/flat,"
    img_url = "{size}00x{size}00,075,f.u2.jpg".format(size=img_size)
    t_rex_img_url = base_url + img_url

    #create and return a reaction to the t-rex attack
    response_str = (
        "{reaction} {target} will never be the same!"
        .format(reaction=reaction,
                target=target,))
    response = {"reaction": response_str,
                "img": t_rex_img_url}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
