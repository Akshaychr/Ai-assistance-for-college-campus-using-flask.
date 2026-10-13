"""Flask web app for answering common college-campus questions."""

from flask import Flask, jsonify, render_template, request

from faq_data import FAQS, find_answers, get_categories

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.get("/")
def home():
    return render_template("portal.html", categories=get_categories(), faqs=FAQS)


@app.post("/api/ask")
def ask():
    payload = request.get_json(silent=True) or {}
    question = str(payload.get("question", "")).strip()
    if not question:
        return jsonify({"error": "Please enter a question."}), 400
    return jsonify({"question": question, "answers": find_answers(question)})


@app.get("/api/faqs")
def faqs():
    category = request.args.get("category", "").strip().lower()
    entries = [item for item in FAQS if not category or item["category"].lower() == category]
    return jsonify(entries)


if __name__ == "__main__":
    app.run(debug=True)
