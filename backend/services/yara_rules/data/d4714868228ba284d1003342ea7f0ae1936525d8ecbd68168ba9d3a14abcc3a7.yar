rule auto_rule_20250727022256_5855 {
  strings:
    $o0 = "off_474E7C" wide ascii nocase
    $o1 = "dword_474A48" wide ascii nocase
    $o2 = "__from_strstr_to_strchr" wide ascii nocase
  condition:
    3 of ($o*)
}