rule auto_rule_20250726174614_8067 {
  strings:
    $o0 = "off_46ADD0" wide ascii nocase
    $o1 = "dword_46C1A0" wide ascii nocase
    $o2 = "UnwindUp1_0" wide ascii nocase
  condition:
    3 of ($o*)
}