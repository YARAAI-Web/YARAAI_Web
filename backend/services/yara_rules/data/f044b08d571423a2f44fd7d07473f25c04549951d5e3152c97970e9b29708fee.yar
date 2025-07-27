rule auto_rule_20250727035606_5882 {
  strings:
    $o0 = "dword_7832C" wide ascii nocase
    $o1 = "dword_782E0" wide ascii nocase
    $o2 = "asc_1ECEA" wide ascii nocase
  condition:
    3 of ($o*)
}