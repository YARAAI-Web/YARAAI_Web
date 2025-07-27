rule auto_rule_20250726204829_8830 {
  strings:
    $o0 = "start_0" wide ascii nocase
    $o1 = "dword_47EBB4" wide ascii nocase
  condition:
    all of them
}