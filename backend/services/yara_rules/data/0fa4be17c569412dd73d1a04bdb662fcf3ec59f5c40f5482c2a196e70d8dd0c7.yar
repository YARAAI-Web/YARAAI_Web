rule auto_rule_20250726120052_1489 {
  strings:
    $o0 = "x415700" wide ascii nocase
    $o1 = "_NLG_Notify" wide ascii nocase
    $o2 = "__from_strstr_to_strchr" wide ascii nocase
  condition:
    3 of ($o*)
}