import logging
from colorama import Fore, Style, init
import os
import pandas as pd

logging.basicConfig(filename='converter.log',level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class FileConverter:
    def conversion(self,input_dir:str,output_dir:str):
     for root, _, files in os.walk(input_dir): 
        for csv_file in files:
            
            if csv_file.endswith('.csv'):   # Check if the file is a CSV file
            
                csv_file_path = os.path.join(root, csv_file)   # Full path to the CSV file
                try:
                # Read the CSV file using pandas
                    df = pd.read_csv(csv_file_path)

            #to generate output json filename
                    json_filename=os.path.join(output_dir,os.path.basename(csv_file).replace('.csv','.json'))
                    os.makedirs(os.path.dirname(json_filename), exist_ok=True)
                    df.to_json(json_filename,orient='records',indent=4)
                    
                except Exception as e:
                    print(f"Error reading {csv_file}: {e}")

                else:
                    print(f"Converted{csv_file} to {json_filename}")
                finally:
                    print(Fore.RED+'completed conversion'+Style.RESET_ALL)
                    logging.info('completed')

                    

def get_converter()->FileConverter:
    print('instance created')
    return FileConverter()
