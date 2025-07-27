rule auto_rule_20250726234040_4648 {
  strings:
    $o0 = "dword_45CDB4" wide ascii nocase
    $o1 = "dword_45CD98" wide ascii nocase
    $o2 = "x426790" wide ascii nocase
    $o3 = "finish_loop" wide ascii nocase
  condition:
    4 of ($o*)
}