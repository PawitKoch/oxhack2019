from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

ENDPOINT = "https://westeurope.api.cognitive.microsoft.com/"

# Replace with a valid key
training_key = "70218db9f6f648b5b300774a835628a4"
prediction_key = "423c23bf69f44f2c83780e2c7ac16e9a"
prediction_resource_id = "/subscriptions/09220dc7-b210-4fe4-a9b8-c2c74d4983e2/resourceGroups/Test1/providers/Microsoft.CognitiveServices/accounts/Custom_Training"

publish_iteration_name = "FinalIteration"
project_id = "39ee7be7-fce5-447b-8650-96b32acdd3d1"


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
