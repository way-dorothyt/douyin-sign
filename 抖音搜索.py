import json
import hashlib
import requests
from urllib.parse import quote

import 抖音签名

url = 'https://search3-search-lf.amemv.com/aweme/v2/search/general/stream/?klink_egdi=AALTrm0WUDpf5ZmknMiAyoCNzAtxgRvXAtv4Ccw1FV0dcqjVNf3P4moG&iid=3651929102896713&device_id=388592219267168&ac=wifi&channel=xiaomi_1128_64&aid=1128&app_name=aweme&version_code=370800&version_name=37.8.0&device_platform=android&os=android&ssmix=a&device_type=22041216C&device_brand=Redmi&language=zh&os_api=33&os_version=13&manifest_version_code=370801&resolution=1080*2316&dpi=440&update_version_code=37809900&_rticket=1771405130960&package=com.ss.android.ugc.aweme&mcc_mnc=46011&first_launch_timestamp=1771048722&last_deeplink_update_version_code=0&cpu_support64=true&host_abi=arm64-v8a&is_guest_mode=0&app_type=normal&minor_status=0&appTheme=light&is_preinstall=0&need_personal_recommend=1&is_android_pad=0&is_android_fold=0&ts=1771405130&cdid=fa273453-be88-48a1-9f39-69261d24f283&oaid=e91518b8fc0d2429'

