rule auto_rule_20250726202922_6204 {
  strings:
    $o0 = "dword_460F14" wide ascii nocase
    $o1 = "TrailDown1" wide ascii nocase
    $o2 = "dword_460D48" wide ascii nocase
  condition:
    3 of ($o*)
}