rule auto_rule_20250726165531_7479 {
  strings:
    $o0 = "j_unknown_libname_55_69" wide ascii nocase
    $o1 = "dword_456000" wide ascii nocase
    $o2 = "IdentToInt" wide ascii nocase
    $o3 = "off_4576C8" wide ascii nocase
    $o4 = "j_unknown_libname_55_77" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726165534_4453 {
  strings:
    $o0 = "TList" wide ascii nocase
    $o1 = "j_unknown_libname_55_61" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726165538_7579 {
  condition:
    auto_rule_20250726165531_7479 or auto_rule_20250726165534_4453
}