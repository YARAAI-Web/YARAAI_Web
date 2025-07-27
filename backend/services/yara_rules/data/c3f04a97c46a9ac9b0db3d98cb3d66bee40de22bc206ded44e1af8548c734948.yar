rule auto_rule_20250726151847_9857 {
  strings:
    $o0 = "byte_409158" wide ascii nocase
    $o1 = "lpszText" wide ascii nocase
  condition:
    all of them
}