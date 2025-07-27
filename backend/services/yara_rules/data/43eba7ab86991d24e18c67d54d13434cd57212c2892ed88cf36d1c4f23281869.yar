rule auto_rule_20250726160136_6484 {
  strings:
    $o0 = "UnwindUp2_0" wide ascii nocase
    $o1 = "dword_40F018" wide ascii nocase
    $o2 = "dword_468068" wide ascii nocase
  condition:
    3 of ($o*)
}