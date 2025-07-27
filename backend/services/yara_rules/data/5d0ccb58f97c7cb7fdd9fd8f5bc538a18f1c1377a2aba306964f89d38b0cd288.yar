rule auto_rule_20250726104911_2852 {
  strings:
    $o0 = "dword_418250" wide ascii nocase
    $o1 = "aClasses" wide ascii nocase
    $o2 = "aSoftware" wide ascii nocase
  condition:
    3 of ($o*)
}