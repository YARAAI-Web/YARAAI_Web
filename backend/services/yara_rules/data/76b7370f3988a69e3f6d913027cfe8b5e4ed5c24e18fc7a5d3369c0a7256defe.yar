rule auto_rule_20250727010237_7405 {
  strings:
    $o0 = "copy_start" wide ascii nocase
    $o1 = "dword_40E524" wide ascii nocase
    $o2 = "byte_407E80" wide ascii nocase
    $o3 = "byte_40E9BC" wide ascii nocase
  condition:
    4 of ($o*)
}