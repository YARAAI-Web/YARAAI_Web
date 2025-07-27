rule auto_rule_20250726224146_7798 {
  strings:
    $o0 = "dword_45D54C" wide ascii nocase
  condition:
    all of them
}