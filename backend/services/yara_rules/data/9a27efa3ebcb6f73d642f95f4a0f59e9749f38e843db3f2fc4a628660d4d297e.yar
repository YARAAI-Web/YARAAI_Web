rule auto_rule_20250726164305_0152 {
  strings:
    $o0 = "dword_45DEF0" wide ascii nocase
    $o1 = "UnwindUp6_0" wide ascii nocase
    $o2 = "dword_45DEFC" wide ascii nocase
  condition:
    3 of ($o*)
}