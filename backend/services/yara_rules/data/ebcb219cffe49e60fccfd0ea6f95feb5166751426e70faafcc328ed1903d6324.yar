rule auto_rule_20250726150926_0480 {
  strings:
    $o0 = "qword_1809D5358" wide ascii nocase
    $o1 = "qword_1809D5820" wide ascii nocase
    $o2 = "qword_1809D53C8" wide ascii nocase
    $o3 = "qword_1809D4BF0" wide ascii nocase
  condition:
    4 of ($o*)
}