data = 'filter_selected=%7B%22sort_type%22%3A%220%22%2C%22publish_time%22%3A%220%22%2C%22filter_duration%22%3A%22%22%7D&template_extra_info=%7B%22need_channel_list%22%3A%5B%22morphling_minor_v2%22%2C%22morphling_edu_minor%22%2C%22morphling_life_normal_v1%22%2C%22morphling_life_normal_v2%22%2C%22morphling_life_normal_v3%22%2C%22morphling_ecom_content%22%5D%2C%22env%22%3A%22prod%22%2C%22ppe%22%3A%22prod%22%7D&enter_from=homepage_hot&is_mute_status=0&client_history_need_store=1&is_accessibility=0&query_correct_type=1&video_cover_shrink=&dynamic_tab_combine=1&feed_tab_from=homepage_hot&is_coin=0&large_font_mode=0&keyword=%E8%8B%B9%E6%9E%9C17&enable_ai_head_tab=0&start_session=1&user_avatar_shrink_double=&is_ai_search_bar=1&effect_sdk_version=20.8.1&is_adapt_elder=0&hit_search_layout_switch_toast_condition=0&search_scene=douyin_search&count=10&from_author_id=94106437106&double_column_mode_scene=&search_layout_toast_shown=1&search_album_style=0&enable_history=1&search_source=search_history&video_cover_shrink_double=&hot_search=0&exit_guide_id_list=%5B%5D&simplify_mix_card_data=1&goods_info_version=1&address_book_access=2&disable_general_performance_opt_from_client=1&force_use_ai=0&location_permission=0&disable_server_forecast=0&cursor=0&nearby_extra_data=%7B%22nearby_tab_name%22%3A%22%E5%90%8C%E5%9F%8E%22%2C%22groupon_tab_name%22%3A%22%E5%9B%A2%E8%B4%AD%22%2C%22has_groupon_tab%22%3Atrue%2C%22groupon_tab_index%22%3A6%7D&vlm_config=1&mall_source_type=1&double_column_mode=0&is_after_locate=false&is_filter_search=0&is_pull_refresh=0&double_switch_to_single_times=0&inner_abstract_ai_bot=0&location_access=2&general_search_layout_type=2&search_session_round=1&enter_page_type=middle_page&history_search_query_list=%5B%5D&no_trace_search_switch=off&nice_search_type=general&music_format_type=1&client_height=895&user_layout_type_setting=0&loadmore_rerank=2&goods_info_count=10&double_column_experience_optimize=2&user_avatar_shrink=&lynx_ssr_props=%7B%22devicePlatform%22%3A%22android%22%2C%22screenWidth%22%3A393%2C%22screenHeight%22%3A842%2C%22fontScale%22%3A1%7D&previous_layout_type=null&previous_input_keyword=&avoid_user_chapter=0&client_width=393&token=search&disable_double_column=0&disable_hotspot_new_card=0&is_quality_style=1&is_double_column_left=0&dy_tab_adjust=homepage_hot&device_score=9.5763&prefetch_id=388592219267168_1771405130953_7606338613&client_prefetch_type=press&bcm_chain=%7B%22chain%22%3A%5B%7B%22btm%22%3A%22a1128.b6573.c0.d0%22%2C%22btm_show_id%22%3A%22bc0d350a-2872-4852-9c32-10a8a60ce991%231%22%7D%2C%7B%22btm%22%3A%22a1128.b0438.c0.d0%22%2C%22btm_show_id%22%3A%22412423e2-0bde-48cb-bd72-c8fe93f8bf6c%231%22%7D%2C%7B%22btm%22%3A%22a1.b1923.c0.d0%22%2C%22btm_show_id%22%3A%2228a0f400-e9cb-4ccb-97e1-69aa9f2cc082%232%22%7D%2C%7B%22btm%22%3A%22a1128.b0438.c0.d0%22%2C%22btm_show_id%22%3A%222e9d89c6-7ebf-4b71-85ec-1c4a91370797%231%22%7D%5D%7D&from_group_id=7607525652736627121&client_engine_extra=%7B%7D&anchor_item_id=&afterfeed_item_id=7607525652736627121&pre_search_id_list=%5B%5D&enter_from_second=&need_filter_settings=1&realtime_feature_channel=%7B%7D&extra=%7B%22search_log_extra%22%3A%22%7B%5C%22caption_level%5C%22%3A%5C%22%5C%22%7D%22%2C%22recommend_word_id%22%3A%22%22%2C%22hotlist_param%22%3A%22%7B%7D%22%2C%22previous_page%22%3A%22search_section%22%2C%22recommend_word_session_id%22%3A%22%22%7D&search_rerank_info=%7B%22poi_send_back%22%3A%7B%22user_device_feature%22%3A%7B%22brightness%22%3A0.11372549%2C%22is_mute%22%3A0%2C%22headphones%22%3A0%2C%22dark_mode%22%3A0%2C%22is_charging%22%3A1%2C%22network_status%22%3A%22WiFi%22%2C%22is_low_power_mode%22%3A0%2C%22volume%22%3A0.46666667%7D%2C%22user_status_prefer_feature%22%3A%7B%22ohr%22%3A%220%22%2C%22har%22%3A%220%22%7D%2C%22life_service_user_history_actions%22%3A%5B%5D%7D%7D&client_extra=%7B%22charging%22%3Atrue%2C%22qoe%22%3A100%2C%22har_info%22%3A%7B%7D%7D&afterfeed_video_id=v1e00fgi0000d69loa7og65hvq6an690_bytevc1_720p_751708&search_session_id=d881a6bf-c960-46ef-8443-28d7d0795d7d&afterfeed_play_progress=4&client_server_extra=%7B%22widget_extra%22%3A%22%7B%5C%22installed_widget_list%5C%22%3A%5B%5D%2C%5C%22check_ug_libra_can_show%5C%22%3Atrue%2C%5C%22series_id%5C%22%3A0%2C%5C%22series_type%5C%22%3A0%2C%5C%22total_episode%5C%22%3A0%7D%22%2C%22ugc_extra_info%22%3A%22%7B%5C%22channel%5C%22%3A%5C%22xiaomi_1128_64%5C%22%2C%5C%22version_name%5C%22%3A%5C%2237.8.0%5C%22%2C%5C%22host_abi%5C%22%3A%5C%22arm64-v8a%5C%22%2C%5C%22effect_sdk_version%5C%22%3A%5C%2220.8.1%5C%22%2C%5C%22feature_bits%5C%22%3A%5C%22%5B%5C%5C%5C%224294967295%5C%5C%5C%22%2C%5C%5C%5C%224290772991%5C%5C%5C%22%2C%5C%5C%5C%224294967295%5C%5C%5C%22%2C%5C%5C%5C%22245759%5C%5C%5C%22%5D%5C%22%7D%22%7D&life_client_extra=eNqLrlYyMTBQslJQio5RSjQ0NLLQSzIwMbaIUdJRAAnoJRlaGhnHKMUq1cYCAOh9CqA%3D'

# 这里可替换搜索关键字
data = data.replace(quote("苹果17"), quote("大疆无人机"))

