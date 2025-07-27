rule auto_rule_20250726191213_2747 {
  strings:
    $o0 = "dword_467EC0" wide ascii nocase
    $o1 = "UnwindUp4_0" wide ascii nocase
    $o2 = "dword_468018" wide ascii nocase
    $o3 = "normal" wide ascii nocase
  condition:
    4 of ($o*)
}