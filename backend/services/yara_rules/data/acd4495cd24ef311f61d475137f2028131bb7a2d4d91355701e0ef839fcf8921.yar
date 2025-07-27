rule auto_rule_20250726164820_8570 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "gu_return" wide ascii nocase
    $o2 = "dword_45D544" wide ascii nocase
    $o3 = "UnwindUp3_0" wide ascii nocase
  condition:
    4 of ($o*)
}