md5 = hashlib.md5()
md5.update(data.encode('utf-8'))
stub = md5.hexdigest().upper()

param_json = {
    # 抖音版本 可以是其他的版本 但是必须和 url 中保持一致
    "version" : "37.8.0",
    # 抖音设备
    "device_id" : "388592219267168",
    # 环境 Code 根据不同的请求填写
    "env_code" : "0400000000000000",
    # 请求Url
    "url" : url,
    # headers 中 x-common-params-v2 参数 (没有可留空)
    "x_common_params_v2" : "",
    # headers 中 x-ss-stub 参数 (没有可留空)
    "x_ss_stub" : stub,
    # mssdk 请求中返回的 token (不清楚可留空 留空可能会触发风控)
    "mssdk_token" : "AuTiVA5PC1WvgdBLQ1HM9ECON",
    # x-bd-client-key (登录之后需要填写的参数 登录时返回 没有登录可留空)
    "x_bd_client_key" : "",
    # 测试密钥 key 飞机联系 @loveyuanfang 先测试再购买
    "key": "XXXXXXXXXXXXXXXXXXX",
    # 此选项固定 基于抖音 3780 版本开发 后续可迭代
    "base": "3780"
}

sign_json = json.loads(抖音签名.call_seven_shen(json.dumps(param_json)))

print(sign_json)

if sign_json["x-medusa"] == "":

    raise Exception("x-medusa is null")

cookies = {
    'passport_csrf_token': '3c37aa68db2169d272bd434cfbadddb6',
    'passport_csrf_token_default': '3c37aa68db2169d272bd434cfbadddb6',
    'store-region': 'cn-gs',
    'store-region-src': 'did',
    'install_id': '3651929102896713',
    'ttreq': '1$691464507436aac42405ce03293da6525c09f9b6',
    'odin_tt': 'e2292c350391bc3f31a5186e56672eeeef5baba2fbd56b5b51b6e7d1d9b6b45b150491eca14ae7e01ca691d1b9e860a4e9d8666bac5be773c6649debf4d820fd3683dedbdcd36ace260e99c1d7fa3944',
}

