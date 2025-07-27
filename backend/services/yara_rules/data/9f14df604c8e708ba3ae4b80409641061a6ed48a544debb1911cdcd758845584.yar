rule auto_rule_20250726142656_8882 {
  strings:
    $o0 = "ppavi" wide ascii nocase
    $o1 = "lParam1" wide ascii nocase
  condition:
    all of them
}