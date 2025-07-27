rule auto_rule_20250727011225_7133 {
  strings:
    $o0 = "_wincmdln" wide ascii nocase
    $o1 = "xFEDu" wide ascii nocase
    $o2 = "write_string" wide ascii nocase
  condition:
    3 of ($o*)
}