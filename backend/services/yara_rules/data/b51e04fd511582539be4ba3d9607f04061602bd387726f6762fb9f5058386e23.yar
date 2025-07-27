rule auto_rule_20250726141154_1975 {
  strings:
    $o0 = "dword_47876C" wide ascii nocase
    $o1 = "__from_strstr_to_strchr" wide ascii nocase
    $o2 = "UnwindUp4_0" wide ascii nocase
  condition:
    3 of ($o*)
}