rule auto_rule_20250726134205_2525 {
  strings:
    $o0 = "copy_start" wide ascii nocase
    $o1 = "dword_450670" wide ascii nocase
    $o2 = "byte_4512C0" wide ascii nocase
    $o3 = "dword_45115C" wide ascii nocase
    $o4 = "UnwindUp6_0" wide ascii nocase
  condition:
    4 of ($o*)
}