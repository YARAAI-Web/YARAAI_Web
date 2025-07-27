rule auto_rule_20250726055850_1824 {
  strings:
    $o0 = "x4A96" wide ascii nocase
    $o1 = "x854" wide ascii nocase
  condition:
    all of them
}