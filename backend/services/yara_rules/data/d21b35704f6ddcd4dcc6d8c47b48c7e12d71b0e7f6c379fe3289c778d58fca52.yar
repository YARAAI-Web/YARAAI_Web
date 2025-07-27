rule auto_rule_20250726222828_1436 {
  strings:
    $o0 = "SHGetValueW" wide ascii nocase
    $o1 = "x170002u" wide ascii nocase
  condition:
    all of them
}