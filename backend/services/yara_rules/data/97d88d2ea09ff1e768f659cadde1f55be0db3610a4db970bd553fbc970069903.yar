rule auto_rule_20250726183136_7448 {
  strings:
    $o0 = "CodePagea" wide ascii nocase
    $o1 = "lRequest" wide ascii nocase
  condition:
    all of them
}