rule auto_rule_20250726072457_4499 {
  strings:
    $o0 = "dword_4693F0" wide ascii nocase
  condition:
    all of them
}