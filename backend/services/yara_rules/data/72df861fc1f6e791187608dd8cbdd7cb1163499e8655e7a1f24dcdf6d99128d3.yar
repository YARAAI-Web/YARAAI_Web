rule auto_rule_20250726064135_7491 {
  strings:
    $o0 = "__from_strstr_to_strchr" wide ascii nocase
    $o1 = "off_46E3E4" wide ascii nocase
    $o2 = "dword_46E5A8" wide ascii nocase
    $o3 = "dword_46E880" wide ascii nocase
  condition:
    4 of ($o*)
}