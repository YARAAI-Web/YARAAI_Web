rule auto_rule_20250726180607_8460 {
  strings:
    $o0 = "dword_4D1518" wide ascii nocase
  condition:
    all of them
}