rule auto_rule_20250727041758_7942 {
  strings:
    $o0 = "dword_427E74" wide ascii nocase
    $o1 = "aGggstgggggcgcr" wide ascii nocase
    $o2 = "dword_427E7C" wide ascii nocase
  condition:
    3 of ($o*)
}