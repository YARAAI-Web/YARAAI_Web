rule auto_rule_20250727013947_1506 {
  strings:
    $o0 = "x402801" wide ascii nocase
    $o1 = "dword_45D8AC" wide ascii nocase
    $o2 = "UnwindUp6_0" wide ascii nocase
    $o3 = "dword_450018" wide ascii nocase
    $o4 = "main_loop_entrance_0" wide ascii nocase
  condition:
    4 of ($o*)
}