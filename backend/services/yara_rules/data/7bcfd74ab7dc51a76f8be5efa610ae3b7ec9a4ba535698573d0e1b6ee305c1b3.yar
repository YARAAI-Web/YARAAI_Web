rule auto_rule_20250727034855_3053 {
  strings:
    $o0 = "__crtInitCritSecNoSpinCount" wide ascii nocase
    $o1 = "dword_4794A4" wide ascii nocase
    $o2 = "__from_strstr_to_strchr" wide ascii nocase
  condition:
    3 of ($o*)
}