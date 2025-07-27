rule auto_rule_20250726153747_8700 {
  strings:
    $o0 = "dword_4643E0" wide ascii nocase
    $o1 = "dword_462000" wide ascii nocase
    $o2 = "dword_463A48" wide ascii nocase
    $o3 = "MbCh" wide ascii nocase
    $o4 = "_aullrem" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726153750_3122 {
  strings:
    $o0 = "dword_462024" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726153755_9440 {
  condition:
    auto_rule_20250726153747_8700 or auto_rule_20250726153750_3122
}