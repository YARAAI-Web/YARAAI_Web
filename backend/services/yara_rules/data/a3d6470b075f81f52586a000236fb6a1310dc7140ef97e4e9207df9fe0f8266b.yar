rule auto_rule_20250726125902_6213 {
  strings:
    $o0 = "dword_6402E568" wide ascii nocase
  condition:
    all of them
}