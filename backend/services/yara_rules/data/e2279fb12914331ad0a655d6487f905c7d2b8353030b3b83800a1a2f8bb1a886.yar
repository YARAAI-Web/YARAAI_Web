rule auto_rule_20250726215109_1084 {
  strings:
    $o0 = "dword_4657D8" wide ascii nocase
    $o1 = "_printMemBlockData" wide ascii nocase
    $o2 = "xC0000093" wide ascii nocase
    $o3 = "dword_4657C8" wide ascii nocase
    $o4 = "dword_464298" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726215110_2446 {
  strings:
    $o0 = "dword_4657C4" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726215116_4325 {
  condition:
    auto_rule_20250726215109_1084 or auto_rule_20250726215110_2446
}