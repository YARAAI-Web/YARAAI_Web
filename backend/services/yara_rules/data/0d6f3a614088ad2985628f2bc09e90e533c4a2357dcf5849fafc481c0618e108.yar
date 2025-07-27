rule auto_rule_20250727025525_6765 {
  strings:
    $o0 = "dword_476A98" wide ascii nocase
    $o1 = "atol" wide ascii nocase
  condition:
    all of them
}