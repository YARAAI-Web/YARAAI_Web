rule auto_rule_20250726073424_4569 {
  strings:
    $o0 = "dword_78130" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}