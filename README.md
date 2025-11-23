Generative AI Study Assistant (Vertex AI + Gemini)

A Python command-line application designed to transform raw study notes into structured, exam-ready material using Google's powerful Gemini model running on the Vertex AI platform.

This project showcases professional integration with modern Cloud LLM SDKs and robust input handling.

✨ Features

Intelligent Summarization: Condenses large blocks of text into a clear, concise summary (3-5 sentences).

Key Idea Extraction: Automatically extracts the 5-7 most critical concepts from the provided notes as structured bullet points.

NEW SDK Implementation: Utilizes the latest google-cloud-aiplatform SDK for seamless integration with modern Gemini models.

Robust Input Handling: Supports multi-line note pasting in the terminal, ending only when an empty line is detected.

🛠️ Technology Stack

Technology | Purpose 

Python 3.10+  | Core programming language.

Google Cloud Vertex AI | Enterprise AI platform for model deployment and management.

Gemini 2.5 Flash | The large language model used for analysis and generation.

vertexai SDK | The new, official Google Cloud SDK for calling Generative AI APIs.



🚀 Setup and Installation

Follow these steps to set up and run the Study Assistant locally.

1. Prerequisites

You must have the following installed:

Python 3.10 or higher

A Google Cloud Project with Billing enabled and the Vertex AI API enabled.

Authentication: You must be authenticated to GCP (e.g., using gcloud auth application-default login).

2. Clone the Repository

git clone [https://github.com/abdohassan15/Generative-AI-Study-Assistant.git](https://github.com/abdohassan15/Generative-AI-Study-Assistant.git)
cd Generative-AI-Study-Assistant

3. Install Dependencies

Use pip to install the required Python libraries.

pip install google-cloud-aiplatform==1.68.0
pip install google-cloud-vertexai


4. Configuration

Before running, update the global constants in main.py with your specific GCP details:

# main.py
# ---------- CONFIGURE THIS ----------
PROJECT_ID = "YOUR_PROJECT_ID_HERE" # e.g., "promising-booth-478220-j2"
LOCATION = "us-central1"
MODEL_NAME = "gemini-2.5-flash"
# ------------------------------------


5. Running the Application

Execute the main script from your terminal:

python main.py


The program will prompt you to paste your study notes.

💡 Usage Example

When prompted, paste your notes (you can paste multiple lines) and press Enter on an empty line to submit.

Input:

The Roman Republic (509 BC - 27 BC) was characterized by a system of magistrates, assemblies, and the Senate. The two Consuls were the chief executive officers, holding imperium and commanding the army. The Senate, though technically advisory, held immense political power due to its wealth and experience, guiding policy and finance. The shift to the Empire under Augustus marked the transition from a republic governed by laws to a principate ruled by an emperor.
(Empty line submitted)


Output:

=== AI Study Breakdown ===

**Summary**
The Roman Republic operated through a balance of power involving elected magistrates (chiefly the two Consuls who commanded the army), popular assemblies, and the influential, advisory Senate. The Senate's long-term power over policy and finance defined the Republic's direction for centuries. This governmental structure eventually gave way to the Roman Empire around 27 BC with the rise of Augustus, who established the rule of a single emperor (the Principate).

**Key Ideas**
* **Roman Republic Duration:** 509 BC to 27 BC.
* **Governing Bodies:** Magistrates, Assemblies, and the Senate.
* **Consuls:** Chief executive officers; held *imperium* (military and civil power).
* **Senate:** Advisory body with significant power over finance and policy.
* **Transition to Empire:** Marked by the rise of Augustus.
* **New System:** The Principate (rule by a single Emperor).

**Exam Questions**
1.  Contrast the role and power of the Consuls with that of the Senate during the Roman Republic.
2.  What was the significance of *imperium*, and which officials held this authority?
3.  Identify the key events or figures responsible for the transition from the Roman Republic to the Roman Empire.

==============================================
