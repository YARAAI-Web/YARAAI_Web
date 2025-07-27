rule auto_rule_20250726174226_5952 {
  strings:
    $o0 = "UnwindUp0_0" wide ascii nocase
    $o1 = "dword_40E004" wide ascii nocase
    $o2 = "find_end_of_dest_string_loop" wide ascii nocase
    $o3 = "dword_4119A8" wide ascii nocase
    $o4 = "byte_40CD28" wide ascii nocase
  condition:
    4 of ($o*)
}