rule auto_rule_20250726143516_2086 {
  strings:
    $o0 = "GetPrivateProfileStringW" wide ascii nocase
    $o1 = "dword_40CE4C" wide ascii nocase
    $o2 = "dword_40CE54" wide ascii nocase
  condition:
    3 of ($o*)
}