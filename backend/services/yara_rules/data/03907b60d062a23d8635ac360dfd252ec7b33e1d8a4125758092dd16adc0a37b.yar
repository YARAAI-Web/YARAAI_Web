rule auto_rule_20250726220621_1481 {
  strings:
    $o0 = "x413485" wide ascii nocase
    $o1 = "safely" wide ascii nocase
  condition:
    all of them
}