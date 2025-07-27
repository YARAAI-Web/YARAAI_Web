rule auto_rule_20250726165745_0587 {
  strings:
    $o0 = "GetPriorityClass" wide ascii nocase
    $o1 = "TrailDown2" wide ascii nocase
    $o2 = "__from_strstr_to_strchr" wide ascii nocase
  condition:
    3 of ($o*)
}