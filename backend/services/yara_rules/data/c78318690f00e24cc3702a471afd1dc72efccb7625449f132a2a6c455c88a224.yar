rule auto_rule_20250726114515_9477 {
  strings:
    $o0 = "_cropzeros" wide ascii nocase
    $o1 = "off_474A50" wide ascii nocase
  condition:
    all of them
}