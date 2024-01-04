import pandas as pd

def convert_excel_to_single_column(input_file, output_file):
    # Read Excel file into a pandas DataFrame
    df = pd.read_excel(input_file, header=None)

    # Flatten the DataFrame to a single column
    result = pd.DataFrame(df.values.flatten(), columns=['Combined Column'])

    # Save the result to a new Excel file
    result.to_excel(output_file, index=False)

if __name__ == "__main__":
    # Replace 'input.xlsx' with the name of your input Excel file
    input_excel_file = 'input.xlsx'

    # Replace 'output.xlsx' with the desired name of the output Excel file
    output_excel_file = 'output.xlsx'

    convert_excel_to_single_column(input_excel_file, output_excel_file)
