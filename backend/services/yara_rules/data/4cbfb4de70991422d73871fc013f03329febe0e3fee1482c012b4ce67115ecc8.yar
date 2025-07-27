rule auto_rule_20250726204543_7362 {
  strings:
    $o0 = "fst7" wide ascii nocase
    $o1 = "x4E5F71" wide ascii nocase
    $o2 = "x4DBBFA" wide ascii nocase
    $o3 = "x4E1CF7" wide ascii nocase
    $o4 = "x4DD105" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726204547_4844 {
  strings:
    $o0 = "x4E2D03" wide ascii nocase
    $o1 = "x800F" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726204551_1127 {
  condition:
    auto_rule_20250726204543_7362 or auto_rule_20250726204547_4844
}