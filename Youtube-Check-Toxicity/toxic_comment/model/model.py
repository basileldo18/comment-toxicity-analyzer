from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn as nn

# Load the pre-trained model and tokenizer
model_name_or_path = 'unitary/toxic-bert'
tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name_or_path=model_name_or_path)
model = AutoModelForSequenceClassification.from_pretrained(pretrained_model_name_or_path=model_name_or_path)

# Determine the device (CPU or GPU) for inference
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Define the function to check text toxicity
def check_text_toxicity(text) -> dict:
    ''' Check the text for toxicity
        Parameters:
        - text: str
        Returns:
        - dict
    '''
    try:
        print('Started checking toxicity...')
        
        # Tokenize and encode the input text
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        inputs = {key: val.to(device) for key, val in inputs.items()}
        
        # Perform model inference
        outputs = model(**inputs)
        
        # Calculate probabilities
        sigmoid = nn.Sigmoid()
        probabilities = sigmoid(outputs.logits)
        probabilities = probabilities.to('cpu').detach().numpy()
        
        # Map label indices to label names
        id2label = model.config.id2label
        
        # Initialize result dictionary
        result = {
            'status': 1,
            'message': 'Request successful',
            'response': {
                'toxic': False,
                'severe_toxic': False,
                'obscene': False,
                'threat': False,
                'insult': False,
                'identity_hate': False
            }
        }
        
        # Update result dictionary based on model predictions
        for index, label_name in id2label.items():
            if probabilities[0][index] > 0.85:  # Adjust threshold as needed
                result['response'][label_name] = True
        
        print('Success...')
    
    except Exception as e:
        print(f'Error occurred: {str(e)}')
        result = {
            'status': -1,
            'message': 'Error at the model level.',
            'response': {}
        }
    
    return result

# Example usage:
input_text = "This is a toxic comment."
output = check_text_toxicity(input_text)
print(output)
