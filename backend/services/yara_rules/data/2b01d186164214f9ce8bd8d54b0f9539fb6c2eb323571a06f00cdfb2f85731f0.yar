rule auto_rule_20250727033812_6458 {
  strings:
    $o0 = "dword_1E6A4" wide ascii nocase
    $o1 = "ZwQueryInformationProcess" wide ascii nocase
  condition:
    all of them
}