rule auto_rule_20250726201748_3080 {
  strings:
    $o0 = "xmmword_14007D360" wide ascii nocase
    $o1 = "_Node_if" wide ascii nocase
    $o2 = "xmmword_14007CA70" wide ascii nocase
    $o3 = "xmmword_14007CF00" wide ascii nocase
  condition:
    4 of ($o*)
}