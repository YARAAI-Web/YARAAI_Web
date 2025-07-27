rule auto_rule_20250726234727_4731 {
  strings:
    $o0 = "cchMaxCount" wide ascii nocase
    $o1 = "LookupIconIdFromDirectory" wide ascii nocase
    $o2 = "DefDlgProcA" wide ascii nocase
  condition:
    3 of ($o*)
}