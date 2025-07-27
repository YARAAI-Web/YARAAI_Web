rule auto_rule_20250726124730_7692 {
  strings:
    $o0 = "dword_472678" wide ascii nocase
    $o1 = "dword_472650" wide ascii nocase
    $o2 = "CopyUnwindUp_0" wide ascii nocase
    $o3 = "off_471920" wide ascii nocase
  condition:
    4 of ($o*)
}