rule auto_rule_20250727004338_1631 {
  strings:
    $o0 = "__from_strstr_to_strchr" wide ascii nocase
    $o1 = "dword_4729B0" wide ascii nocase
    $o2 = "GetLocaleInfoA" wide ascii nocase
  condition:
    3 of ($o*)
}