rule auto_rule_20250726114741_1800 {
  strings:
    $o0 = "dword_640303D8" wide ascii nocase
    $o1 = "x9249248u" wide ascii nocase
  condition:
    all of them
}