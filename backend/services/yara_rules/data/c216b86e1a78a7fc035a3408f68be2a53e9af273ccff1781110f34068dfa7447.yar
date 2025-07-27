rule auto_rule_20250726072545_6624 {
  strings:
    $o0 = "dword_464298" wide ascii nocase
    $o1 = "located" wide ascii nocase
  condition:
    all of them
}