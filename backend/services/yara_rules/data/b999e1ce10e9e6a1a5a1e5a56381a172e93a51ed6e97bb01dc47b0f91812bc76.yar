rule auto_rule_20250726162533_9507 {
  strings:
    $o0 = "dword_78118" wide ascii nocase
    $o1 = "dword_78280" wide ascii nocase
    $o2 = "dword_780F8" wide ascii nocase
    $o3 = "dword_1E6A8" wide ascii nocase
  condition:
    4 of ($o*)
}