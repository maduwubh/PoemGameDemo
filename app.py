from flask import Flask, render_template, request, redirect, url_for, jsonify

from services.game_service import GameService

app = Flask(__name__)

game = GameService()


@app.route("/")
def setup():
    game.reset()
    return render_template("setup.html")


@app.route("/start", methods=["POST"])
def start():
    title = request.form.get("title", "").strip() or "Untitled Poem"
    names_raw = request.form.get("players", "")
    names = [n.strip() for n in names_raw.split(",") if n.strip()]

    if len(names) < 2:
        return render_template(
            "setup.html", error="Enter at least 2 player names, separated by commas."
        )

    game.add_players(names)
    game.start_game(title)
    return redirect(url_for("play"))


@app.route("/play")
def play():
    if not game.started:
        return redirect(url_for("setup"))
    if game.is_over():
        return redirect(url_for("finished"))
    return render_template("play.html", game=game, current=game.current_player)


@app.route("/submit", methods=["POST"])
def submit():
    if not game.started or game.is_over():
        return redirect(url_for("setup"))

    line = request.form.get("line", "")
    game.submit_line(line)

    if game.is_over():
        return redirect(url_for("finished"))
    return redirect(url_for("play"))


@app.route("/finished")
def finished():
    if not game.started or not game.is_over():
        return redirect(url_for("setup"))
    return render_template("finished.html", poem=game.poem)


@app.route("/api/state")
def api_state():
    """Lets the play page poll for updates, so the growing poem stays
    visible to everyone watching, not just the player whose turn it is."""
    if not game.started:
        return jsonify({"lines": [], "current": None, "over": False})
    return jsonify(
        {
            "lines": game.poem.get_lines(),
            "current": game.current_player.name if game.current_player else None,
            "over": game.is_over(),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)