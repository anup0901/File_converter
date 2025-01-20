import logging
import os
from .file_converter import get_converter,FileConverter
from fastapi import Depends, FastAPI,HTTPException

appf=FastAPI(docs_url='/')

logging.basicConfig(filename='converter.log',level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@appf.get('/convert-file')
async def trigger(output_dir:str,app:FileConverter=Depends(get_converter)):
    output_dir=os.path.join('files/',output_dir)
    input_dir=os.getenv('input_dirr')
    try:
        if not os.path.exists(input_dir):
            raise HTTPException(status_code=400, detail="Input directory does not exist")

        # Call the conversion function
        app.conversion(input_dir, output_dir)
        print(input_dir)
        print(output_dir)
        logging.info('The file has been converted')
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   

