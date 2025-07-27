rule auto_rule_20250726093923_6843 {
  strings:
    $o0 = "UnwindUp3_0" wide ascii nocase
    $o1 = "dword_45CFCC" wide ascii nocase
    $o2 = "CodePagea" wide ascii nocase
    $o3 = "main_loop_entrance" wide ascii nocase
  condition:
    4 of ($o*)
}