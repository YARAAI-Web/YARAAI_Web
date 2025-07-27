rule auto_rule_20250727034638_8399 {
  strings:
    $o0 = "aGetlastactivep" wide ascii nocase
    $o1 = "InterlockedDecrement" wide ascii nocase
  condition:
    all of them
}