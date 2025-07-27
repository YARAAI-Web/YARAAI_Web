rule auto_rule_20250726111435_3524 {
  strings:
    $o0 = "before" wide ascii nocase
    $o1 = "byte_4655A0" wide ascii nocase
  condition:
    all of them
}