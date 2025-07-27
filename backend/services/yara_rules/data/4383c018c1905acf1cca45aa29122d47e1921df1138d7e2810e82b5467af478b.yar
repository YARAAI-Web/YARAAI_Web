rule auto_rule_20250727003823_6152 {
  strings:
    $o0 = "dword_435004" wide ascii nocase
    $o1 = "off_43A2D4" wide ascii nocase
  condition:
    all of them
}