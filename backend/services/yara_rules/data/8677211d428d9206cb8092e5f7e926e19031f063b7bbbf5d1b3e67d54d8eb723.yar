rule auto_rule_20250726191141_4663 {
  strings:
    $o0 = "dword_409634" wide ascii nocase
    $o1 = "dword_40112C" wide ascii nocase
  condition:
    all of them
}