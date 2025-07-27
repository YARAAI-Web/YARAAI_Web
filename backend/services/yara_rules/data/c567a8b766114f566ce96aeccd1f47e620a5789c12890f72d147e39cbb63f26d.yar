rule auto_rule_20250726152353_5285 {
  strings:
    $o0 = "dword_45525C" wide ascii nocase
    $o1 = "__crtInitCritSecAndSpinCount" wide ascii nocase
    $o2 = "dword_455240" wide ascii nocase
    $o3 = "dword_4555F0" wide ascii nocase
  condition:
    4 of ($o*)
}