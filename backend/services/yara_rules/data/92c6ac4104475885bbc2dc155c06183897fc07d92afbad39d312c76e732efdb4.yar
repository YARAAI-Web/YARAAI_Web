rule auto_rule_20250726113834_7734 {
  strings:
    $o0 = "x78A59207" wide ascii nocase
    $o1 = "x7A2633C1" wide ascii nocase
  condition:
    all of them
}