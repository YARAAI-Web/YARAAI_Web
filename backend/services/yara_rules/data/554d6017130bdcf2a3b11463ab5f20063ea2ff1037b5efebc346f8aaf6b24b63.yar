rule auto_rule_20250726082654_2369 {
  strings:
    $o0 = "fsModifiers" wide ascii nocase
    $o1 = "dword_4C171C" wide ascii nocase
  condition:
    all of them
}