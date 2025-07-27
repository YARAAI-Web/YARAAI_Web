rule auto_rule_20250726170435_3669 {
  strings:
    $o0 = "dword_45522C" wide ascii nocase
    $o1 = "dword_455720" wide ascii nocase
    $o2 = "tail_loop_start" wide ascii nocase
    $o3 = "dword_454658" wide ascii nocase
  condition:
    4 of ($o*)
}