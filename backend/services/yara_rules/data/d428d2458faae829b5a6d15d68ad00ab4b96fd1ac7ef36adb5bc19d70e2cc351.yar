rule auto_rule_20250726110136_7726 {
  strings:
    $o0 = "hWinSta" wide ascii nocase
    $o1 = "GetClassNameA" wide ascii nocase
    $o2 = "GetAltTabInfoW" wide ascii nocase
    $o3 = "EnumWindowStationsW" wide ascii nocase
    $o4 = "paccel" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726110139_1020 {
  strings:
    $o0 = "IMPSetIMEA" wide ascii nocase
    $o1 = "CloseWindow" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726110142_0771 {
  condition:
    auto_rule_20250726110136_7726 or auto_rule_20250726110139_1020
}