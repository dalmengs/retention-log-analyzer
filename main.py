from fastapi import FastAPI
from database import Database
from model import *
import uvicorn

app = FastAPI()
PREFIX = "/api/v1"

@app.post(PREFIX + "/auth")
async def api_insert_authentication_log(insert_authentication_log_dto: InsertAuthenticationLog) -> BaseResponseDto:
    try:
        database.insert_authentication_log(
            session_id=insert_authentication_log_dto.session_id,
            user_id=insert_authentication_log_dto.user_id,
            serial_number=insert_authentication_log_dto.serial_number,
            token=insert_authentication_log_dto.token,
            is_auth_succeed=insert_authentication_log_dto.is_auth_succeed,
            msg=insert_authentication_log_dto.msg,
            created_at=insert_authentication_log_dto.created_at
        )
        return BaseResponseDto.ok()
    except Exception as e:
        return BaseResponseDto.failed(msg=str(e))

@app.post(PREFIX + "/turn")
async def api_insert_one_turn_log(insert_one_turn_log_dto: InsertOneTurnLog) -> BaseResponseDto:
    try:
        database.insert_one_turn_log(
            request_id=insert_one_turn_log_dto.request_id,
            session_id=insert_one_turn_log_dto.session_id,
            user_id=insert_one_turn_log_dto.user_id,
            created_at=insert_one_turn_log_dto.created_at,
            user_chat=insert_one_turn_log_dto.user_chat,
            naly_chat=insert_one_turn_log_dto.naly_chat
        )
        return BaseResponseDto.ok()
    except Exception as e:
        return BaseResponseDto.failed(msg=str(e))

@app.post(PREFIX + "/performance")
async def api_insert_performance_log(insert_performance_log_dto: InsertPerformanceLog) -> BaseResponseDto:
    try:
        database.insert_performance_log(
            request_id=insert_performance_log_dto.request_id,
            session_id=insert_performance_log_dto.session_id,
            user_id=insert_performance_log_dto.user_id,
            component_id=insert_performance_log_dto.component_id,
            data=insert_performance_log_dto.data,
            execution_time=insert_performance_log_dto.execution_time
        )
        return BaseResponseDto.ok()
    except Exception as e:
        return BaseResponseDto.failed(msg=str(e))

@app.post(PREFIX + "/performances")
async def api_insert_performance_log(insert_performance_log_dto: InsertPerformancesLog) -> BaseResponseDto:
    try:
        database.insert_performance_log(
            request_id=insert_performance_log_dto.request_id,
            session_id=insert_performance_log_dto.session_id,
            user_id=insert_performance_log_dto.user_id,
            component_id=0,
            data=None,
            execution_time=insert_performance_log_dto.main_chain_time
        )
        database.insert_performance_log(
            request_id=insert_performance_log_dto.request_id,
            session_id=insert_performance_log_dto.session_id,
            user_id=insert_performance_log_dto.user_id,
            component_id=1,
            data=insert_performance_log_dto.retrieval_result,
            execution_time=insert_performance_log_dto.rag_time
        )
        database.insert_performance_log(
            request_id=insert_performance_log_dto.request_id,
            session_id=insert_performance_log_dto.session_id,
            user_id=insert_performance_log_dto.user_id,
            component_id=2,
            data=insert_performance_log_dto.inference_result,
            execution_time=insert_performance_log_dto.inference_time
        )
        database.insert_performance_log(
            request_id=insert_performance_log_dto.request_id,
            session_id=insert_performance_log_dto.session_id,
            user_id=insert_performance_log_dto.user_id,
            component_id=3,
            data=None,
            execution_time=insert_performance_log_dto.tts_time
        )
        return BaseResponseDto.ok()
    except Exception as e:
        return BaseResponseDto.failed(msg=str(e))

@app.post(PREFIX + "/summary")
async def api_insert_summary_log(insert_summary_log_dto: InsertSummaryLog) -> BaseResponseDto:
    try:
        database.insert_summary_log(
            session_id=insert_summary_log_dto.session_id,
            summary=insert_summary_log_dto.summary,
            summary_type=insert_summary_log_dto.summary_type,
            user_id=insert_summary_log_dto.user_id,
            created_at=insert_summary_log_dto.created_at
        )
        return BaseResponseDto.ok()
    except Exception as e:
        return BaseResponseDto.failed(msg=str(e))

@app.post(PREFIX + "/summaries")
async def api_insert_summary_log(insert_summary_log_dto: InsertSummariesLog) -> BaseResponseDto:
    try:
        for front_summary in insert_summary_log_dto.front_summary:
            database.insert_summary_log(
                session_id=insert_summary_log_dto.session_id,
                summary=front_summary,
                summary_type=0,
                user_id=insert_summary_log_dto.user_id,
                created_at=insert_summary_log_dto.created_at
            )
        for back_summary in insert_summary_log_dto.back_summary:
            database.insert_summary_log(
                session_id=insert_summary_log_dto.session_id,
                summary=back_summary,
                summary_type=1,
                user_id=insert_summary_log_dto.user_id,
                created_at=insert_summary_log_dto.created_at
            )
        database.insert_summary_log(
            session_id=insert_summary_log_dto.session_id,
            summary=insert_summary_log_dto.nalytic_summary,
            summary_type=2,
            user_id=insert_summary_log_dto.user_id,
            created_at=insert_summary_log_dto.created_at
        )
        return BaseResponseDto.ok()
    except Exception as e:
        return BaseResponseDto.failed(msg=str(e))

if __name__ == "__main__":
    database = Database(test_environment=False)
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=9999
    )