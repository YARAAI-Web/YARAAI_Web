rule auto_rule_20250726173501_0889 {
  strings:
    $o0 = "dodwords" wide ascii nocase
    $o1 = "dword_4766C4" wide ascii nocase
    $o2 = "dword_432008" wide ascii nocase
    $o3 = "dword_476980" wide ascii nocase
  condition:
    4 of ($o*)
}