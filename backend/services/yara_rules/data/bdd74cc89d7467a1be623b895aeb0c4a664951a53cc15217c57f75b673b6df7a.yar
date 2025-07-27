rule auto_rule_20250726210505_7054 {
  strings:
    $o0 = "UnwindUp1_0" wide ascii nocase
    $o1 = "dword_45D57C" wide ascii nocase
    $o2 = "dword_45CFC0" wide ascii nocase
  condition:
    3 of ($o*)
}