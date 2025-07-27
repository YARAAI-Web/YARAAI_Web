rule auto_rule_20250726232142_2893 {
  strings:
    $o0 = "dword_14009166C" wide ascii nocase
    $o1 = "dword_1400912B8" wide ascii nocase
    $o2 = "hrtere" wide ascii nocase
  condition:
    3 of ($o*)
}