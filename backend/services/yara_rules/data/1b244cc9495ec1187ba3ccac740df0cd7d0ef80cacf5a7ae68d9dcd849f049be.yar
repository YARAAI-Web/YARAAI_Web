rule auto_rule_20250726111710_4888 {
  strings:
    $o0 = "dword_463AE0" wide ascii nocase
    $o1 = "MbCh" wide ascii nocase
    $o2 = "UnwindUp1_0" wide ascii nocase
  condition:
    3 of ($o*)
}