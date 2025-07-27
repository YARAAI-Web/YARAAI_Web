rule auto_rule_20250727005212_7860 {
  strings:
    $o0 = "main_loop_entrance_0" wide ascii nocase
    $o1 = "dword_4642CC" wide ascii nocase
    $o2 = "ReturnValue" wide ascii nocase
    $o3 = "Dumping" wide ascii nocase
  condition:
    4 of ($o*)
}