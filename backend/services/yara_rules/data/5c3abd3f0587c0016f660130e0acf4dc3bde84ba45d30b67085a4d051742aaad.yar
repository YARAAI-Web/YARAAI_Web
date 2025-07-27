rule auto_rule_20250726231648_3083 {
  strings:
    $o0 = "off_467744" wide ascii nocase
    $o1 = "Sourcea" wide ascii nocase
  condition:
    all of them
}