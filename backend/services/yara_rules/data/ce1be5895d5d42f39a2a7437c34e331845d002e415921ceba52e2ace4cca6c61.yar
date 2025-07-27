rule auto_rule_20250726215018_5434 {
  strings:
    $o0 = "dword_45D3F8" wide ascii nocase
    $o1 = "__crtMessageBoxA" wide ascii nocase
    $o2 = "dword_45D8A4" wide ascii nocase
    $o3 = "dword_45D548" wide ascii nocase
    $o4 = "GetStringTypeW" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726215021_5793 {
  strings:
    $o0 = "dword_45001C" wide ascii nocase
    $o1 = "waveInClose" wide ascii nocase
    $o2 = "strcat" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726215025_3335 {
  condition:
    auto_rule_20250726215018_5434 or auto_rule_20250726215021_5793
}