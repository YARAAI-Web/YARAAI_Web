rule auto_rule_20250726214947_4738 {
  strings:
    $o0 = "dword_4C1694" wide ascii nocase
    $o1 = "String1e" wide ascii nocase
    $o2 = "dword_4C1264" wide ascii nocase
  condition:
    3 of ($o*)
}