rule auto_rule_20250727015745_3962 {
  strings:
    $o0 = "dword_441840" wide ascii nocase
    $o1 = "icebp" wide ascii nocase
  condition:
    all of them
}