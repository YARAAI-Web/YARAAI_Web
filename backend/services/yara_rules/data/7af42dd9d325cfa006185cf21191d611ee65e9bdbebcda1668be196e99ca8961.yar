rule auto_rule_20250726130408_3463 {
  strings:
    $o0 = "x426860" wide ascii nocase
    $o1 = "finish_loop" wide ascii nocase
    $o2 = "dword_462F9C" wide ascii nocase
    $o3 = "strpbrk" wide ascii nocase
    $o4 = "x140u" wide ascii nocase
  condition:
    4 of ($o*)
}