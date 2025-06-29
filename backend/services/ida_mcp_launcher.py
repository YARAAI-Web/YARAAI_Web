import idaapi
import idc
import time
from extract_all_to_c import decompile_to_c

print("✅ MCP 플러그인 자동 활성화 시도")
try:
    for plugin in idaapi.plugins():
        if plugin.wanted_name == "MCP":
            plugin.run(None)
            print("✅ MCP 플러그인 실행됨")
            break
except Exception as e:
    print("❌ MCP 실행 실패:", e)

time.sleep(3)  # MCP 서버 준비 시간 확보

try:
    decompile_to_c()
    print("✅ extract_all_to_c 수행 완료")
except Exception as e:
    print("❌ extract_all_to_c 실행 실패:", e)

idc.qexit(0)
