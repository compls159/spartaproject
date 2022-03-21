from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mc11th

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mc11th

docs = [
    {
        "item_name": "행주",
        "item_place": "부엌",
        "timer": 30,
        "img": "https://thumbnail7.coupangcdn.com/thumbnails/remote/230x230ex/image/product/image/vendoritem/2019/04/15/4470475497/073290b5-325a-408c-b2b5-8eff7eef1e38.jpg"
    },
    {
        "item_name": "고무장갑",
        "item_place": "부엌",
        "item_timer": 90,
        "item_img": "https://thumbnail6.coupangcdn.com/thumbnails/remote/230x230ex/image/vendor_inventory/c860/5ee8cd182bb72b60d76aa5a4a498e3141d6bfca28de808a3e80ed29e2517.jpg"
    },
    {

        "item_name": "수세미",
        "item_place": "부엌",
        "item_timer": 14,
        "item_img": "https://thumbnail6.coupangcdn.com/thumbnails/remote/230x230ex/image/vendor_inventory/828d/4418a362eb1fc0deb4bfc880310ea86d170ebae96557103ed6b970121635.jpg"
    },
    {

        "item_name": "플라스틱 용기",
        "item_place": "부엌",
        "item_timer": 90,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/104645475260882-764f7281-ccdc-4f82-a879-c00d38878f6d.jpg"
    },
    {

        "item_name": "나무 도마",
        "item_place": "부엌",
        "item_timer": 730,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/513919329786943-a5bbfe75-9fd7-4472-b364-d1682a3e9f06.jpg"
    },
    {

        "item_name": "도마",
        "item_place": "부엌",
        "item_timer": 365,
        "item_img": "https://thumbnail8.coupangcdn.com/thumbnails/remote/230x230ex/image/product/image/vendoritem/2019/09/25/4562175348/8996b438-468b-4ce1-880f-5455f2b35cf8.jpg"
    },
    {

        "item_name": "코팅프라이팬",
        "item_place": "부엌",
        "item_timer": 730,
        "item_img": "https://thumbnail8.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/517625530368447-19024890-d0c1-40b0-919f-8f257d50f130.jpg"
    },
    {

        "item_name": "스텐프라이팬",
        "item_place": "부엌",
        "item_timer": 2555,
        "item_img": "https://thumbnail8.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/2016/04/01/18/5/8a694d26-d49a-456a-bfbc-e11dde44d080.jpg"
    },
    {

        "item_name": "전기 압력밥솥",
        "item_place": "부엌",
        "item_timer": 2190,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/vendor_inventory/1d27/1917347d34ba56accfa416298c7932d88c1473d7428a51ff04f81bd630cf.jpg"
    },
    {

        "item_name": "식칼",
        "item_place": "부엌",
        "item_timer": 1095,
        "item_img": "https://thumbnail8.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/1107566389896410-3310969c-c422-407d-b1c2-9bd79ed71e74.jpg"
    },
    {

        "item_name": "베개",
        "item_place": "침실",
        "item_timer": 365,
        "item_img": "https://thumbnail7.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/2021/04/05/16/3/0ad5586c-28de-4db1-b945-c7c603b89158.jpg"
    },
    {

        "item_name": "메이크업 브러쉬",
        "item_place": "침실",
        "item_timer": 730,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/rs_quotation_api/dwkjpvby/8cc9e1fa154b4c45b1a575731be765ad.jpg"
    },
    {

        "item_name": "팬티",
        "item_place": "침실",
        "item_timer": 365,
        "item_img": "https://thumbnail7.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/2020/10/07/15/3/75306d4e-2952-400c-be67-ddaa165b7357.jpg"
    },
    {
        "item_name": "빗",
        "item_place": "침실",
        "item_timer": 180,
        "item_img": "https://thumbnail6.coupangcdn.com/thumbnails/remote/230x230ex/image/vendor_inventory/0b6b/cae781ac7ed6bc1c04208e84a7312594a495ca6facfeee7277fd5123b477.jpg"
    },
    {

        "item_name": "멀티탭",
        "item_place": "침실",
        "item_timer": 730,
        "item_img": "https://thumbnail7.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/520409240884547-d7caf43c-cfeb-47af-bf8c-865fd4ba90d3.jpg"
    },
    {

        "item_name": "커튼",
        "item_place": "침실",
        "item_timer": 90,
        "item_img": "https://thumbnail10.coupangcdn.com/thumbnails/remote/230x230ex/image/rs_quotation_api/xrtzercr/cfe1f4ae356745bba1d2a366f9a4c2b4.jpg"
    },
    {

        "item_name": "잠옷",
        "item_place": "침실",
        "item_timer": 7,
        "item_img": "https://thumbnail7.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/2022/01/14/14/4/34828616-e8b0-47da-9410-1f3ccc1f8df5.jpg"
    },
    {

        "item_name": "향수",
        "item_place": "침실",
        "item_timer": 730,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/product/image/vendoritem/2018/12/28/3509667270/34b26667-1f53-4a0e-a2fc-5884c5c437b0.jpg"
    },
    {

        "item_name": "이불",
        "item_place": "침실",
        "item_timer": 1825,
        "item_img": "https://thumbnail8.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/8970385456593661-181bbcaa-4e1a-43ea-9543-c1305a035044.jpg"
    },
    {

        "item_name": "해충약",
        "item_place": "침실",
        "item_timer": 90,
        "item_img": "https://thumbnail10.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/85458595926289-0e11f763-ccab-4e04-b129-b13d5ce10707.jpg"
    },
    {

        "item_name": "실내화",
        "item_place": "침실",
        "item_timer": 180,
        "item_img": "https://thumbnail10.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/14941685881816-ef404365-7306-43ed-8f3d-3f3941765915.jpg"
    },
    {

        "item_name": "담요",
        "item_place": "침실",
        "item_timer": 365,
        "item_img": "https://thumbnail7.coupangcdn.com/thumbnails/remote/230x230ex/image/rs_quotation_api/qynnguup/4be14e1fcb194eed998131f5b9be92ad.jpg"
    },
    {

        "item_name": "인공눈물",
        "item_place": "침실",
        "item_timer": 730,
        "item_img": "https://thumbnail10.coupangcdn.com/thumbnails/remote/230x230ex/image/vendor_inventory/3d58/ef1b6620d47dc77b71f16c1515317e0bbaabebf3db18a88ea201cc96850f.jpg"
    },
    {

        "item_name": "렌즈통",
        "item_place": "침실",
        "item_timer": 90,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/1930899795955770-626168f0-b9a0-4484-a4bf-fae8099ddde2.jpg"
    },
    {

        "item_name": "매트리스",
        "item_place": "침실",
        "item_timer": 2492,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/vendor_inventory/6c1e/659876ca9c9c40524e9b22f3a4c970a26cd9c47c0608dfb4e343ee3a9079.jpg"
    },
    {

        "item_name": "브래지어",
        "item_place": "침실",
        "item_timer": 365,
        "item_img": "https://thumbnail6.coupangcdn.com/thumbnails/remote/230x230ex/image/vendor_inventory/77af/0d096c43058ed72fc6c5d1cb1f578d0d5696429ecbdc03bd9cd58f32196f.jpg"
    },
    {

        "item_name": "향초",
        "item_place": "침실,화장실",
        "item_timer": 3,
        "item_img": "https://thumbnail10.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/6908447132559458-6d9cbf78-79d6-48f7-bcbb-16f38a0722ef.jpg"
    },
    {

        "item_name": "칫솔",
        "item_place": "화장실",
        "item_timer": 90,
        "item_img": "https://thumbnail8.coupangcdn.com/thumbnails/remote/230x230ex/image/product/image/vendoritem/2019/02/19/4402520940/9844ce7f-b97c-49e8-8860-33df94e1f69f.jpg"
    },
    {

        "item_name": "치약(개봉 후)",
        "item_place": "화장실",
        "item_timer": 180,
        "item_img": "https://thumbnail6.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/2020/08/18/10/2/3f1aa322-a2e1-40e0-9961-46167472545a.jpg"
    },
    {

        "item_name": "샤워타올",
        "item_place": "화장실",
        "item_timer": 90,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/vendor_inventory/8db2/33255f8bd7787b76ad1ea39d57956d60484815ea0fae0df9aeb804a4e68a.jpg"
    },
    {

        "item_name": "샤워볼",
        "item_place": "화장실",
        "item_timer": 30,
        "item_img": "https://thumbnail6.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/942212605568443-8ca6ccba-c41c-40df-b7b5-ebe68d89efd2.jpg"
    },
    {

        "item_name": "수건",
        "item_place": "화장실",
        "item_timer": 730,
        "item_img": "https://thumbnail10.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/75127176213018-0369195a-3d58-49d9-b11f-3d5aa22ce776.jpg"
    },
    {

        "item_name": "욕실 발 매트",
        "item_place": "화장실",
        "item_timer": 7,
        "item_img": "https://thumbnail8.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/343379527682382-db1e075c-a23f-4717-b78e-e2f4f283279c.jpg"
    },
    {

        "item_name": "변기 청소 솔",
        "item_place": "화장실",
        "item_timer": 180,
        "item_img": "https://thumbnail7.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/1197697955959371-00dca15f-1ca6-4a63-ae20-1dd949b735cc.jpg"
    },
    {

        "item_name": "텀블러",
        "item_place": "화장실",
        "item_timer": 60,
        "item_img": "https://thumbnail6.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/2020/09/22/22/7/eb182605-c529-4c44-be41-d936d2426c66.jpg"
    },
    {

        "item_name": "샤워기 헤드",
        "item_place": "화장실",
        "item_timer": 730,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/319101970425463-6c53da06-dee9-48c3-99da-81b24906352d.jpg"
    },
    {

        "item_name": "면도날",
        "item_place": "화장실",
        "item_timer": 14,
        "item_img": "https://thumbnail7.coupangcdn.com/thumbnails/remote/230x230ex/image/rs_quotation_api/8id8sjiq/9907901a8aa64960a067beb9fc067af1.jpg"
    },
    {

        "item_name": "샤워기 필터",
        "item_place": "화장실",
        "item_timer": 30,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/vendor_inventory/ae65/69ae28d52131096852da676e5e9ebff8995b0047afc917c91e7d815f0885.jpg"
    },
    {

        "item_name": "운동화",
        "item_place": "침실",
        "item_timer": 365,
        "item_img": "https://thumbnail9.coupangcdn.com/thumbnails/remote/230x230ex/image/rs_quotation_api/hiwibsjq/23620c4467f84eaeb36198a0cf1a690d.jpg"
    }
]

db.CYCL.insert_many(docs)
