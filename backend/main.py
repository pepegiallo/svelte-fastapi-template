from fastapi import FastAPI, Request
from datetime import datetime
from config import VERSION, STATUS_OK, STATUS_ERROR
from models import HealthCheckResponse, Endpoint, RootResponse
from urllib.parse import urljoin

app = FastAPI()
start_time = datetime.now()

@app.get('/health', response_model=HealthCheckResponse, summary='Health', description='Returns application health')
async def health_check():
    current_time = datetime.now()
    return HealthCheckResponse(
        status=STATUS_OK,
        uptime=str(datetime.now() - start_time),
        version=VERSION,
        timestamp=current_time.isoformat()
    )

@app.get("/", response_model=RootResponse)
async def root(request: Request, summary='Root'):
    return RootResponse(
        message='Welcome to the API',
        version=VERSION,
        documentation_url=urljoin(str(request.base_url), 'docs')
    )
