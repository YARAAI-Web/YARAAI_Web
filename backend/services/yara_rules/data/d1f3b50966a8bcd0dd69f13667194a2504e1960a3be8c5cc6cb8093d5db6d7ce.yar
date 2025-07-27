rule auto_rule_20250727025247_1478 {
  strings:
    $o0 = "aGggstgggggcgcr" wide ascii nocase
    $o1 = "lpOverlapped" wide ascii nocase
    $o2 = "dword_41A208" wide ascii nocase
  condition:
    3 of ($o*)
}