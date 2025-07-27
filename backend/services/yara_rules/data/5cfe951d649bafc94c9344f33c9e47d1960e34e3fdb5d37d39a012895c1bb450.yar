rule auto_rule_20250726064104_4002 {
  strings:
    $o0 = "dword_46F4A8" wide ascii nocase
  condition:
    all of them
}