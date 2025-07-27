rule auto_rule_20250726095916_6937 {
  strings:
    $o0 = "dword_467D2C" wide ascii nocase
    $o1 = "cause" wide ascii nocase
  condition:
    all of them
}