rule auto_rule_20250726211412_9365 {
  strings:
    $o0 = "gu_return" wide ascii nocase
    $o1 = "dword_4280A8" wide ascii nocase
    $o2 = "dword_4275F0" wide ascii nocase
    $o3 = "copy_tail_loop" wide ascii nocase
  condition:
    4 of ($o*)
}