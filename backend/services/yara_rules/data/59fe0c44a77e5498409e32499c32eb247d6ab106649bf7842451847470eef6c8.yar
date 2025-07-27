rule auto_rule_20250727025754_7426 {
  strings:
    $o0 = "dword_467ED0" wide ascii nocase
  condition:
    all of them
}