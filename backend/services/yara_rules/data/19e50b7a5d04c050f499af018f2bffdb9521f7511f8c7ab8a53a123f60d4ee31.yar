rule auto_rule_20250726105559_7372 {
  strings:
    $o0 = "dword_41D96C" wide ascii nocase
    $o1 = "lpNumberOfBytesWritten" wide ascii nocase
    $o2 = "dword_4047F8" wide ascii nocase
  condition:
    3 of ($o*)
}