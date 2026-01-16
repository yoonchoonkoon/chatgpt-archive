# Negative Roll Yield Explained

- id: 67d62356-9a40-8007-a445-11541418a079
- date: 2025-03-16

```json
{
  "title": "Negative Roll Yield Explained",
  "create_time": 1742086998.802417,
  "update_time": 1742088907.713444,
  "mapping": {
    "client-created-root": {
      "id": "client-created-root",
      "message": null,
      "parent": null,
      "children": [
        "cbdb1ab1-5f72-40bc-8e81-d0fc8bf29ecb"
      ]
    },
    "cbdb1ab1-5f72-40bc-8e81-d0fc8bf29ecb": {
      "id": "cbdb1ab1-5f72-40bc-8e81-d0fc8bf29ecb",
      "message": {
        "id": "cbdb1ab1-5f72-40bc-8e81-d0fc8bf29ecb",
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
        "864bd546-4a02-4e64-834c-04cebdd41d8c"
      ]
    },
    "864bd546-4a02-4e64-834c-04cebdd41d8c": {
      "id": "864bd546-4a02-4e64-834c-04cebdd41d8c",
      "message": {
        "id": "864bd546-4a02-4e64-834c-04cebdd41d8c",
        "author": {
          "role": "user",
          "name": null,
          "metadata": {}
        },
        "create_time": 1742086998.265,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "Negative Roll Yield"
          ]
        },
        "status": "finished_successfully",
        "end_turn": null,
        "weight": 1.0,
        "metadata": {
          "serialization_metadata": {
            "custom_symbol_offsets": []
          },
          "dictation": false,
          "request_id": "92105479e991d1eb-ATL",
          "message_source": null,
          "timestamp_": "absolute",
          "message_type": null
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "cbdb1ab1-5f72-40bc-8e81-d0fc8bf29ecb",
      "children": [
        "ba077a67-4dfb-4205-bc10-ef61a68ca802"
      ]
    },
    "ba077a67-4dfb-4205-bc10-ef61a68ca802": {
      "id": "ba077a67-4dfb-4205-bc10-ef61a68ca802",
      "message": {
        "id": "ba077a67-4dfb-4205-bc10-ef61a68ca802",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1742087010.860097,
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
          "default_model_slug": "auto",
          "parent_id": "864bd546-4a02-4e64-834c-04cebdd41d8c",
          "request_id": "92105479e991d1eb-ATL",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "864bd546-4a02-4e64-834c-04cebdd41d8c",
      "children": [
        "3726aba3-4ee3-4dde-996a-4a394c6cfa62"
      ]
    },
    "3726aba3-4ee3-4dde-996a-4a394c6cfa62": {
      "id": "3726aba3-4ee3-4dde-996a-4a394c6cfa62",
      "message": {
        "id": "3726aba3-4ee3-4dde-996a-4a394c6cfa62",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1742086998.871237,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "### **Negative Roll Yield: Definition & Explanation**\nNegative roll yield occurs when a futures contract is rolled over at a lower price than the expiring contract, leading to a loss for the investor. It is commonly associated with **contango** markets, where futures prices are higher than spot prices. \n\n---\n\n### **How Negative Roll Yield Happens**\n1. **Futures Contract Expiry:** Investors in futures contracts must roll over (close and re-enter) positions before expiration.\n2. **Contango Market Structure:** If the futures curve is in contango (i.e., future prices are higher than spot prices), the new contract will be more expensive than the expiring contract.\n3. **Loss on Roll Over:** When the investor sells the expiring contract at a lower price and buys the new contract at a higher price, they incur a loss—this loss is the **negative roll yield**.\n\n---\n\n### **Example of Negative Roll Yield**\n- Suppose an investor holds an oil futures contract expiring this month at **$80** per barrel.\n- The next month’s futures contract is trading at **$82** (contango).\n- The investor sells the expiring contract at **$80** and buys the new one at **$82**.\n- **Loss per barrel = $2** → This is the negative roll yield.\n\n---\n\n### **Implications of Negative Roll Yield**\n- **Commodity ETFs:** Many commodity ETFs suffer from negative roll yield because they frequently roll over futures contracts.\n- **Hedgers & Speculators:** Long-term holders in contango markets face continuous losses if roll yield remains negative.\n- **Investment Strategies:** Traders adjust strategies to minimize roll yield losses, such as using different contract maturities or alternative hedging methods.\n\n---\n\n### **How to Mitigate Negative Roll Yield**\n- **Choose Backwardation Markets:** Negative roll yield occurs in contango, so investing in backwardation (where futures prices are lower than spot prices) can lead to positive roll yield.\n- **Optimize Roll Timing:** Some traders roll contracts earlier or later to minimize costs.\n- **Use Alternative Investments:** Instead of futures-based ETFs, investors may opt for direct commodity investments or companies in related industries.\n\nWould you like more details on specific strategies to mitigate negative roll yield? 🚀"
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
          "default_model_slug": "auto",
          "parent_id": "ba077a67-4dfb-4205-bc10-ef61a68ca802",
          "request_id": "92105479e991d1eb-ATL",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "ba077a67-4dfb-4205-bc10-ef61a68ca802",
      "children": [
        "b33d7c96-31ae-40d3-8907-42b2df14aeb7"
      ]
    },
    "b33d7c96-31ae-40d3-8907-42b2df14aeb7": {
      "id": "b33d7c96-31ae-40d3-8907-42b2df14aeb7",
      "message": {
        "id": "b33d7c96-31ae-40d3-8907-42b2df14aeb7",
        "author": {
          "role": "user",
          "name": null,
          "metadata": {}
        },
        "create_time": 1742087031.442,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "한글로 번역해줘"
          ]
        },
        "status": "finished_successfully",
        "end_turn": null,
        "weight": 1.0,
        "metadata": {
          "serialization_metadata": {
            "custom_symbol_offsets": []
          },
          "dictation": false,
          "request_id": "921055492c32d1eb-ATL",
          "message_source": null,
          "timestamp_": "absolute",
          "message_type": null
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "3726aba3-4ee3-4dde-996a-4a394c6cfa62",
      "children": [
        "d3d0bdfc-1251-42e0-b362-94716f4116d9"
      ]
    },
    "d3d0bdfc-1251-42e0-b362-94716f4116d9": {
      "id": "d3d0bdfc-1251-42e0-b362-94716f4116d9",
      "message": {
        "id": "d3d0bdfc-1251-42e0-b362-94716f4116d9",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1742087031.653137,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "### **네거티브 롤 수익(Negative Roll Yield)란?**  \n네거티브 롤 수익은 **만기된 선물 계약을 롤오버(갱신)할 때, 새로운 계약 가격이 기존 계약보다 높아 손실이 발생하는 상황**을 의미합니다. 주로 **콘탱고(Contango)** 시장에서 발생하며, 이때 선물 가격이 현물 가격보다 높습니다.  \n\n---\n\n### **네거티브 롤 수익이 발생하는 과정**\n1. **선물 계약 만기:** 투자자는 선물 계약 만기 전에 기존 포지션을 청산하고 새로운 계약을 매수해야 합니다.  \n2. **콘탱고 시장 구조:** 만약 시장이 콘탱고 상태라면, 새로운 선물 계약의 가격이 기존 계약보다 높습니다.  \n3. **롤오버 과정에서 발생하는 손실:** 기존 계약을 낮은 가격에 팔고, 새로운 계약을 더 높은 가격에 사게 되므로 손실(네거티브 롤 수익)이 발생합니다.  \n\n---\n\n### **네거티브 롤 수익 예시**\n- 투자자가 이번 달 만기되는 **유가 선물 계약을 80달러**에 보유하고 있다고 가정합니다.  \n- 다음 달 유가 선물 가격이 **82달러**라면, 새로운 계약을 더 비싼 가격에 사야 합니다.  \n- 기존 계약(80달러) 매도 → 새로운 계약(82달러) 매수  \n- **배럴당 2달러 손실 발생** → 이것이 **네거티브 롤 수익**입니다.  \n\n---\n\n### **네거티브 롤 수익의 영향**\n- **상품 ETF:** 원자재 ETF는 선물 계약을 자주 롤오버하기 때문에 네거티브 롤 수익의 영향을 크게 받습니다.  \n- **헤지거 및 투기자:** 콘탱고 시장에서 장기 보유자는 지속적인 롤오버 손실을 경험할 수 있습니다.  \n- **투자 전략:** 트레이더들은 롤 수익 손실을 최소화하기 위해 계약 만기를 조정하거나 대체 헤징 방법을 활용하기도 합니다.  \n\n---\n\n### **네거티브 롤 수익을 최소화하는 방법**\n✅ **백워데이션(Backwardation) 시장 선택:** 네거티브 롤 수익은 콘탱고 시장에서 발생하므로, 백워데이션 시장(선물 가격이 현물 가격보다 낮은 상태)에 투자하면 **긍정적인 롤 수익**을 얻을 수 있습니다.  \n✅ **롤오버 타이밍 최적화:** 일부 투자자들은 특정 시점에 롤오버를 조정하여 비용을 줄입니다.  \n✅ **대체 투자 활용:** 선물 기반 ETF 대신, 원자재 자체에 투자하거나 관련 산업 기업에 투자하는 방법도 고려할 수 있습니다.  \n\n네거티브 롤 수익을 줄이는 구체적인 투자 전략이 필요하신가요? 🚀"
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
          "default_model_slug": "auto",
          "parent_id": "b33d7c96-31ae-40d3-8907-42b2df14aeb7",
          "request_id": "921055492c32d1eb-ATL",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "b33d7c96-31ae-40d3-8907-42b2df14aeb7",
      "children": [
        "26c08878-8159-418d-b480-e04a32fe7dd5"
      ]
    },
    "26c08878-8159-418d-b480-e04a32fe7dd5": {
      "id": "26c08878-8159-418d-b480-e04a32fe7dd5",
      "message": {
        "id": "26c08878-8159-418d-b480-e04a32fe7dd5",
        "author": {
          "role": "user",
          "name": null,
          "metadata": {}
        },
        "create_time": 1742088880.67,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "Positive Roll Yield"
          ]
        },
        "status": "finished_successfully",
        "end_turn": null,
        "weight": 1.0,
        "metadata": {
          "serialization_metadata": {
            "custom_symbol_offsets": []
          },
          "dictation": false,
          "request_id": "9210826f8d00d1dd-ATL",
          "message_source": null,
          "timestamp_": "absolute",
          "message_type": null
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "d3d0bdfc-1251-42e0-b362-94716f4116d9",
      "children": [
        "3f01380d-8dfd-41eb-8021-a6a7b17c8c0e"
      ]
    },
    "3f01380d-8dfd-41eb-8021-a6a7b17c8c0e": {
      "id": "3f01380d-8dfd-41eb-8021-a6a7b17c8c0e",
      "message": {
        "id": "3f01380d-8dfd-41eb-8021-a6a7b17c8c0e",
        "author": {
          "role": "assistant",
          "name": null,
          "metadata": {}
        },
        "create_time": 1742088881.253901,
        "update_time": null,
        "content": {
          "content_type": "text",
          "parts": [
            "### **포지티브 롤 수익(Positive Roll Yield)란?**  \n포지티브 롤 수익(Positive Roll Yield)은 **만기된 선물 계약을 롤오버(갱신)할 때, 새로운 계약 가격이 기존 계약보다 낮아 이익이 발생하는 경우**를 의미합니다.  \n이것은 **백워데이션(Backwardation)** 시장에서 주로 발생하며, 이때 선물 가격이 현물 가격보다 낮습니다.  \n\n---\n\n### **포지티브 롤 수익이 발생하는 과정**\n1. **선물 계약 만기:** 투자자는 기존 선물 계약을 청산하고 새로운 계약을 매수해야 합니다.  \n2. **백워데이션 시장 구조:** 만약 시장이 백워데이션 상태라면, 새로운 선물 계약의 가격이 기존 계약보다 낮습니다.  \n3. **롤오버 과정에서 발생하는 이익:** 기존 계약을 높은 가격에 매도하고, 새로운 계약을 더 낮은 가격에 매수할 수 있어 이익(포지티브 롤 수익)이 발생합니다.  \n\n---\n\n### **포지티브 롤 수익 예시**\n- 투자자가 이번 달 만기되는 **유가 선물 계약을 80달러**에 보유하고 있다고 가정합니다.  \n- 다음 달 유가 선물 가격이 **78달러**라면, 새로운 계약을 더 저렴한 가격에 살 수 있습니다.  \n- 기존 계약(80달러) 매도 → 새로운 계약(78달러) 매수  \n- **배럴당 2달러 이익 발생** → 이것이 **포지티브 롤 수익**입니다.  \n\n---\n\n### **포지티브 롤 수익의 영향**\n- **상품 ETF:** 백워데이션 시장에서 선물 기반 ETF는 지속적으로 포지티브 롤 수익을 누릴 수 있습니다.  \n- **헤지거 및 투기자:** 롤오버 비용이 낮아지므로 장기 보유자에게 유리한 환경이 됩니다.  \n- **투자 전략:** 일부 트레이더는 포지티브 롤 수익이 예상되는 시장을 선택해 롤오버 전략을 최적화합니다.  \n\n---\n\n### **포지티브 롤 수익을 극대화하는 방법**\n✅ **백워데이션 시장 탐색:** 백워데이션 시장은 공급 부족, 높은 현물 수요 등으로 인해 발생할 수 있으므로, 이러한 시장을 찾아 투자하면 포지티브 롤 수익을 얻을 가능성이 높아집니다.  \n✅ **선물 만기 구조 최적화:** 단기 선물보다 장기 선물 계약을 선택하는 전략도 고려할 수 있습니다.  \n✅ **상품 ETF 활용:** 백워데이션 상태가 지속되는 원자재 ETF(예: 특정 에너지 또는 농산물 ETF)에 투자하면 롤오버 과정에서 수익을 기대할 수 있습니다.  \n\n포지티브 롤 수익을 활용한 구체적인 투자 전략이 궁금하신가요? 🚀"
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
          "default_model_slug": "auto",
          "parent_id": "26c08878-8159-418d-b480-e04a32fe7dd5",
          "request_id": "9210826f8d00d1dd-ATL",
          "timestamp_": "absolute"
        },
        "recipient": "all",
        "channel": null
      },
      "parent": "26c08878-8159-418d-b480-e04a32fe7dd5",
      "children": []
    }
  },
  "moderation_results": [],
  "current_node": "3f01380d-8dfd-41eb-8021-a6a7b17c8c0e",
  "plugin_ids": null,
  "conversation_id": "67d62356-9a40-8007-a445-11541418a079",
  "conversation_template_id": null,
  "gizmo_id": null,
  "gizmo_type": null,
  "is_archived": true,
  "is_starred": null,
  "safe_urls": [],
  "blocked_urls": [],
  "default_model_slug": "auto",
  "conversation_origin": null,
  "is_read_only": null,
  "voice": null,
  "async_status": null,
  "disabled_tool_ids": [],
  "is_do_not_remember": null,
  "memory_scope": "global_enabled",
  "context_scopes": null,
  "sugar_item_id": null,
  "sugar_item_visible": false,
  "pinned_time": null,
  "is_study_mode": false,
  "owner": null,
  "id": "67d62356-9a40-8007-a445-11541418a079"
}
```
