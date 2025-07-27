rule auto_rule_20250726101714_5759 {
  strings:
    $o0 = "dword_458264" wide ascii nocase
    $o1 = "__from_strstr_to_strchr" wide ascii nocase
    $o2 = "algn_458032" wide ascii nocase
  condition:
    3 of ($o*)
}