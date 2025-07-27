rule auto_rule_20250727022231_2133 {
  strings:
    $o0 = "dword_790020" wide ascii nocase
  condition:
    all of them
}