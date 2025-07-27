rule auto_rule_20250726170733_4314 {
  strings:
    $o0 = "program" wide ascii nocase
    $o1 = "UnwindUp1_0" wide ascii nocase
    $o2 = "GetActiveWindow_0" wide ascii nocase
    $o3 = "dword_4674F4" wide ascii nocase
  condition:
    4 of ($o*)
}