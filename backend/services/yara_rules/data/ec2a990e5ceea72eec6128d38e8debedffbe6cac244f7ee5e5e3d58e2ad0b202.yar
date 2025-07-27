rule auto_rule_20250726101947_1029 {
  strings:
    $o0 = "DllEntryPoint" wide ascii nocase
    $o1 = "FileA" wide ascii nocase
    $o2 = "dword_10003148" wide ascii nocase
  condition:
    3 of ($o*)
}