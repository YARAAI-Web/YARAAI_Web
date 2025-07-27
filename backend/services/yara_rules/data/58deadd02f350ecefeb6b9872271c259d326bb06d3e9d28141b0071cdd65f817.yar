rule auto_rule_20250727011820_1117 {
  strings:
    $o0 = "byte_40FDC8" wide ascii nocase
    $o1 = "VisualC" wide ascii nocase
  condition:
    all of them
}