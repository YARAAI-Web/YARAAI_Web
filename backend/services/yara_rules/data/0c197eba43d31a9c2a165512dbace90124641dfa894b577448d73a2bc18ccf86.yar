rule auto_rule_20250726155424_9732 {
  strings:
    $o0 = "dword_44C2A0" wide ascii nocase
    $o1 = "dword_44B658" wide ascii nocase
    $o2 = "lpCharType" wide ascii nocase
    $o3 = "find_end_of_dest_string_loop" wide ascii nocase
    $o4 = "UnwindUp0_0" wide ascii nocase
  condition:
    4 of ($o*)
}