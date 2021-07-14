from fastapi import File, UploadFile, APIRouter, HTTPException, status
from starlette.responses import StreamingResponse
import io

from ..services import excel


router = APIRouter()


@router.post("/excel/{tab}", tags=["Upload"])
async def xls_total_price(tab, file: UploadFile = File(...)):
    """Calculate the total price in each row 

    Args:
        aba (string): spreadsheet tab
        file (UploadFile, optional): file. Defaults to File(...).

    Returns:
        spreadsheet: the spreadsheet to be downloaded
    """
    df, msg = excel.run(file, tab)

    if msg != None:
        raise HTTPException(status_code=404, detail = msg)
        
    # write dataframe in excel format to BytesIO buffer
    stream = io.BytesIO()
    df.to_excel(stream, encoding='utf-8', index=False, header=True)
    stream.seek(0)

    # Create a streaming response in xls format. 
    response = StreamingResponse(stream, media_type="application/xls", status_code=201)
    response.headers["Content-Disposition"] = "attachment; filename=export.xls"
    response.status = 201

    return response