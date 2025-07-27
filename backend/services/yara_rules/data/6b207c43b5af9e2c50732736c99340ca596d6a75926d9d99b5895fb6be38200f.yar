rule auto_rule_20250726125852_6685 {
  strings:
    $o0 = "x7D0Fu" wide ascii nocase
    $o1 = "x5C37u" wide ascii nocase
  condition:
    all of them
}