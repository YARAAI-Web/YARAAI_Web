rule auto_rule_20250726190518_5696 {
  strings:
    $o0 = "_ZeroTail" wide ascii nocase
    $o1 = "strpbrk" wide ascii nocase
    $o2 = "dword_4757C0" wide ascii nocase
  condition:
    3 of ($o*)
}