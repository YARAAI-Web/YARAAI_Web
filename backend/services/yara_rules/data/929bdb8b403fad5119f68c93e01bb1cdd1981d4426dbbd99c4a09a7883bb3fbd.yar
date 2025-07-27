rule auto_rule_20250726101917_4634 {
  strings:
    $o0 = "gu_return" wide ascii nocase
    $o1 = "dword_464270" wide ascii nocase
  condition:
    all of them
}