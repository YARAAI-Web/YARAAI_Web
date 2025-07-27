rule auto_rule_20250726092603_8196 {
  strings:
    $o0 = "dword_42E50D" wide ascii nocase
    $o1 = "x546Cu" wide ascii nocase
    $o2 = "x1359u" wide ascii nocase
    $o3 = "x66A3" wide ascii nocase
  condition:
    4 of ($o*)
}