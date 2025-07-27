rule auto_rule_20250726074517_2506 {
  strings:
    $o0 = "byte_44BE9C" wide ascii nocase
    $o1 = "dword_44B550" wide ascii nocase
    $o2 = "TrailDown1_0" wide ascii nocase
    $o3 = "dword_418020" wide ascii nocase
    $o4 = "main_loop_entrance" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726074520_7135 {
  strings:
    $o0 = "__crtInitCritSecNoSpinCount" wide ascii nocase
    $o1 = "dword_44C110" wide ascii nocase
    $o2 = "strpbrk" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726074524_5881 {
  condition:
    auto_rule_20250726074517_2506 or auto_rule_20250726074520_7135
}