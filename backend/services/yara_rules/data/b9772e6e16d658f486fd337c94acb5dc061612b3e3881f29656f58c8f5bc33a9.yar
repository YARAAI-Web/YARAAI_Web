rule auto_rule_20250726104126_5121 {
  strings:
    $o0 = "hMailslot" wide ascii nocase
    $o1 = "penv" wide ascii nocase
    $o2 = "Toolhelp32ReadProcessMemory" wide ascii nocase
    $o3 = "hszItem" wide ascii nocase
    $o4 = "DrawFrame" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726104129_5231 {
  strings:
    $o0 = "GetMUILanguage" wide ascii nocase
    $o1 = "lpdwFlags" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726104134_7019 {
  condition:
    auto_rule_20250726104126_5121 or auto_rule_20250726104129_5231
}