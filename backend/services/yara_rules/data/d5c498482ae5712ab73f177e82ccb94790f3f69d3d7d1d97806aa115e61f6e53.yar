rule auto_rule_20250727000505_2923 {
  strings:
    $o0 = "byte_4C12A9" wide ascii nocase
  condition:
    all of them
}