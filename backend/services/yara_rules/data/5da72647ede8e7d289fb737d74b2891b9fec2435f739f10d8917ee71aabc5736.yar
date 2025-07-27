rule auto_rule_20250726101823_0693 {
  strings:
    $o0 = "_abnormal_termination" wide ascii nocase
    $o1 = "byte_40CD28" wide ascii nocase
    $o2 = "dword_41197C" wide ascii nocase
  condition:
    3 of ($o*)
}