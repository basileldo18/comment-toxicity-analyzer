Comment Toxicity Analyzer
A web-based tool powered by AI to assess and analyze the toxicity of online comments. Using the Unitary Toxic-BERT model, this tool identifies various toxic behaviors like insults, threats, severe toxicity, and identity hate in text.

Features
Toxicity Detection: Analyzes input text for different types of toxicity (e.g., insults, threats, severe toxicity).

Real-time Feedback: Provides immediate feedback on whether a comment is toxic or not.

Pre-trained Model: Utilizes the pre-trained Unitary Toxic-BERT model for accurate predictions.

Tech Stack
Flask: Lightweight web framework for handling requests and serving the application.

Hugging Face Transformers: For loading and using the pre-trained BERT model.

PyTorch: Deep learning framework to run the BERT model for text classification.

CUDA: Utilized for GPU acceleration if available.

Setup & Installation
To run this project locally:

Clone the Repository:

bash
Copy
Edit
git clone https://github.com/basileldo18/comment-toxicity-analyzer.git
cd comment-toxicity-analyzer
Install Dependencies: Install required Python libraries using pip:

bash
Copy
Edit
pip install -r requirements.txt
Run the Application: Start the Flask development server:

bash
Copy
Edit
python app.py
Access the App: Open a web browser and navigate to http://127.0.0.1:5000/ to access the application.

API Usage
The API endpoint /api/text accepts GET requests with a text query parameter (jtext). It returns a JSON response with the toxicity analysis results.

Example Request:
bash
Copy
Edit
GET http://127.0.0.1:5000/api/text?jtext=Your%20input%20text%20here
Example Response:
json
Copy
Edit
{
  "status": 1,
  "message": "Request successful",
  "response": {
    "toxic": false,
    "severe_toxic": false,
    "obscene": false,
    "threat": false,
    "insult": false,
    "identity_hate": false
  }
}
Model
This project uses the Unitary Toxic-BERT model, a fine-tuned BERT-based model, designed to classify text into various categories of toxicity.

License
This project is open source and available under the MIT License. See the LICENSE file for more information.

Acknowledgements
Unitary Toxic-BERT: A pre-trained model for toxicity detection.

Flask: Web framework used for building the application.

Hugging Face: For providing the transformers library that simplifies the usage of pre-trained models.

You can adjust the requirements.txt to include the necessary packages, such as Flask, transformers, and torch. Let me know if you need help with that!
