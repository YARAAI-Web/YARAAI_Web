rule auto_rule_20250726191035_8572 {
  strings:
    $o0 = "aInconsistentIo" wide ascii nocase
    $o1 = "dword_463E80" wide ascii nocase
    $o2 = "dword_4643E0" wide ascii nocase
  condition:
    3 of ($o*)
}