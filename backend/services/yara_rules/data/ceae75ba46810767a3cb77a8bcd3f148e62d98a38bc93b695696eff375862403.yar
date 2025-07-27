rule auto_rule_20250726083440_6684 {
  strings:
    $o0 = "dword_64030168" wide ascii nocase
  condition:
    all of them
}