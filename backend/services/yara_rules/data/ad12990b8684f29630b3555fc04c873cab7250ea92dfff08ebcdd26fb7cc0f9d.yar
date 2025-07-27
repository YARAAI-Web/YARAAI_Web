rule auto_rule_20250726101157_7391 {
  strings:
    $o0 = "String1b" wide ascii nocase
    $o1 = "dword_4C1310" wide ascii nocase
  condition:
    all of them
}