rule auto_rule_20250726211612_9750 {
  strings:
    $o0 = "_c_exit" wide ascii nocase
    $o1 = "UnwindUp6_0" wide ascii nocase
    $o2 = "ReturnValue" wide ascii nocase
    $o3 = "dword_460348" wide ascii nocase
  condition:
    4 of ($o*)
}