rule auto_rule_20250727042503_2999 {
  strings:
    $o0 = "dword_6403034C" wide ascii nocase
  condition:
    all of them
}