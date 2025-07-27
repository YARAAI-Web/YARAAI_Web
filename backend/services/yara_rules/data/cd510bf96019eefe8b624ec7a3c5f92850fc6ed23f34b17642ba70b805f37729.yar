rule auto_rule_20250726100134_6636 {
  strings:
    $o0 = "dword_4305C2" wide ascii nocase
    $o1 = "x5572" wide ascii nocase
    $o2 = "dword_430646" wide ascii nocase
    $o3 = "x5A2E" wide ascii nocase
    $o4 = "dwCommittedSize" wide ascii nocase
  condition:
    4 of ($o*)
}