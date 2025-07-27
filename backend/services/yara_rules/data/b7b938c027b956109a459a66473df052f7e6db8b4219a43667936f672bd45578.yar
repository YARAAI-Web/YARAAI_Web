rule auto_rule_20250726091819_4106 {
  strings:
    $o0 = "dwInfoType" wide ascii nocase
    $o1 = "_heap_init" wide ascii nocase
    $o2 = "dword_4605E8" wide ascii nocase
  condition:
    3 of ($o*)
}