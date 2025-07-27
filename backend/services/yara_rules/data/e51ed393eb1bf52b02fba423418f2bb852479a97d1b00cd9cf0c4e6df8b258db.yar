rule auto_rule_20250726110521_5231 {
  strings:
    $o0 = "dword_4672EC" wide ascii nocase
    $o1 = "dword_468334" wide ascii nocase
    $o2 = "dword_4668E8" wide ascii nocase
  condition:
    3 of ($o*)
}