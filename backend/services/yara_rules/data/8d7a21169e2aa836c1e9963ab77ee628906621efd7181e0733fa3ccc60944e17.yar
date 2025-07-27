rule auto_rule_20250726163744_6979 {
  strings:
    $o0 = "dword_4479C8" wide ascii nocase
  condition:
    all of them
}