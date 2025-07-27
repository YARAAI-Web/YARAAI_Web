rule auto_rule_20250726202831_4049 {
  strings:
    $o0 = "x8A36" wide ascii nocase
    $o1 = "x55D1u" wide ascii nocase
  condition:
    all of them
}