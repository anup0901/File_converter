import os
from lib.file_converter import get_converter
import uvicorn
from dotenv import load_dotenv
import click

load_dotenv(dotenv_path='.local.properties',override=True)

@click.command()
@click.option('--mode', type=click.Choice(['api', 'manual'], 
                                          case_sensitive=False), help="Run the app in 'api' or 'manual' mode.")
def main(mode):
    """
    This script runs the application either in API mode (via FastAPI)
      or in Manual mode (via direct conversion).
    """
    # Get input and output directories from the environment variables
    input_dir = os.getenv('input_dirr')
    output_dir = os.getenv('output_dirr')

    # Use match expression to handle different modes
    match mode:
        case 'api':
            print("Running in API mode...")
            uvicorn.run('lib.fast_api:appf',host='0.0.0.0',port=8001,reload=True)
        
        case 'manual':
            print(f"Running in Manual mode with input: {input_dir} and output: {output_dir}")
            # Assuming `app.conversion` is the function to run in manual mode
            app=get_converter()
            app.conversion(input_dir, output_dir)




if __name__ == '__main__':
    main()



#old


'''
if __name__ == '__main__':  

    input_dir=os.getenv('input_dirr')
    output_dir=os.getenv('output_dirr')
    
    # --
    # app.conversion(input_dir,output_dir)

    # -- 
    uvicorn.run('lib.fast_api:app')
    '''


