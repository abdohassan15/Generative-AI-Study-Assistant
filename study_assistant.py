"""
Study Assistant using Google Cloud Vertex AI (Gemini - NEW SDK)

This version uses the NEW Vertex AI SDK which works with models
like gemini-1.5-flash-001 for brand new GCP projects.
"""

# pip install google-cloud-aiplatform==1.68.0
# pip install google-cloud-vertexai

from vertexai import init
from vertexai.generative_models import GenerativeModel

# ---------- CONFIGURE THIS ----------
PROJECT_ID = "promising-booth-478220-j2"
LOCATION = "us-central1"
# Change this line! Use the current, stable model name.
MODEL_NAME = "gemini-2.5-flash" 
# ------------------------------------


def init_vertex_ai():
    """Initialize Vertex AI client."""
    init(project=PROJECT_ID, location=LOCATION)


def build_prompt(user_text: str) -> str:
    return f"""
You are a helpful study assistant for a university student.

The student gives you some notes or text. You must:
1. Summarize it clearly in 3–5 sentences.
2. Extract 5–7 key ideas as bullet points.
3. Suggest 3–5 exam-style questions based on the content.

Text from the student:
\"\"\"{user_text}\"\"\"
""".strip()


def analyze_text_with_gemini(user_text: str) -> str:
    prompt = build_prompt(user_text)

    # NEW SDK call
    model = GenerativeModel(MODEL_NAME)

    response = model.generate_content(prompt)

    return response.text


def main():
    print("=== Study Assistant (Vertex AI + Gemini) — NEW SDK ===")
    print("Paste your notes or text below. Finish input with an empty line:")
    print("--------------------------------------------------------------")

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    user_text = "\n".join(lines).strip()

    if not user_text:
        print("No text provided. Exiting.")
        return

    print("\nSending your text to Gemini on Vertex AI...")
    print("Please wait...\n")

    try:
        result = analyze_text_with_gemini(user_text)
    except Exception as e:
        print("❌ Error calling Vertex AI:", e)
        print("\nTroubleshooting:")
        print("- Ensure billing is enabled")
        print("- Ensure the model name is correct")
        print("- Ensure you accepted the Generative AI Terms in Vertex AI Studio")
        return

    print("=== AI Study Breakdown ===\n")
    print(result)
    print("\n==============================================")
    print("Tip: Save this in your notes or Notion 🚀")


if __name__ == "__main__":
    init_vertex_ai()
    main()
