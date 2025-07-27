rule auto_rule_20250726223646_2278 {
  strings:
    $o0 = "dword_45CF48" wide ascii nocase
    $o1 = "_ioinit" wide ascii nocase
    $o2 = "_global_unwind2" wide ascii nocase
  condition:
    3 of ($o*)
}