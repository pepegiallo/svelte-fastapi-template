from pydantic import BaseModel

class HealthCheckResponse(BaseModel):
    status: str
    uptime: str
    version: str
    timestamp: str

class Endpoint(BaseModel):
    path: str
    description: str

class RootResponse(BaseModel):
    message: str
    version: str
    documentation_url: str