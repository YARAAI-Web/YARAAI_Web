rule auto_rule_20250726103447_8444 {
  strings:
    $o0 = "_wincmdln" wide ascii nocase
    $o1 = "dword_4119B0" wide ascii nocase
    $o2 = "dword_41198C" wide ascii nocase
    $o3 = "main_loop_0" wide ascii nocase
  condition:
    4 of ($o*)
}