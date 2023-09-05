import sys
import os
import json

data = {
    "took": 1,
    "timed_out": "false",
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 22,
            "relation": "eq"
        },
        "max_score": 0.0,
        "hits": [
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "88",
                "_score": 0.0,
                "_source": {
                    "skuName": "莓小兔香野(11粒)200g",
                    "pinyin": "mxtxy(11l)200g",
                    "unitName": "公斤",
                    "priceFee": 0,
                    "partyCode": "1101200",
                    "skuId": 88
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "94",
                "_score": 0.0,
                "_source": {
                    "skuName": "莓小兔香野(15粒)200g",
                    "pinyin": "mxtxy(15l)200g",
                    "unitName": "公斤",
                    "priceFee": 0,
                    "partyCode": "1102002",
                    "skuId": 94
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "277",
                "_score": 0.0,
                "_source": {
                    "skuName": "膜壳先锋固话钢化膜收纳框",
                    "pinyin": "mqxfghghmsnk",
                    "unitName": "个",
                    "priceFee": 5000,
                    "partyCode": "6000001",
                    "skuId": 277
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "331",
                "_score": 0.0,
                "_source": {
                    "skuName": "1kg塑料黑筐(小）",
                    "pinyin": "1kgslhk(x）",
                    "unitName": "个",
                    "priceFee": 5500,
                    "partyCode": "2010405",
                    "skuId": 331
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "57",
                "_score": 0.0,
                "_source": {
                    "skuName": "招牌-三个零杭白菜200g",
                    "pinyin": "zp-sglhbc200g",
                    "unitName": "包",
                    "priceFee": 5000,
                    "partyCode": "12010201",
                    "skuId": 57
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "58",
                "_score": 0.0,
                "_source": {
                    "skuName": "招牌-三个零杭白菜420g",
                    "pinyin": "zp-sglhbc420g",
                    "unitName": "包",
                    "priceFee": 7000,
                    "partyCode": "12010203",
                    "skuId": 58
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "167",
                "_score": 0.0,
                "_source": {
                    "skuName": "招牌-三个零杭白菜268g好长好长好长好长好长好长好长好长好长好长好长好长好长好长好长",
                    "pinyin": "zp-sglhbc268g",
                    "unitName": "包",
                    "priceFee": 5000,
                    "partyCode": "12010202",
                    "skuId": 167
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "534",
                "_score": 0.0,
                "_source": {
                    "skuName": "膜蔻 荣耀平板 V7Pro 高清平板钢化膜",
                    "pinyin": "mk rypb V7Pro gqpbghm",
                    "unitName": "个",
                    "priceFee": 0,
                    "partyCode": "2020",
                    "skuId": 534
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "500",
                "_score": 0.0,
                "_source": {
                    "skuName": "苹果13mini膜蔻电镀磨砂膜黑色",
                    "pinyin": "pg13minimkddmsmhs",
                    "unitName": "个",
                    "priceFee": 5500,
                    "partyCode": "1011",
                    "skuId": 500
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "458",
                "_score": 0.0,
                "_source": {
                    "skuName": "膜蔻 iPad迷你/2/3 高清平板钢化膜",
                    "pinyin": "mk iPadmn/2/3 gqpbghm",
                    "unitName": "个",
                    "priceFee": 2500,
                    "partyCode": "2200",
                    "skuId": 458
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "513",
                "_score": 0.0,
                "_source": {
                    "skuName": "苹果13mini全屏膜黑色",
                    "pinyin": "pg13miniqpmhs",
                    "unitName": "个",
                    "priceFee": 5500,
                    "partyCode": "1010",
                    "skuId": 513
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "386",
                "_score": 0.0,
                "_source": {
                    "skuName": "膜蔻 ipad5/6/air/air2/2017 高清平板钢化膜",
                    "pinyin": "mk ipad5/6/air/air2/2017 gqpbghm",
                    "unitName": "个",
                    "priceFee": 3500,
                    "partyCode": "2201",
                    "skuId": 386
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "248",
                "_score": 0.0,
                "_source": {
                    "skuName": "膜壳先锋固话钢化膜",
                    "pinyin": "mqxfghghm",
                    "unitName": "个",
                    "priceFee": 2500,
                    "partyCode": "8000001",
                    "skuId": 248
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "338",
                "_score": 0.0,
                "_source": {
                    "skuName": "A级-最美红颜草莓(公斤)",
                    "pinyin": "Aj-zmhycm(gj)",
                    "unitName": "公斤",
                    "priceFee": 2000,
                    "partyCode": "1010199",
                    "skuId": 338
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "335",
                "_score": 0.0,
                "_source": {
                    "skuName": "莓小兔香野(15粒)200g",
                    "pinyin": "mxtxy(15l)200g",
                    "unitName": "公斤",
                    "priceFee": 6000,
                    "partyCode": "1101201",
                    "skuId": 335
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "162",
                "_score": 0.0,
                "_source": {
                    "skuName": "1.4kg塑料筐(中)",
                    "pinyin": "1.4kgslk(z)",
                    "unitName": "个",
                    "priceFee": 1,
                    "partyCode": "2010402",
                    "skuId": 162
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "163",
                "_score": 0.0,
                "_source": {
                    "skuName": "1.2kg塑料黑筐(小)",
                    "pinyin": "1.2kgslhk(x)",
                    "unitName": "个",
                    "priceFee": 500,
                    "partyCode": "2010404",
                    "skuId": 163
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "619",
                "_score": 0.0,
                "_source": {
                    "skuName": "库存锁定测试商品",
                    "pinyin": "kcsdcssp",
                    "unitName": "公斤",
                    "priceFee": 0,
                    "partyCode": "1000009",
                    "skuId": 619
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "661",
                "_score": 0.0,
                "_source": {
                    "skuName": "柳乐测试商品",
                    "pinyin": "llcssp",
                    "unitName": "个",
                    "priceFee": 100,
                    "partyCode": "liulecs",
                    "skuId": 661
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "676",
                "_score": 0.0,
                "_source": {
                    "skuName": "莓小兔香野200g",
                    "pinyin": "mxtxy200g",
                    "unitName": "公斤",
                    "priceFee": 0,
                    "partyCode": "1102003",
                    "skuId": 676
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "687",
                "_score": 0.0,
                "_source": {
                    "skuName": "莓小兔香野200g",
                    "pinyin": "mxtxy200g",
                    "unitName": "公斤",
                    "priceFee": 0,
                    "partyCode": "1102003",
                    "skuId": 687
                }
            },
            {
                "_index": "sku_product",
                "_type": "_doc",
                "_id": "698",
                "_score": 0.0,
                "_source": {
                    "skuName": "莓小兔香野200g",
                    "pinyin": "mxtxy200g",
                    "unitName": "公斤",
                    "priceFee": 0,
                    "partyCode": "1102003",
                    "skuId": 698
                }
            }
        ]
    }
}
json_str = json.dumps(data)
obj = json.loads(json_str)
hits = obj["hits"]["hits"]
for item in hits:
    print("%d," % item["_source"]["skuId"])