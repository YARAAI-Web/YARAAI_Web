rule auto_rule_20250726114911_2868 {
  strings:
    $o0 = "byte_4C18B4" wide ascii nocase
    $o1 = "dword_4C132C" wide ascii nocase
    $o2 = "WinDetectHiddenText" wide ascii nocase
    $o3 = "RegisterHotKey" wide ascii nocase
    $o4 = "byte_4C10C3" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726114914_6846 {
  strings:
    $o0 = "word_4C145C" wide ascii nocase
    $o1 = "dword_4C115C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726114918_8797 {
  condition:
    auto_rule_20250726114911_2868 or auto_rule_20250726114914_6846
}