from pydantic import BaseModel
from typing import Optional

class InsertAuthenticationLog(BaseModel):
    session_id: str
    user_id: Optional[str] = None
    serial_number: str
    token: str
    is_auth_succeed: bool
    msg: Optional[str] = None
    created_at: str

class InsertOneTurnLog(BaseModel):
    request_id: str
    session_id: str
    user_id: str
    created_at: str
    user_chat: str
    naly_chat: str

class InsertPerformanceLog(BaseModel):
    request_id: str
    session_id: str
    user_id: str
    component_id: int
    data: Optional[str] = None
    execution_time: int

class InsertPerformancesLog(BaseModel):
    request_id: str
    session_id: str
    user_id: str

    retrieval_result: str
    inference_result: str

    main_chain_time: int
    rag_time: int
    inference_time: int
    tts_time: int

class InsertSummaryLog(BaseModel):
    session_id: str
    summary: str
    summary_type: int
    user_id: str
    created_at: str

class InsertSummariesLog(BaseModel):
    session_id: str
    front_summary: list
    back_summary: list
    nalytic_summary: str
    user_id: str
    created_at: str

class BaseResponseDto(BaseModel):
    status_code: int
    msg: str
    data: Optional[object]

    @staticmethod
    def ok(status_code: int = 200, msg: str = "succeed", data: object = None):
        return {
            "status_code": status_code,
            "msg": msg,
            "data": data
        }

    @staticmethod
    def failed(status_code: int = 400, msg: str = "failed", data: object = None):
        return {
            "status_code": status_code,
            "msg": msg,
            "data": data
        }