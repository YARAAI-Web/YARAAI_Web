rule auto_rule_20250726062114_2927 {
  strings:
    $o0 = "hWinPosInfo" wide ascii nocase
    $o1 = "uCode" wide ascii nocase
    $o2 = "presbits" wide ascii nocase
    $o3 = "CharPrevA" wide ascii nocase
    $o4 = "EnumDisplayDevicesA" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726062117_8317 {
  strings:
    $o0 = "GetClassInfoExA" wide ascii nocase
    $o1 = "lpszFormatName" wide ascii nocase
    $o2 = "DestroyCaret" wide ascii nocase
    $o3 = "EnumWindowStationsW" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726062121_1424 {
  condition:
    auto_rule_20250726062114_2927 or auto_rule_20250726062117_8317
}