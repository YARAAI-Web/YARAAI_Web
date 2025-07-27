rule auto_rule_20250726144905_6590 {
  strings:
    $o0 = "ReturnValue" wide ascii nocase
    $o1 = "dword_40CFD0" wide ascii nocase
    $o2 = "GetStringTypeW" wide ascii nocase
  condition:
    3 of ($o*)
}