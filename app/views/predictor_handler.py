from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

ENDPOINT = "https://westeurope.api.cognitive.microsoft.com/"

# Replace with a valid key
training_key = "***********"
prediction_key = "***********"
prediction_resource_id = "***********"

publish_iteration_name = "FinalIteration"
project_id = "***********"


def predict(image_path):
    predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)
    with open(image_path, "rb") as image_contents:
        results = predictor.classify_image(
             project_id, publish_iteration_name, image_contents.read())
        predictions = {}
       # Display the results.
        for prediction in results.predictions:
            predictions.__setitem__(prediction.tag_name, round(prediction.probability*100))

    return predictions
