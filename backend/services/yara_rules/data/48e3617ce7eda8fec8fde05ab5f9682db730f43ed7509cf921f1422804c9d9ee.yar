rule auto_rule_20250726165644_6609 {
  strings:
    $o0 = "ulOptions" wide ascii nocase
    $o1 = "dword_4183C0" wide ascii nocase
    $o2 = "dword_417570" wide ascii nocase
  condition:
    3 of ($o*)
}