# ADR EDR GDR 비교

- id: 682a7fed-d5ac-8007-b407-3f5e21ebe527
- date: 2025-05-19

```json
{
  "title": "ADR EDR GDR 비교",
  "create_time": 1747615726.071726,
  "update_time": 1747615734.246602,
  "mapping": {
    "bf3fcc8f-f1c0-4e65-b3d3-0f337abdfe85": {
      "id": "bf3fcc8f-f1c0-4e65-b3d3-0f337abdfe85",
      "message": null,
      "parent": null,
      "children": [
        "23945cc2-2834-484f-a560-bb2d92cb5f19"
      ]
    },
    "23945cc2-2834-484f-a560-bb2d92cb5f19": {
      "id": "23945cc2-2834-484f-a560-bb2d92cb5f19",
      "message": {
        "id": "23945cc2-2834-484f-a560-bb2d92cb5f19",
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
      "parent": "bf3fcc8f-f1c0-4e65-b3d3-0f337abdfe85",
      "children": [
        "bbb21b61-cbc7-40b0-8372-7e0c6dc65b1b"
      ]
    },
    "bbb21b61-cbc7-40b0-8372-7e0c6dc65b1b": {
      "id": "bbb21b61-cbc7-40b0-8372-7e0c6dc65b1b",
      "message": {
        "id": "bbb21b61-cbc7-40b0-8372-7e0c6dc65b1b",
        "author": {
          "role": "user",
          "name": null,
          "metadata": {}
        },
        "create_time": 1747615726.074053,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "ADR EDR GDR"
          ]
        },
        "status": "finished_successfully",
        "end_turn": null,
        "weight": 1.0,
        "metadata": {
          "content_references": [],
          "search_result_groups": [],
          "search_queries": [],
          "image_results": [],
          "real_time_audio_has_video": false,
          "dictation": false,
          "image_gen_async": false,
          "trigger_async_ux": false,
          "request_id": "941f972dcf04ea01-ICN",
          "message_source": null,
          "timestamp_": "absolute",
          "message_type": null
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "23945cc2-2834-484f-a560-bb2d92cb5f19",
      "children": [
        "ce9a18a1-f2a4-4032-a6f1-d6396f5b9f95"
      ]
    },
    "ce9a18a1-f2a4-4032-a6f1-d6396f5b9f95": {
      "id": "ce9a18a1-f2a4-4032-a6f1-d6396f5b9f95",
      "message": {
        "id": "ce9a18a1-f2a4-4032-a6f1-d6396f5b9f95",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1747615733.656083,
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
          "message_type": null,
          "model_slug": "gpt-4o",
          "default_model_slug": "gpt-4o",
          "parent_id": "bbb21b61-cbc7-40b0-8372-7e0c6dc65b1b",
          "request_id": "941f972dcf04ea01-ICN",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "bbb21b61-cbc7-40b0-8372-7e0c6dc65b1b",
      "children": [
        "b79b0b53-ac27-43c9-8788-38ad20bb33be"
      ]
    },
    "b79b0b53-ac27-43c9-8788-38ad20bb33be": {
      "id": "b79b0b53-ac27-43c9-8788-38ad20bb33be",
      "message": {
        "id": "b79b0b53-ac27-43c9-8788-38ad20bb33be",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1747615726.254996,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "ADR, EDR, GDR은 모두 **국제예탁증서 (Depositary Receipts, DR)**의 일종으로, 특정 국가 외의 투자자들이 해외 기업 주식에 투자할 수 있게 하는 증권입니다. 아래는 각각의 개념과 특징을 요약한 내용입니다:\n\n| 구분 | 명칭 | 발행지역 | 설명 |\n|------|------|---------|------|\n| **ADR** | American Depositary Receipt | **미국** | 미국 시장(NYSE, NASDAQ 등)에서 거래되도록 미국 예탁은행이 발행한 외국 기업 주식의 예탁증서. 미국 투자자가 해외 주식에 쉽게 투자 가능하게 함. |\n| **EDR** | European Depositary Receipt | **유럽** | 유럽의 증권시장(LSE, 프랑크푸르트 등)에서 거래되도록 유럽 내 은행이 발행한 예탁증서. 미국 이외의 유럽 투자자들이 외국 주식에 접근할 수 있게 함. |\n| **GDR** | Global Depositary Receipt | **국제시장 (주로 유럽/아시아)** | 여러 국가의 증권시장에 상장될 수 있도록 설계된 국제 예탁증서. 보통 런던, 룩셈부르크, 싱가포르, 홍콩 등에서 발행. 글로벌 자금 조달에 유리. |\n\n### 추가 비교\n\n| 항목 | ADR | EDR | GDR |\n|------|-----|-----|-----|\n| 주로 상장되는 시장 | 미국 | 유럽 | 유럽 및 아시아 등 |\n| 발행 통화 | USD | EUR 등 | 보통 USD, EUR |\n| 규제기관 | SEC (미국 증권거래위원회) | 해당 유럽 국가의 규제기관 | 발행국 및 상장국 규제 |\n| 투자자 대상 | 미국 투자자 | 유럽 투자자 | 글로벌 투자자 |\n\n필요하면 실제 상장사 예시나 투자 시 고려사항도 정리해드릴 수 있습니다."
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
          "message_type": null,
          "model_slug": "gpt-4o",
          "default_model_slug": "gpt-4o",
          "parent_id": "ce9a18a1-f2a4-4032-a6f1-d6396f5b9f95",
          "request_id": "941f972dcf04ea01-ICN",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "ce9a18a1-f2a4-4032-a6f1-d6396f5b9f95",
      "children": []
    }
  },
  "moderation_results": [],
  "current_node": "b79b0b53-ac27-43c9-8788-38ad20bb33be",
  "plugin_ids": null,
  "conversation_id": "682a7fed-d5ac-8007-b407-3f5e21ebe527",
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
  "id": "682a7fed-d5ac-8007-b407-3f5e21ebe527"
}
```
