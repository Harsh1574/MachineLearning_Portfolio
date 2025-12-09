import numpy as np

# function to predict whether the object is a Rock or a Mine
def predict_object(model, input_data):

    # checking for all values are in proper format
    if (len(input_data) != 60):
        return f'Invalid input data. Expected 60 feature values. Recieved {len(input_data)}.'

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # make prediction
    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The object is a Rock'
    else:
        return 'The object is a Mine'