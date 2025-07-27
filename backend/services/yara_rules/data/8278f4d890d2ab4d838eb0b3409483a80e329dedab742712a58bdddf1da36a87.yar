rule auto_rule_20250726170825_7895 {
  strings:
    $o0 = "dword_77CA8" wide ascii nocase
    $o1 = "dword_77B78" wide ascii nocase
    $o2 = "dword_77AB4" wide ascii nocase
    $o3 = "asc_1F5A2" wide ascii nocase
  condition:
    4 of ($o*)
}