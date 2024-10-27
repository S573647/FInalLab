import requests
import json

# Replace with your Cognitive Services key and endpoint
subscription_key = "edcf6be79d264e92871af9439f4c0b79"
endpoint = "https://kpimageanalysis.cognitiveservices.azure.com/"

# The URL of the image you want to analyze
image_url = "https://t4.ftcdn.net/jpg/07/30/19/11/240_F_730191183_j3cebFtikbhkDwVsnE1c6OmV9Cjc6kqe.jpg"


# The URL of the Computer Vision API
analyze_url = endpoint + "vision/v3.1/analyze"

# Set the parameters for the analysis
params = {
    "visualFeatures": "Categories,Tags,Description,Color,Objects,Tags"
}
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/json"
}

data = {
    "url": image_url
}

response = requests.post(analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()

analysis = response.json()
print(json.dumps(analysis, indent=4))

# File to write the tags and results
output_file = "tags_results.txt"

# Open the file for writing
with open(output_file, "w") as file:
    tags = analysis['tags']
    for tag in tags:
        name = tag['name']
        confidence = tag['confidence']
        result = f"Tag: {name}, Confidence: {confidence:.2f}\n"
        
        # Determine if the confidence score meets a threshold
        if confidence > 0.8:  # Example threshold
            result += f"Tag '{name}' matches the image content well with confidence {confidence:.2f}.\n"
        else:
            result += f"Tag '{name}' does not match the image content well (low confidence: {confidence:.2f}).\n"
        
        # Write the result to the file
        file.write(result)

print(f"Tags and results written to {output_file}")
