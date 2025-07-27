rule auto_rule_20250726215825_3110 {
  strings:
    $o0 = "GetKeyNameTextW" wide ascii nocase
    $o1 = "IsCharUpperA" wide ascii nocase
    $o2 = "GetUpdateRect" wide ascii nocase
  condition:
    3 of ($o*)
}