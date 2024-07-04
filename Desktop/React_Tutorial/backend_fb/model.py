from langchain_openai import ChatOpenAI

def Answer (text):
    API_KEY = ''

    llm = ChatOpenAI(model="gpt-4",
                        temperature=0,
                        max_tokens=None,
                        timeout=None,
                        max_retries=2,
                        api_key=API_KEY,
                        )

    messages = [
        (
            "system",
            "너는 이제 뭐든지 부정적으로 바꿔주는 마법의 주문이야.내가 하는 예시를 보고 모든 문장을 부정적으로 바꿔줘. 문장에 투정과 좆같음을 조금 길게 심어줘. 항상 마지막엔 존나 잖아~🍀를 까먹지 말아줘 물이 반이나 차있어 -> 아~ 연습 끝나고 목 말라 죽겠는데 물이 반 밖에 안차있네~ 씨빠~ 좆같은거~ 개빡치잖아~? 존나 빡치네~ 🍀\\n 과외가 열시에 끝나 -> 아 돈벌기 씨발 존나 힘드네~ 도대체 몇시간을 쳐 해야 하는거야? 존~나 힘들다~🍀 ",
        ),
        ("human", text),
    ]
    ai_msg = llm.invoke(messages)
    return ai_msg.content

