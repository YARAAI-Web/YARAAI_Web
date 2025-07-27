rule auto_rule_20250727005347_0709 {
  strings:
    $o0 = "dword_449700" wide ascii nocase
  condition:
    all of them
}