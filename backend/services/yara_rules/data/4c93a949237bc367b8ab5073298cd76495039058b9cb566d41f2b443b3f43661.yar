rule auto_rule_20250726060804_3150 {
  strings:
    $o0 = "dword_407358" wide ascii nocase
    $o1 = "dword_407008" wide ascii nocase
    $o2 = "ProcessWindowStation" wide ascii nocase
    $o3 = "Runtime" wide ascii nocase
  condition:
    4 of ($o*)
}