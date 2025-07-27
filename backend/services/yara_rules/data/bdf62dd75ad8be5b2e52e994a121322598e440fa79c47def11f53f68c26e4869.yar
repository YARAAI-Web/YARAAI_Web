rule auto_rule_20250726201216_5950 {
  strings:
    $o0 = "BBCh" wide ascii nocase
    $o1 = "dword_4296F8" wide ascii nocase
    $o2 = "dword_4294A8" wide ascii nocase
    $o3 = "dword_42968C" wide ascii nocase
    $o4 = "x87ABA9E" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726201219_9616 {
  strings:
    $o0 = "dword_429494" wide ascii nocase
    $o1 = "x5C9D" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726201223_2144 {
  condition:
    auto_rule_20250726201216_5950 or auto_rule_20250726201219_9616
}