rule auto_rule_20250726092503_6566 {
  strings:
    $o0 = "strpbrk" wide ascii nocase
    $o1 = "dword_46ED7C" wide ascii nocase
    $o2 = "_ioinit" wide ascii nocase
  condition:
    3 of ($o*)
}