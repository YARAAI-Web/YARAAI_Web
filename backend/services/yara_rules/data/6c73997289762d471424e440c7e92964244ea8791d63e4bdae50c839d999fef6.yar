rule auto_rule_20250726072255_5491 {
  strings:
    $o0 = "xFFFFFFEA" wide ascii nocase
    $o1 = "byte_404185" wide ascii nocase
    $o2 = "byte_40412A" wide ascii nocase
    $o3 = "byte_404128" wide ascii nocase
    $o4 = "dword_40410D" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726072258_1530 {
  strings:
    $o0 = "byte_4040B4" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726072302_6924 {
  condition:
    auto_rule_20250726072255_5491 or auto_rule_20250726072258_1530
}