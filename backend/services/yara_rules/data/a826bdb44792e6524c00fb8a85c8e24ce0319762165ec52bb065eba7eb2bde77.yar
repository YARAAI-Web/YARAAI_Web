rule auto_rule_20250726170920_6165 {
  strings:
    $o0 = "lpfnEnum" wide ascii nocase
    $o1 = "x17000u" wide ascii nocase
    $o2 = "SetScrollRange" wide ascii nocase
    $o3 = "CloseWindow" wide ascii nocase
    $o4 = "CharLowerW" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726170922_3651 {
  strings:
    $o0 = "fShow" wide ascii nocase
    $o1 = "DdeDisconnectList" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726170925_1528 {
  condition:
    auto_rule_20250726170920_6165 or auto_rule_20250726170922_3651
}