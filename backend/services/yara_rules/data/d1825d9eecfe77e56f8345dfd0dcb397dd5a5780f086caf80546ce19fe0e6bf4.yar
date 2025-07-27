rule auto_rule_20250726172823_5273 {
  strings:
    $o0 = "dword_449EA8" wide ascii nocase
    $o1 = "off_449A40" wide ascii nocase
    $o2 = "x4020D4" wide ascii nocase
    $o3 = "UnwindUp1_0" wide ascii nocase
    $o4 = "dword_449ED4" wide ascii nocase
  condition:
    4 of ($o*)
}