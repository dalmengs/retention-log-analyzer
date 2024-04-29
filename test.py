from datetime import datetime
import random

retention_list = [
    (2024, 4, 25, 19, 22, 20),
    (2024, 4, 25, 23, 18, 14),
    (2024, 4, 26, 8, 14, 20),
    (2024, 4, 26, 14, 22, 20),
    (2024, 4, 27, 23, 22, 20),
    (2024, 4, 28, 7, 22, 20),
    (2024, 4, 29, 14, 22, 20),
    (2024, 4, 29, 20, 22, 20),
    (2024, 4, 30, 6, 22, 20),
    (2024, 4, 30, 10, 22, 20),
]

def make_time(year, month, day, hour, minute, second) -> str:
    dt = datetime(year, month, day, hour, minute, second)
    return dt.isoformat()

def make_random_id() -> str:
    c = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    return "".join([c[random.randrange(0, len(c))] for _ in range(30)])

conversation = {
    "user": "Hi, there!",
    "naly": "Hey, fam! How was it your day?"
}

def make_test_data() -> dict:
    ret = {
        "auth": [],
        "one_turn": [],
        "performance": [],
        "summary": []
    }
    for _ in range(3):
        session_id = make_random_id()
        ret["auth"].append({
                "session_id": session_id,
                "user_id": None,
                "serial_number": "naly_12345678",
                "token": "test_token_failed",
                "is_auth_succeed": False,
                "msg": "Authentication Failed: Invalid token",
                "created_at": make_time(*retention_list[0])
            })
    
    for _ in range(50): # make 50 users
        user_id = make_random_id()
        retention = random.randrange(0, 10)
        for i in range(retention + 1):
            session_id = make_random_id()
            ret["auth"].append({
                "session_id": session_id,
                "user_id": user_id,
                "serial_number": "naly_12345678",
                "token": "test_token",
                "is_auth_succeed": True,
                "msg": "Authentication Succeed",
                "created_at": make_time(*retention_list[i])
            })

            turn = random.randrange(1, 20)
            for j in range(turn):
                request_id = make_random_id()

                ret["one_turn"].append({
                    "request_id": request_id,
                    "session_id": session_id,
                    "user_id": user_id,
                    "created_at": make_time(*retention_list[i]),
                    "user_chat": conversation["user"],
                    "naly_chat": conversation["naly"]
                })

                rag = random.randrange(100, 700)
                inference = random.randrange(800, 2000)
                tts = random.randrange(500, 1400)

                if random.randrange(0, 100) < 3:
                    inference = random.randrange(8000, 10000)
                
                main = rag + inference + tts + 40

                ret["performance"].append({
                    "request_id": request_id,
                    "session_id": session_id,
                    "user_id": user_id,
                    "component_id": 0,
                    "data": None,
                    "execution_time": main
                })
                ret["performance"].append({
                    "request_id": request_id,
                    "session_id": session_id,
                    "user_id": user_id,
                    "component_id": 1,
                    "data": "test retrieval result",
                    "execution_time": rag
                })
                ret["performance"].append({
                    "request_id": request_id,
                    "session_id": session_id,
                    "user_id": user_id,
                    "component_id": 2,
                    "data": "Hi, there! -> Hey, fam! How was it your day?",
                    "execution_time": inference
                })
                ret["performance"].append({
                    "request_id": request_id,
                    "session_id": session_id,
                    "user_id": user_id,
                    "component_id": 3,
                    "data": None,
                    "execution_time": tts
                })
            ret["summary"].append({
                    "session_id": session_id,
                    "user_id": user_id,
                    "created_at": make_time(*retention_list[i]),
                    "summary": "User have talked about each's favorite foods.",
                    "summary_type": 0
                })
            ret["summary"].append({
                    "session_id": session_id,
                    "user_id": user_id,
                    "created_at": make_time(*retention_list[i]),
                    "summary": "User was curious about Naly's MBTI.",
                    "summary_type": 0
                })
            ret["summary"].append({
                    "session_id": session_id,
                    "user_id": user_id,
                    "created_at": make_time(*retention_list[i]),
                    "summary": "User loves pepperoni pizza.",
                    "summary_type": 1
                })
            ret["summary"].append({
                    "session_id": session_id,
                    "user_id": user_id,
                    "created_at": make_time(*retention_list[i]),
                    "summary": "Naly likes hambugers, with beef patties.",
                    "summary_type": 1
                })
            ret["summary"].append({
                    "session_id": session_id,
                    "user_id": user_id,
                    "created_at": make_time(*retention_list[i]),
                    "summary": "Naly's MBTI is INTP.",
                    "summary_type": 1
                })
            ret["summary"].append({
                    "session_id": session_id,
                    "user_id": user_id,
                    "created_at": make_time(*retention_list[i]),
                    "summary": "User's MBTI is ENFJ.",
                    "summary_type": 1
                })
            ret["summary"].append({
                    "session_id": session_id,
                    "user_id": user_id,
                    "created_at": make_time(*retention_list[i]),
                    "summary": "We were talked very fun tho!",
                    "summary_type": 2
                })

    return ret