headers = {
    'Host': 'search3-search-lf.amemv.com',
    'x-tt-dt': 'AAA5VXPYR3OOCI2RYY262UNMWDT5JCK52DJQOU7YQ6FZYA3X5PQV33GQIIE3U26A7ZOGNONPILKQ2TS3H22XXK2NM73USM4UNDOOZLPI55BHHXYAFTOPUZUOIHOD3YTRZPJRJMF36PHQ2A3QR4LHCDY',
    'activity_now_client': '1771405132365',
    'compressed-bcm-chain': 'H4sIAAAAAAAAAH2R3WrDMAyF38W9rYItO7aVVxkjWLK9BtZ0P+nGKHn3uSsM1tLdSBc6+tA5OinZpWlWw8NJ8bJXg0rGYOyYgo+d6C5rtVVymJcyL2o4rev2Suj7YH+FbTK+7w6f45SbgkVn2+sEGAOCiz0CiUUwOsXktRQiszHqBqmdjXeQzqBDWxA059KQwsC5wSXWQrZGrl6ukB0bwnsnYky6Oq2hUEM5aYVCMeApJaoooiNu8E8E6iU9lXPP5Xn6KG9f43GeXo/lAlTrbUT/+MFCOZJ4CIUrOA4GYl8EjLhExgYdKJz9PLZF2Y8/z7pshpSRa7VQrffgfE2QQssks7XcsxXtslq/AQAdQtPgAQAA',
    'x-ss-req-ticket': '1771405130962',
    'x-vc-bdturing-sdk-version': '4.1.1.cn',
    'sdk-version': '2',
    'passport-sdk-settings': 'device_transfer_s_0,device_transfer_ab_0',
    'passport-sdk-version': '601511',
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'x-ss-stub': stub,
    # 'x-bd-content-encoding': 'zstd',
    'x-tt-store-region': 'cn-gs',
    'x-tt-store-region-src': 'did',
    'x-tt-request-tag': 's=-1;p=0',
    'x-ss-dp': '1128',
    'x-tt-trace-id': '01-6ff93e710d1616c2d3120605eae50468-6ff93e710d1616c2-00',
    'user-agent': 'com.ss.android.ugc.aweme/370801 (Linux; U; Android 13; zh_CN; 22041216C; Build/TP1A.220624.014; Cronet/TTNetVersion:6f1e308d 2025-12-08 QuicVersion:21ac1950 2025-11-18)',
    'ttzip-version': 'search_api',
    'ttzip-tlb': '1',
    'accept-encoding': 'gzip',
    # 'x-perseus': '7R777v/yTQxOt/ni6bOpECbEzjuY3gXf9FVuZkpX5Xx9zW3ycBXq3mB4IrEOZ25n4QSLL+qEhojjv19bmP9Kt/Zf3aopR2cqQXaJVxFvyMxwUF2nM3s8dK1aeWtywy6suGxrQbmuJz1E8p8ZgBBWNJH8kLwcP8SzpXxdxuKDTelnfrcxOC8uIJ9ku1K1BHNiheVW+9brCWchgAVevFBkB2ZkkI0drRRDW7y80s0TZwODsZ7X+ZdJhYcslWILs4CutbtuwScszCefAc9uPdnKyfhDpoFNlCmrAm5lIbdZIhbuDfI6ewKEPhc9iC+JUUBUOta2iBEheDU2OQQ1ZbY0EseJl9w6XiKBJoO2SGX/IkfdmwDDMV41iehzUH/DVTS6ZYAl9iSAW2p/X9ECRAzdcUe5pjlcFjYX++7tDdCefghTUqylpnAR01l9DXv/zEzbKaBbn3VvyUS99Yu18UHYYrfek20Z9T6e3mSIC4OJJ/LGRj+94Xa6ceD7jOlVNfMgfrQTermt8/ucmG7QXL3PJua9Jw/gpAyNbCBwtmoTdld+u9tL702MzeNfEcQkBPA7Yh6SWX1lgwHTUVpakcLbZrBpt5beDzJM5VGPqSCwsGxH9O9VS4uS6pIPkAzdht8ooBqRnPQcRG9HZECdfuIj1ilPuG+D4Oj/kZDHVZqY639z4SWPf0Dl3x8eFQx4j1BB05saTyd+LVtuQW9QoYt3SMtNBMG8dMlejoEk3V0Krv2K03EPIulkIQB5diUULcpcV5is1crSuzftopgWp6CcFCCt2u7AZhdvvgauCtMw9m5cMlCz3I0FZE0YmhxQfz1gd0uC6VPnGnUpyv27qxCmx+m25essezXhsgPaZGr40hK2ja6n07ICOGEF9ktCJ0Iz08pcoO3dPhELbb8wTDVrxVcB+R==',
    # 'x-medusa': 'TX+VaSHlvkMI5Dr4y7WXA4hJMZeOAgANWhupo9VysGd+CUsXELUU+BcHAX4ZmPthI4KnomZUv4xt1unYelrDkjQIBtu0OGLCuVDrMzOxiKyvhhe438E3qxJbZolB9ej3LneiznabM7kTdIwZYyXuIz//zmK1/ncpRylFj58+GSenoMK2BtUgn9T9utwXYy6bnGV/KiwxfOiWVrd3sv4f2R11aKTIGpVJqXz25f8QHf4v76CdzGIII8W4kG+jGfJ9dDNmcHAtvEwlZ3fP29SZUUbxs7IiLso9xp1izFZzwYFOgTk/Pk+iouoqw8a/LD7oDECV+qpscHz4KQOAU2fCRif1ojpAIf/4jx//+I8b7gk=',
    # 'x-argus': 'Sn+VaQ==',
    # 'x-helios': 'w9ScdmmK8T6CuuaIe0DmODk0jvvdEdweRm73YQxqE5af44ji',
    # 'x-ladon': 'TbcdSw==',
    # 'x-khronos': '1771405130',
    # 'x-gorgon': '840440d00400c932566b90644b01078889b142a9b8412bb26985',
    'x-perseus': sign_json['x-perseus'],
    'x-medusa': sign_json['x-medusa'],
    'x-argus': sign_json['x-argus'],
    'x-helios': sign_json['x-helios'],
    'x-ladon': sign_json['x-ladon'],
    'x-khronos': str(sign_json['x-khronos']),
    'x-gorgon': sign_json['x-gorgon'],
}

response = requests.post(
    url,
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False
)

print(response.text)