from fastapi import File, UploadFile, APIRouter, HTTPException, status
from starlette.responses import StreamingResponse
import io

from ..services import csv


router = APIRouter()


@router.post("/csv", tags=["Upload"])
async def csv_total_price(file: UploadFile = File(...)):
    """Calculate the total price in each row 

    Args:
        file (UploadFile, optional): file. Defaults to File(...).

    Returns:
        spreadsheet: the spreadsheet to be downloaded
    """
    df, msg = csv.run(file)

    if msg != None:
        raise HTTPException(status_code=404, detail = msg)
        
    # write dataframe in excel format to BytesIO buffer
    stream = io.BytesIO()
    df.to_csv(stream, encoding='utf-8', index=False, header=True)
    stream.seek(0)

    # Create a streaming response in xls format. 
    response = StreamingResponse(stream, media_type="text/x-csv", status_code=201)
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    response.status = 201

    return response