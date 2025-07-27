rule auto_rule_20250726061834_7433 {
  strings:
    $o0 = "xFFFFFFFFFLL" wide ascii nocase
    $o1 = ".packed" wide ascii nocase
  condition:
    all of them
}