rule auto_rule_20250726081227_7483 {
  strings:
    $o0 = "F58h" wide ascii nocase
    $o1 = "ServicesReturned" wide ascii nocase
  condition:
    all of them
}