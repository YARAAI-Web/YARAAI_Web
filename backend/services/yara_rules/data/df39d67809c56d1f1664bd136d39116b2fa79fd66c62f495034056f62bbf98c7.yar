rule auto_rule_20250726144433_2830 {
  strings:
    $o0 = "nProgram" wide ascii nocase
    $o1 = "dword_45B14C" wide ascii nocase
    $o2 = "SetStdHandle" wide ascii nocase
    $o3 = "byte_45AFD8" wide ascii nocase
  condition:
    4 of ($o*)
}