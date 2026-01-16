# Few-shot vs Zero-shot

- id: 6891a485-3fec-8331-964d-f6bafb8733d3
- date: 2025-08-05

```json
{
  "title": "Few-shot vs Zero-shot",
  "create_time": 1754375326.171142,
  "update_time": 1757747834.358353,
  "mapping": {
    "client-created-root": {
      "id": "client-created-root",
      "message": null,
      "parent": null,
      "children": [
        "d98acc71-a78d-4ee0-af15-851004128cda"
      ]
    },
    "d98acc71-a78d-4ee0-af15-851004128cda": {
      "id": "d98acc71-a78d-4ee0-af15-851004128cda",
      "message": {
        "id": "d98acc71-a78d-4ee0-af15-851004128cda",
        "author": {
          "role": "system",
          "name": null,
          "metadata": {}
        },
        "create_time": null,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            ""
          ]
        },
        "status": "finished_successfully",
        "end_turn": true,
        "weight": 0.0,
        "metadata": {
          "is_visually_hidden_from_conversation": true
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "client-created-root",
      "children": [
        "cad884ee-f63d-4c3a-996e-a78cafa1258d"
      ]
    },
    "cad884ee-f63d-4c3a-996e-a78cafa1258d": {
      "id": "cad884ee-f63d-4c3a-996e-a78cafa1258d",
      "message": {
        "id": "cad884ee-f63d-4c3a-996e-a78cafa1258d",
        "author": {
          "role": "user",
          "name": null,
          "metadata": {}
        },
        "create_time": 1754375325.82,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "  Few-shot vs Zero-shot에 대해설명해줘"
          ]
        },
        "status": "finished_successfully",
        "end_turn": null,
        "weight": 1.0,
        "metadata": {
          "selected_sources": [],
          "selected_github_repos": [],
          "serialization_metadata": {
            "custom_symbol_offsets": []
          },
          "request_id": "96a43c798e683085-ICN",
          "message_source": null,
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "d98acc71-a78d-4ee0-af15-851004128cda",
      "children": [
        "a3a42398-5993-4b0e-8249-145625f42fb4"
      ]
    },
    "a3a42398-5993-4b0e-8249-145625f42fb4": {
      "id": "a3a42398-5993-4b0e-8249-145625f42fb4",
      "message": {
        "id": "a3a42398-5993-4b0e-8249-145625f42fb4",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1754375325.9021804,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            ""
          ]
        },
        "status": "finished_successfully",
        "end_turn": null,
        "weight": 1.0,
        "metadata": {
          "request_id": "96a43c798e683085-ICN",
          "message_type": "next",
          "model_slug": "gpt-4o",
          "default_model_slug": "gpt-4o",
          "parent_id": "cad884ee-f63d-4c3a-996e-a78cafa1258d",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "cad884ee-f63d-4c3a-996e-a78cafa1258d",
      "children": [
        "31ecb01d-44db-459d-8d16-7e11473dde6a"
      ]
    },
    "31ecb01d-44db-459d-8d16-7e11473dde6a": {
      "id": "31ecb01d-44db-459d-8d16-7e11473dde6a",
      "message": {
        "id": "31ecb01d-44db-459d-8d16-7e11473dde6a",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1754375325.910211,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "\"Few-shot\"과 \"Zero-shot\"은 **AI, 특히 자연어 처리(NLP) 모델이 새로운 작업을 어떻게 학습하고 수행하는지** 설명할 때 자주 사용되는 용어입니다. 둘 다 **사전학습(pretrained)** 된 모델이 어떻게 **새로운 문제에 대응하는지**에 대한 방식입니다.\n\n---\n\n## 🔹 Zero-shot Learning (제로샷 학습)\n\n> 📌 **정의:**  \n모델이 **한 번도 본 적 없는 작업이나 예제**에 대해 **사전 지식만으로 바로 추론**하는 방식입니다.\n\n### ✔️ 특징\n- **예제 없이** 문제 설명(prompt)만으로 정답을 유추.\n- 일반화 능력이 중요함.\n- 예: GPT에게 “스페인어로 ‘사랑해’는 뭐야?”라고 했을 때, 따로 학습되지 않았어도 “Te amo”라고 답할 수 있음.\n\n### ✔️ 예시\n```\nPrompt: 번역해줘: \"I love you\" → ?\nOutput: \"나는 너를 사랑해\"\n```\n\n---\n\n## 🔹 Few-shot Learning (퓨샷 학습)\n\n> 📌 **정의:**  \n모델이 **소수의 예제(few examples)**를 참고하여 새로운 작업을 수행하는 방식입니다.\n\n### ✔️ 특징\n- 학습 데이터는 없지만, **예제를 몇 개 제공하면 더 정확한 예측** 가능.\n- 인간의 학습 방식과 유사 (예제 몇 개 보고 따라하기).\n- **GPT 모델의 대표적 강점** 중 하나.\n\n### ✔️ 예시\n```\nPrompt:\n번역 예시:\n- I love you → 나는 너를 사랑해\n- Thank you → 고마워\n- Good night → ?\n\nOutput: \"잘 자\"\n```\n\n---\n\n## 🔸 비교 요약표\n\n| 항목          | Zero-shot                  | Few-shot                     |\n|---------------|----------------------------|------------------------------|\n| 예제 개수     | 없음                       | 몇 개 (보통 1~5개 정도)     |\n| 인간 유사성   | 낮음                       | 높음                         |\n| 정확도        | 낮을 수 있음               | 보통 더 높음                 |\n| 유연성        | 매우 높음                  | 중간                         |\n| 예시          | 단순 지시만 있음           | 지시 + 예시 포함            |\n\n---\n\n## 🔸 One-shot도 있어요!\n\n- **One-shot**: 예제 1개만 제공.\n- Few-shot과 거의 유사한 개념이지만, **엄밀히는 1개의 예제만** 포함됨.\n\n---\n\n## ✅ 정리 한 줄 요약\n\n- **Zero-shot**: \"이거 해줘\"만 말해도 알아서 해줌.  \n- **Few-shot**: \"이런 식으로 해줘 (예시 몇 개 줌)\" 하면 더 잘함.\n\n---\n\n필요하면 실제 GPT 프롬프트 사례도 만들어 보여드릴 수 있어요."
          ]
        },
        "status": "finished_successfully",
        "end_turn": true,
        "weight": 1.0,
        "metadata": {
          "finish_details": {
            "type": "stop",
            "stop_tokens": [
              200002
            ]
          },
          "is_complete": true,
          "citations": [],
          "content_references": [],
          "request_id": "96a43c798e683085-ICN",
          "message_type": "next",
          "model_slug": "gpt-4o",
          "default_model_slug": "gpt-4o",
          "parent_id": "a3a42398-5993-4b0e-8249-145625f42fb4",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "a3a42398-5993-4b0e-8249-145625f42fb4",
      "children": [
        "87686d82-eed9-4305-93b0-7c132ca1534d"
      ]
    },
    "87686d82-eed9-4305-93b0-7c132ca1534d": {
      "id": "87686d82-eed9-4305-93b0-7c132ca1534d",
      "message": {
        "id": "87686d82-eed9-4305-93b0-7c132ca1534d",
        "author": {
          "role": "user",
          "name": null,
          "metadata": {}
        },
        "create_time": 1754375431.146,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "Chain-of-Thought에 대해설명해주"
          ]
        },
        "status": "finished_successfully",
        "end_turn": null,
        "weight": 1.0,
        "metadata": {
          "selected_sources": [],
          "selected_github_repos": [],
          "serialization_metadata": {
            "custom_symbol_offsets": []
          },
          "request_id": "96a43f0bba363085-ICN",
          "message_source": null,
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "31ecb01d-44db-459d-8d16-7e11473dde6a",
      "children": [
        "c9cbb2ff-e8b7-4bbe-81c8-c63c1c01d7dd"
      ]
    },
    "c9cbb2ff-e8b7-4bbe-81c8-c63c1c01d7dd": {
      "id": "c9cbb2ff-e8b7-4bbe-81c8-c63c1c01d7dd",
      "message": {
        "id": "c9cbb2ff-e8b7-4bbe-81c8-c63c1c01d7dd",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1754375431.477144,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "물론입니다!  \n**Chain-of-Thought (CoT)**는 AI 모델이 문제를 **단계적으로 추론하며 답을 도출**하도록 유도하는 기법입니다. 특히 수학 문제나 논리적 사고가 필요한 경우에 큰 효과를 발휘합니다.\n\n---\n\n## 🔹 Chain-of-Thought (CoT)의 정의\n\n> **Chain-of-Thought**란, **답을 바로 요구하지 않고**,  \n> **중간 사고 과정(생각의 흐름)을 명시적으로 유도**하는 방식입니다.  \n> 쉽게 말해, **“생각하는 과정을 말해줘”**라고 모델에 요청하는 것입니다.\n\n---\n\n## 🔸 예시 1: 일반 프롬프트 (Zero-shot)\n\n```\nQ: 마트에서 사과 3개가 6000원입니다. 사과 1개의 가격은 얼마인가요?\nA: 2000원\n```\n\n- 답은 맞지만, **과정이 생략됨**.\n- 복잡한 문제에서는 오류 확률이 높아짐.\n\n---\n\n## 🔸 예시 2: Chain-of-Thought 방식\n\n```\nQ: 마트에서 사과 3개가 6000원입니다. 사과 1개의 가격은 얼마인가요?\n\nA: 먼저, 사과 3개의 가격이 6000원이므로, 1개의 가격은  \n6000원을 3으로 나누면 됩니다.  \n6000 ÷ 3 = 2000  \n따라서 정답은 2000원입니다.\n```\n\n- **생각의 흐름**을 명확히 적음.\n- 모델이 **더 정확하고 일관된 답변**을 할 수 있음.\n\n---\n\n## 🔸 CoT의 핵심 효과\n\n| 효과 | 설명 |\n|------|------|\n| 🧠 추론 능력 향상 | 수학, 논리, 조건 판단 문제에서 더 나은 결과 |\n| 🔎 오류 감소 | 중간 과정이 있어 검토·교정이 쉬움 |\n| 🪜 단계별 학습 | 복잡한 문제를 분해해 쉽게 해결 가능 |\n\n---\n\n## 🔸 CoT의 활용 조건\n\n- 단순한 질문보다는 **복잡하거나 논리적인 문제**일 때 유용함.\n- **수학 문제**, **상황 판단**, **조건 추론**, **법률 적용** 등에서 강력함.\n\n---\n\n## 🔸 CoT + Few-shot = 💥 시너지\n\nChain-of-Thought 프롬프트를 만들 때,  \n**Few-shot 학습과 함께 사용하면 성능이 극대화**됩니다.\n\n```\nQ: 제과점에 빵이 5개 있고, 친구가 2개 더 가져왔습니다. 총 몇 개인가요?\nA: 먼저 빵이 5개 있었고, 친구가 2개를 가져왔으므로  \n총 빵의 개수는 5 + 2 = 7개입니다.\n\nQ: 책상 위에 연필이 10자루 있고, 3자루를 사용했습니다. 남은 연필 수는?\nA: 먼저 연필이 10자루 있었고, 3자루를 사용했으므로  \n남은 연필 수는 10 - 3 = 7자루입니다.\n```\n\n이런 식의 **Chain-of-Thought 예제 몇 개**를 미리 보여주면,  \n모델이 **새로운 문제도 같은 흐름으로 해결**할 수 있게 됩니다.\n\n---\n\n## ✅ 요약\n\n| 구분 | 설명 |\n|------|------|\n| 📌 개념 | 문제 해결의 **사고 과정을 문장으로 유도**하는 방식 |\n| 🧠 목적 | 모델이 **추론 능력을 더 잘 발휘**하도록 돕기 |\n| ✅ 장점 | 정확도 향상, 복잡한 문제 해결 가능, 오류 확인 용이 |\n| 💡 활용 | 수학, 논리, 조건 판단, 긴 추론 문제 등에 효과적 |\n\n---\n\n원하시면 직접 CoT 프롬프트를 만들어드릴 수 있어요!  \n어떤 주제에 해볼까요?"
          ]
        },
        "status": "finished_successfully",
        "end_turn": true,
        "weight": 1.0,
        "metadata": {
          "citations": [],
          "content_references": [],
          "request_id": "96a43f0bba363085-ICN",
          "message_type": "next",
          "model_slug": "gpt-4o",
          "default_model_slug": "gpt-4o",
          "parent_id": "87686d82-eed9-4305-93b0-7c132ca1534d",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "87686d82-eed9-4305-93b0-7c132ca1534d",
      "children": [
        "3e471ba3-f8f4-4516-ba32-5e675a36eb4e"
      ]
    },
    "3e471ba3-f8f4-4516-ba32-5e675a36eb4e": {
      "id": "3e471ba3-f8f4-4516-ba32-5e675a36eb4e",
      "message": {
        "id": "3e471ba3-f8f4-4516-ba32-5e675a36eb4e",
        "author": {
          "role": "user",
          "name": null,
          "metadata": {}
        },
        "create_time": 1754375529.674,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "만들어줘"
          ]
        },
        "status": "finished_successfully",
        "end_turn": null,
        "weight": 1.0,
        "metadata": {
          "selected_sources": [],
          "selected_github_repos": [],
          "serialization_metadata": {
            "custom_symbol_offsets": []
          },
          "request_id": "96a441738dc73085-ICN",
          "message_source": null,
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "c9cbb2ff-e8b7-4bbe-81c8-c63c1c01d7dd",
      "children": [
        "b546c705-e2a7-4a96-8b1e-496da7396f95"
      ]
    },
    "b546c705-e2a7-4a96-8b1e-496da7396f95": {
      "id": "b546c705-e2a7-4a96-8b1e-496da7396f95",
      "message": {
        "id": "b546c705-e2a7-4a96-8b1e-496da7396f95",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1754375529.77715,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "좋습니다!  \n아래에 **Chain-of-Thought 프롬프트 예시**를 세 가지 주제로 나눠서 보여드릴게요.\n\n---\n\n## 🧮 1. **수학 문제 예시 (초등 수학 수준)**\n\n**Q:** 철수는 하루에 연필을 2자루씩 씁니다. 연필이 10자루 있다면 며칠 동안 쓸 수 있을까요?  \n**A (Chain-of-Thought):**  \n먼저 연필이 총 10자루 있고, 철수는 하루에 2자루씩 씁니다.  \n그러면 몇 일 동안 쓸 수 있는지를 알아보기 위해 10을 2로 나눕니다.  \n10 ÷ 2 = 5  \n따라서 철수는 연필을 5일 동안 쓸 수 있습니다.  \n👉 정답: **5일**\n\n---\n\n## 📦 2. **논리 문제 예시**\n\n**Q:** A, B, C 중 한 명이 거짓말쟁이고, 나머지 둘은 진실을 말합니다.  \nA: \"나는 거짓말쟁이가 아니다.\"  \nB: \"C는 거짓말쟁이야.\"  \nC: \"A는 진실을 말하고 있어.\"  \n누가 거짓말쟁이일까요?\n\n**A (Chain-of-Thought):**  \n우선 A가 \"나는 거짓말쟁이가 아니다\"라고 했습니다.  \n만약 A가 거짓말쟁이라면, 자신이 거짓말쟁이가 아니라고 말했으니 **그 말이 거짓**, 즉 **A는 거짓말쟁이**가 맞습니다.  \n이 경우 B는 \"C는 거짓말쟁이야\"라고 말했는데, C가 진실을 말하고 있다면, B는 거짓말입니다.  \nC는 \"A는 진실을 말하고 있어\"라고 말했는데, A는 거짓말쟁이니까 C의 말도 거짓입니다.  \n즉, A는 거짓말쟁이이고, B와 C는 진실을 말합니다.  \n👉 정답: **A가 거짓말쟁이**\n\n---\n\n## 📈 3. **경제/투자 문제 예시**\n\n**Q:** 한 주식이 1년 전에 100,000원이었고 지금은 120,000원입니다. 연간 수익률은 얼마일까요?\n\n**A (Chain-of-Thought):**  \n연간 수익률은 현재 가격과 과거 가격을 비교해서 계산합니다.  \n현재 가격은 120,000원, 과거 가격은 100,000원이므로  \n수익 = 120,000 - 100,000 = 20,000원  \n수익률 = 수익 ÷ 원금 × 100 = 20,000 ÷ 100,000 × 100 = 20%  \n👉 정답: **20%**\n\n---\n\n필요하신 분야(예: 영어, 과학, 금융, 법률 등)에 맞춰 추가 제작해드릴 수 있어요.  \n원하시면 특정 주제를 알려주세요!"
          ]
        },
        "status": "finished_successfully",
        "end_turn": true,
        "weight": 1.0,
        "metadata": {
          "finish_details": {
            "type": "stop",
            "stop_tokens": [
              200002
            ]
          },
          "is_complete": true,
          "citations": [],
          "content_references": [],
          "request_id": "96a441738dc73085-ICN",
          "message_type": "next",
          "model_slug": "gpt-4o",
          "default_model_slug": "gpt-4o",
          "parent_id": "3e471ba3-f8f4-4516-ba32-5e675a36eb4e",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "3e471ba3-f8f4-4516-ba32-5e675a36eb4e",
      "children": [
        "c5a30fc2-5387-4caf-a10d-0ea011dd1a79"
      ]
    },
    "c5a30fc2-5387-4caf-a10d-0ea011dd1a79": {
      "id": "c5a30fc2-5387-4caf-a10d-0ea011dd1a79",
      "message": {
        "id": "c5a30fc2-5387-4caf-a10d-0ea011dd1a79",
        "author": {
          "role": "user",
          "name": null,
          "metadata": {}
        },
        "create_time": 1754375600.496,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "영어, 과학, 금융, 법률에 맞춰 추가 제작해"
          ]
        },
        "status": "finished_successfully",
        "end_turn": null,
        "weight": 1.0,
        "metadata": {
          "selected_sources": [],
          "selected_github_repos": [],
          "serialization_metadata": {
            "custom_symbol_offsets": []
          },
          "request_id": "96a4432e3ebc3085-ICN",
          "message_source": null,
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "b546c705-e2a7-4a96-8b1e-496da7396f95",
      "children": [
        "bfd12489-8282-4236-bb5e-f47e326dcd23"
      ]
    },
    "bfd12489-8282-4236-bb5e-f47e326dcd23": {
      "id": "bfd12489-8282-4236-bb5e-f47e326dcd23",
      "message": {
        "id": "bfd12489-8282-4236-bb5e-f47e326dcd23",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1754375600.89377,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "아래에 요청하신 네 가지 주제 — **영어**, **과학**, **금융**, **법률** — 각각에 대해  \n**Chain-of-Thought(사고의 흐름)** 형식의 프롬프트 예시를 만들어 드립니다.  \n각각 **질문 → Chain-of-Thought 풀이 → 최종 정답** 형식입니다.\n\n---\n\n## 🟦 1. 영어 (문법 및 어휘 판단 문제)\n\n**Q:** Which sentence is grammatically correct?  \nA. He don’t like pizza.  \nB. He doesn’t like pizza.  \nC. He didn’t likes pizza.  \n\n**A (Chain-of-Thought):**  \n먼저 주어 \"He\"는 **3인칭 단수**이므로 현재형 동사에 맞는 조동사나 동사형이 필요합니다.  \nA: \"don’t\"는 **1인칭/2인칭 복수에 사용**, 3인칭 단수에는 부적절 → ❌  \nB: \"doesn’t\"는 **3인칭 단수에 사용**, 동사 원형 \"like\"가 따라와서 맞음 → ✅  \nC: \"didn’t likes\"는 **과거 부정 조동사 \"didn't\" 뒤에 동사 원형**이 와야 함. \"likes\"는 잘못된 형태 → ❌  \n👉 정답: **B. He doesn’t like pizza.**\n\n---\n\n## 🟩 2. 과학 (물리 - 중력)\n\n**Q:** 왜 달에서 물건이 지구보다 천천히 떨어질까요?\n\n**A (Chain-of-Thought):**  \n물체가 떨어지는 속도는 **중력 가속도**에 따라 결정됩니다.  \n지구의 중력 가속도는 약 **9.8 m/s²**, 달의 중력은 **지구의 약 1/6**입니다.  \n즉, 달에서는 **중력이 약하므로 물체를 끌어당기는 힘이 작고**,  \n그 결과 **물체가 더 천천히 떨어집니다.**  \n👉 정답: **달의 중력이 약하기 때문에**\n\n---\n\n## 🟨 3. 금융 (복리 계산)\n\n**Q:** 100만원을 연 5% 이자로 2년간 복리로 투자하면 얼마가 될까?\n\n**A (Chain-of-Thought):**  \n복리 계산 공식은:  \n▶️ 미래가치 = 원금 × (1 + 이자율)^기간  \n▶️ 여기서 원금 = 1,000,000원, 이자율 = 0.05, 기간 = 2년  \n→ 미래가치 = 1,000,000 × (1 + 0.05)^2  \n= 1,000,000 × (1.1025) = 1,102,500  \n👉 정답: **1,102,500원**\n\n---\n\n## 🟥 4. 법률 (상황 판단)\n\n**Q:** A가 B의 허락 없이 B의 자전거를 몰래 타고 갔다가 돌려줬습니다. 절도죄에 해당할까요?\n\n**A (Chain-of-Thought):**  \n절도죄는 **타인의 재물을 '불법영득의사'를 가지고 가져가는 것**이 핵심입니다.  \n여기서 A는 B의 자전거를 **허락 없이** 가져갔지만, **돌려줄 의도**였기 때문에  \n‘영구적으로 소유하려는 의사(영득의사)’가 없었다고 볼 수 있습니다.  \n→ 따라서 **절도죄 요건 중 하나인 ‘불법영득의사’가 부족합니다.**  \n👉 정답: **절도죄에 해당하지 않을 가능성이 큼**\n\n---\n\n## ✅ 요약표\n\n| 분야 | 질문 요지 | Chain-of-Thought 핵심 | 정답 |\n|------|-----------|------------------------|-------|\n| 영어 | 문법 선택 | 주어와 조동사 일치 판별 | B |\n| 과학 | 중력 비교 | 달의 중력이 더 작다 | 달의 중력이 약해서 |\n| 금융 | 복리 계산 | 복리 공식 적용 | 1,102,500원 |\n| 법률 | 절도 성립 여부 | 불법영득의사 유무 판단 | 절도 아님 |\n\n---\n\n원하시면 위 형식으로 **문제 생성 자동화 도구**나  \n**학생용 학습지 형태**로 확장도 도와드릴 수 있습니다.  \n필요한 주제나 레벨을 알려주세요!"
          ]
        },
        "status": "finished_successfully",
        "end_turn": true,
        "weight": 1.0,
        "metadata": {
          "finish_details": {
            "type": "stop",
            "stop_tokens": [
              200002
            ]
          },
          "is_complete": true,
          "citations": [],
          "content_references": [],
          "request_id": "96a4432e3ebc3085-ICN",
          "message_type": "next",
          "model_slug": "gpt-4o",
          "default_model_slug": "gpt-4o",
          "parent_id": "c5a30fc2-5387-4caf-a10d-0ea011dd1a79",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "c5a30fc2-5387-4caf-a10d-0ea011dd1a79",
      "children": []
    }
  },
  "moderation_results": [],
  "current_node": "bfd12489-8282-4236-bb5e-f47e326dcd23",
  "plugin_ids": null,
  "conversation_id": "6891a485-3fec-8331-964d-f6bafb8733d3",
  "conversation_template_id": null,
  "gizmo_id": null,
  "gizmo_type": null,
  "is_archived": true,
  "is_starred": null,
  "safe_urls": [],
  "blocked_urls": [],
  "default_model_slug": "gpt-4o",
  "conversation_origin": null,
  "is_read_only": null,
  "voice": null,
  "async_status": null,
  "disabled_tool_ids": [],
  "is_do_not_remember": false,
  "memory_scope": "global_enabled",
  "context_scopes": null,
  "sugar_item_id": null,
  "sugar_item_visible": false,
  "pinned_time": null,
  "is_study_mode": false,
  "owner": null,
  "id": "6891a485-3fec-8331-964d-f6bafb8733d3"
}
```
