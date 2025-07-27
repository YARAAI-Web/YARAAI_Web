rule auto_rule_20250727010749_8178 {
  strings:
    $o0 = "dword_411974" wide ascii nocase
    $o1 = "dword_41197C" wide ascii nocase
  condition:
    all of them
}