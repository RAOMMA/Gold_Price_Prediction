import joblib
import pandas as pd
import argparse

# Load your encoder and model
loaded_model = joblib.load('C:/salman/ML/gold price predection/model.joblib')

def predict_price(args):
    # Create a DataFrame from the input data
    input_df = [(args.SPX,args.USD,args.SLV,args.USD)]

    print(input_df)

    # Make predictions
    pred = loaded_model.predict(input_df)
    return pred[0]

if __name__ == "__main__":
    # Set up argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description='GOLD house price')
    parser.add_argument('--SPX', type=float,required=True, help='SPX')
    parser.add_argument('--USO', type=float,required=True, help='USO')
    parser.add_argument('--SLV', type=float,required=True, help='SLV')
    parser.add_argument('--USD', type=float,required=True, help='EUR/USD')

    args = parser.parse_args()

    # Call the predict_price function with the parsed arguments
    prediction = predict_price(args)
    print(f"Predicted price is: {prediction}")