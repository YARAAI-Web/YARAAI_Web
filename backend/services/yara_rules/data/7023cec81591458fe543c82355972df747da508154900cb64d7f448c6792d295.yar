rule auto_rule_20250726134029_4560 {
  strings:
    $o0 = "dword_476920" wide ascii nocase
    $o1 = "dword_41B008" wide ascii nocase
    $o2 = "strcspn" wide ascii nocase
  condition:
    3 of ($o*)
}