rule auto_rule_20250726103033_8945 {
  strings:
    $o0 = "xFFFFFDDF" wide ascii nocase
    $o1 = "x62Fu" wide ascii nocase
    $o2 = "general" wide ascii nocase
  condition:
    3 of ($o*)
}