rule auto_rule_20250726082146_4708 {
  strings:
    $o0 = "dword_4012D8" wide ascii nocase
    $o1 = "retnw" wide ascii nocase
  condition:
    all of them
}