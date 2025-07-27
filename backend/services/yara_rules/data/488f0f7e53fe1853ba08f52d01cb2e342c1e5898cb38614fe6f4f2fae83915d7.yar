rule auto_rule_20250726132157_5707 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "dword_460270" wide ascii nocase
  condition:
    all of them
}