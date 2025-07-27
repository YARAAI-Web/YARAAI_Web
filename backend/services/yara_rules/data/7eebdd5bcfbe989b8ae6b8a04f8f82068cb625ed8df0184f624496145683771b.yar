rule auto_rule_20250726065236_9774 {
  strings:
    $o0 = "dword_6402E060" wide ascii nocase
  condition:
    all of them
}