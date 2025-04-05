from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter(
    prefix="/test",
    tags=["Health"]
)

@router.get(
    "/health",
    summary="Health check endpoint",
    description="Returns the health status of the API",
    response_description="Health status",
    responses={
        200: {
            "description": "Successful health check",
            "content": {
                "application/json": {
                    "example": {"status": "healthy", "message": "API is running"}
                }
            }
        },
        500: {
            "description": "Internal server error",
            "content": {
                "application/json": {
                    "example": {"detail": "Health check failed: error message"}
                }
            }
        }
    }
)
async def health_check():
    try:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"status": "healthy", "message": "API is running"},
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET",
                "Access-Control-Allow-Headers": "Content-Type"
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Health check failed: {str(e)}"
        )