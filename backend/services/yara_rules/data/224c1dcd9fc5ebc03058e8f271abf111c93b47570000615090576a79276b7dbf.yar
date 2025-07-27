rule auto_rule_20250726160736_2096 {
  strings:
    $o0 = "fstcw" wide ascii nocase
    $o1 = "tbyte_49291A" wide ascii nocase
    $o2 = "negative_x_0" wide ascii nocase
    $o3 = "_startOneArgErrorHandling" wide ascii nocase
    $o4 = "IsThemeActive" wide ascii nocase
  condition:
    4 of ($o*)
}