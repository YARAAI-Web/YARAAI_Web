rule auto_rule_20250726224157_9462 {
  strings:
    $o0 = "wsprintfA" wide ascii nocase
    $o1 = "dword_41D980" wide ascii nocase
  condition:
    all of them
}