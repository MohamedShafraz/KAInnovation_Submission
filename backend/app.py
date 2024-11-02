from flask import Flask, jsonify, render_template, request
from rag_application import answer_question
from flask_cors import CORS

# from finetuning import fine_tune_model
from chat_with_pdf import answer_pdf
from inject_vector import inject_to_faiss, inject_to_pinecone
import tempfile
import os

app = Flask(__name__)
CORS(app)


@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/answer_question", methods=["POST"])
def api_answer_question():
    data = request.json
    print(data)
    question = data["question"]
    model = data["model"]
    database_name = data["database"]

    try:
        result, relevant_images = answer_question(question, model, database_name)
        return jsonify({"result": result, "relevant_images": relevant_images})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/finetune", methods=["POST"])
def finetune():
    file = request.files["file"]
    suffix = request.form["suffixName"]
    api_key = request.form["apiKey"]
    try:
        model_id = fine_tune_model(file, suffix, api_key)
        return jsonify({"model_id": model_id})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/inject_to_vector_db", methods=["POST"])
def inject_to_vector_db():
    file = request.files["file"]
    database_choice = request.form["database"]
    try:
        if database_choice == "Faiss":
            inject_to_faiss(file)
        else:
            inject_to_pinecone(file)
        return jsonify(
            {"message": f"Data has been successfully injected into {database_choice}."}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/chat_with_pdfs", methods=["POST"])
def chat_with_pdfs():
    question = request.form["question"]
    file = request.files["file"]
    try:
        # Save the file temporarily
        temp_dir = tempfile.TemporaryDirectory()
        temp_pdf_path = os.path.join(temp_dir.name, file.filename)
        file.save(temp_pdf_path)

        answer, images_base64 = answer_pdf(question, temp_pdf_path)

        # Optionally, handle images_base64 if needed

        temp_dir.cleanup()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
