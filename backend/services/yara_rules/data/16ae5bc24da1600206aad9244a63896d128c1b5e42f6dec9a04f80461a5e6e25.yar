rule auto_rule_20250726222507_9011 {
  strings:
    $o0 = "x810A4888" wide ascii nocase
    $o1 = "xA166" wide ascii nocase
  condition:
    all of them
}