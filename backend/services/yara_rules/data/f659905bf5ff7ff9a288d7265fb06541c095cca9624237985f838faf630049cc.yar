rule auto_rule_20250726225043_9498 {
  strings:
    $o0 = "xFFCD8D20" wide ascii nocase
    $o1 = "stru_42C008" wide ascii nocase
  condition:
    all of them
}